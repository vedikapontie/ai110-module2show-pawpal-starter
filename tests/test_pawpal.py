from datetime import datetime

from pawpal_system import Owner, Pet, Scheduler, Task


def test_task_completion():
    task = Task(title="Morning Walk", description="Take a short walk")

    assert task.completion_status is False

    task.mark_complete()

    assert task.completion_status is True


def test_task_addition():
    pet = Pet(pet_id="pet-1", name="Mochi", species="dog", age=3)
    task = Task(title="Feed Breakfast", description="Serve breakfast")

    initial_count = len(pet.tasks)

    pet.add_task(task)

    assert len(pet.tasks) == initial_count + 1
    assert task in pet.tasks


def test_scheduler_orders_tasks_by_time():
    owner = Owner(owner_id="owner-1", name="Jordan")
    pet = Pet(pet_id="pet-1", name="Mochi", species="dog", age=3)
    owner.add_pet(pet)

    later_task = Task(title="Dinner Prep", description="Prepare dinner", time="20:00")
    earlier_task = Task(title="Morning Walk", description="Take a walk", time="07:30")
    pet.add_task(later_task)
    pet.add_task(earlier_task)

    scheduler = Scheduler(scheduler_id="scheduler-1")
    plan = scheduler.compile_tasks_for_owner(owner)

    assert [task.time for task in plan] == ["07:30", "20:00"]


def test_scheduler_filters_tasks_by_pet_and_status():
    owner = Owner(owner_id="owner-1", name="Jordan")
    mochi = Pet(pet_id="pet-1", name="Mochi", species="dog", age=3)
    luna = Pet(pet_id="pet-2", name="Luna", species="cat", age=2)
    owner.add_pet(mochi)
    owner.add_pet(luna)

    pending_task = Task(title="Feed Mochi", description="Feed food", time="08:00", completion_status=False)
    completed_task = Task(title="Clean Litter", description="Clean litter", time="20:00", completion_status=True)
    mochi.add_task(pending_task)
    luna.add_task(completed_task)

    scheduler = Scheduler(scheduler_id="scheduler-1")
    filtered = scheduler.filter_tasks(owner.get_all_tasks(), pet_name="Mochi", completed=False)

    assert len(filtered) == 1
    assert filtered[0].title == "Feed Mochi"


def test_recurring_task_creates_next_instance_on_completion():
    pet = Pet(pet_id="pet-1", name="Mochi", species="dog", age=3)
    task = Task(title="Morning Walk", description="Take a walk", time="07:30", frequency="Daily")
    pet.add_task(task)

    next_task = task.mark_complete(pet=pet)

    assert task.completion_status is True
    assert next_task is not None
    assert next_task.completion_status is False
    assert next_task in pet.tasks
    assert next_task.frequency == "Daily"


def test_conflict_detection_returns_warning_for_same_time():
    scheduler = Scheduler(scheduler_id="scheduler-1")
    tasks = [
        Task(title="Morning Walk", description="Walk", time="08:00"),
        Task(title="Feed Breakfast", description="Feed", time="08:00"),
    ]

    warnings = scheduler.detect_conflicts(tasks)

    assert len(warnings) == 1
    assert "08:00" in warnings[0]


def test_recurring_task_uses_next_due_date():
    pet = Pet(pet_id="pet-1", name="Mochi", species="dog", age=3)
    task = Task(
        title="Morning Walk",
        description="Take a walk",
        time="07:30",
        frequency="Daily",
        due_date=datetime(2026, 1, 1, 8, 0),
    )
    pet.add_task(task)

    next_task = task.mark_complete(pet=pet)

    assert next_task is not None
    assert next_task.due_date == datetime(2026, 1, 2, 8, 0)
