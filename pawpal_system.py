from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass
class Task:
    task_id: str
    title: str
    description: str = ""
    duration_minutes: int = 0
    priority: str = "medium"
    scheduled_time: Optional[datetime] = None
    is_completed: bool = False
    created_at: datetime = field(default_factory=datetime.now)

    def mark_complete(self) -> None:
        pass

    def update_schedule(self, scheduled_time: datetime) -> None:
        pass


@dataclass
class Pet:
    pet_id: str
    name: str
    species: str = "other"
    age: int = 0
    notes: str = ""
    created_at: datetime = field(default_factory=datetime.now)
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        pass

    def remove_task(self, task_id: str) -> None:
        pass


class Owner:
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
        pass

    def remove_pet(self, pet_id: str) -> None:
        pass


class Scheduler:
    def __init__(self, scheduler_id: str = "scheduler-1") -> None:
        self.scheduler_id = scheduler_id
        self.generated_at: Optional[datetime] = None
        self.plan: List[Task] = []

    def schedule_tasks(self, tasks: List[Task], pets: List[Pet], owner: Owner) -> List[Task]:
        return []

    def sort_tasks(self, tasks: List[Task]) -> List[Task]:
        return []

    def detect_conflicts(self, tasks: List[Task]) -> List[Task]:
        return []

    def explain_plan(self) -> str:
        return ""
