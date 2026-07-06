from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Optional


@dataclass
class Task:
    """Represent a single pet-care task with timing and completion state."""
    title: str
    description: str = ""
    time: str = "09:00"
    frequency: str = "Daily"
    completion_status: bool = False
    task_id: str = ""
    pet: Optional["Pet"] = None
    due_date: Optional[datetime] = None

    def mark_complete(self, pet: Optional["Pet"] = None) -> Optional["Task"]:
        """Mark the task as completed and create the next recurring instance when needed."""
        self.completion_status = True

        if pet is None:
            return None

        if self.frequency.lower() in {"daily", "weekly"}:
            base_date = self.due_date or datetime.now()
            interval = timedelta(days=1 if self.frequency.lower() == "daily" else 7)
            next_due_date = base_date + interval

            next_task = Task(
                title=self.title,
                description=self.description,
                time=self.time,
                frequency=self.frequency,
                completion_status=False,
                task_id="",
                pet=pet,
                due_date=next_due_date,
            )
            pet.add_task(next_task)
            return next_task

        return None


@dataclass
class Pet:
    """Represent a pet and the tasks associated with it."""
    pet_id: str
    name: str
    species: str = "other"
    age: int = 0
    tasks: List[Task] = field(default_factory=list)
    owner: Optional["Owner"] = None

    def add_task(self, task: Task) -> None:
        """Add a task to the pet and link it to this pet."""
        if task not in self.tasks:
            self.tasks.append(task)
            task.pet = self


class Owner:
    """Represent a pet owner and their registered pets."""
    def __init__(
        self,
        owner_id: str,
        name: str,
        email: str = "",
        preferences: Optional[List[str]] = None,
        created_at: Optional[datetime] = None,
    ) -> None:
        self.owner_id = owner_id
        self.name = name
        self.email = email
        self.preferences = preferences or []
        self.created_at = created_at or datetime.now()
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's profile."""
        if pet not in self.pets:
            self.pets.append(pet)
            pet.owner = self

    def get_pets(self) -> List[Pet]:
        """Return a copy of the owner's pets."""
        return list(self.pets)

    def get_all_tasks(self) -> List[Task]:
        """Collect all tasks from every pet owned by this owner."""
        all_tasks: List[Task] = []
        for pet in self.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks


class Scheduler:
    """Organize and compile pet-care tasks for an owner."""
    def __init__(self, scheduler_id: str = "scheduler-1") -> None:
        """Initialize the scheduler with an identifier."""
        self.scheduler_id = scheduler_id
        self.generated_at: Optional[datetime] = None
        self.plan: List[Task] = []

    def compile_tasks_for_owner(self, owner: Owner) -> List[Task]:
        """Compile, filter, sort, and annotate all pending tasks for an owner's pets."""
        if not isinstance(owner, Owner):
            raise TypeError("owner must be an Owner instance")

        pet_list = owner.get_pets()
        task_list: List[Task] = []
        for pet in pet_list:
            task_list.extend(pet.tasks)

        pending_tasks = self.filter_tasks(task_list, completed=False)
        pending_tasks = self.sort_tasks(pending_tasks)
        self.generated_at = datetime.now()
        self.plan = pending_tasks
        return self.plan

    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        """Return tasks sorted chronologically by their HH:MM time string."""
        return sorted(tasks, key=lambda task: task.time)

    def filter_tasks(
        self,
        tasks: List[Task],
        pet_name: Optional[str] = None,
        status: Optional[bool] = None,
        completed: Optional[bool] = None,
    ) -> List[Task]:
        """Filter tasks by pet name, completion status, or both criteria."""
        if completed is not None and status is None:
            status = completed

        filtered_tasks: List[Task] = []
        for task in tasks:
            pet_matches = pet_name is None or (task.pet is not None and task.pet.name.lower() == pet_name.lower())
            status_matches = status is None or task.completion_status is status
            if pet_matches and status_matches:
                filtered_tasks.append(task)
        return filtered_tasks

    def sort_tasks(self, tasks: List[Task]) -> List[Task]:
        """Sort tasks chronologically by their scheduled time."""
        return self.sort_by_time(tasks)

    def check_conflicts(self, tasks: List[Task]) -> Optional[str]:
        """Return a warning string when two active tasks share the same HH:MM time."""
        active_tasks = [task for task in tasks if not task.completion_status]
        seen_times = set()
        for task in active_tasks:
            if task.time in seen_times:
                return f"Warning: Multiple tasks are scheduled at {task.time}!"
            seen_times.add(task.time)
        return None

    def detect_conflicts(self, tasks: List[Task]) -> List[str]:
        """Return warning messages for active tasks sharing the same scheduled time."""
        warnings: List[str] = []
        time_map: dict[int, List[Task]] = {}
        for task in tasks:
            if task.completion_status:
                continue
            minute_value = self._time_to_minutes(task.time)
            time_map.setdefault(minute_value, []).append(task)

        for minute_value, grouped_tasks in time_map.items():
            if len(grouped_tasks) > 1:
                task_names = ", ".join(task.title for task in grouped_tasks)
                warnings.append(f"Warning: {task_names} are scheduled for {self._minutes_to_time(minute_value)}.")
        return warnings

    def _task_sort_key(self, task: Task) -> tuple[int, int, str]:
        """Return the sort key used to order tasks."""
        return (self._time_to_minutes(task.time), task.frequency.lower() != "daily", task.title.lower())

    def _time_to_minutes(self, time_value: str) -> int:
        """Convert an HH:MM time string into minutes since midnight."""
        try:
            hour_text, minute_text = time_value.split(":", 1)
            hour = int(hour_text)
            minute = int(minute_text)
            return hour * 60 + minute
        except ValueError:
            return 24 * 60

    def _minutes_to_time(self, minutes: int) -> str:
        """Convert minutes since midnight back into HH:MM."""
        hour = minutes // 60
        minute = minutes % 60
        return f"{hour:02d}:{minute:02d}"
