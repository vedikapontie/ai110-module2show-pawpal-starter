from pawpal_system import Pet, Task


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
