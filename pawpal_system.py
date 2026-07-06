from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
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

    def mark_complete(self) -> None:
        """Mark the task as completed."""
        self.completion_status = True


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
        """Compile and sort all pending tasks for an owner's pets."""
        if not isinstance(owner, Owner):
            raise TypeError("owner must be an Owner instance")

        pet_list = owner.get_pets()
        task_list: List[Task] = []
        for pet in pet_list:
            task_list.extend(pet.tasks)

        pending_tasks = [task for task in task_list if not task.completion_status]
        pending_tasks.sort(key=self._task_sort_key)

        self.generated_at = datetime.now()
        self.plan = pending_tasks
        return self.plan

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
