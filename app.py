from datetime import datetime

import streamlit as st

from pawpal_system import Owner, Pet, Task

if "owner" not in st.session_state:
    st.session_state["owner"] = Owner(owner_id="owner-1", name="Jordan")

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

owner = st.session_state["owner"]

st.subheader("Add a Pet")
with st.form("add_pet_form"):
    pet_name = st.text_input("Pet name")
    species = st.selectbox("Species", ["dog", "cat", "other"])
    age = st.number_input("Age", min_value=0, max_value=30, value=1)
    submitted_pet = st.form_submit_button("Add pet")

    if submitted_pet:
        if pet_name.strip():
            pet = Pet(
                pet_id=f"pet-{len(owner.get_pets()) + 1}",
                name=pet_name.strip(),
                species=species,
                age=int(age),
            )
            owner.add_pet(pet)
            st.success(f"{pet.name} was added to your account.")
        else:
            st.warning("Please enter a pet name.")

st.subheader("Schedule a Task")
if owner.get_pets():
    with st.form("schedule_task_form"):
        pet_names = [pet.name for pet in owner.get_pets()]
        selected_pet_name = st.selectbox("Choose pet", pet_names)
        selected_pet = next(pet for pet in owner.get_pets() if pet.name == selected_pet_name)

        task_title = st.text_input("Task title")
        task_description = st.text_area("Description")
        task_time = st.text_input("Time (HH:MM)", value="09:00")
        frequency = st.selectbox("Frequency", ["Daily", "Weekly", "Monthly"])
        submitted_task = st.form_submit_button("Schedule task")

        if submitted_task:
            if task_title.strip():
                task = Task(
                    title=task_title.strip(),
                    description=task_description.strip(),
                    time=task_time.strip(),
                    frequency=frequency,
                    due_date=datetime.now(),
                )
                selected_pet.add_task(task)
                st.success(f"{task.title} was scheduled for {selected_pet.name}.")
            else:
                st.warning("Please enter a task title.")
else:
    st.info("Add a pet first before scheduling tasks.")

st.divider()

st.subheader("Current Pets and Tasks")
if owner.get_pets():
    for pet in owner.get_pets():
        st.write(f"**{pet.name}** ({pet.species}, age {pet.age})")
        if pet.tasks:
            for task in pet.tasks:
                status = "Done" if task.completion_status else "Pending"
                due_text = f" | due {task.due_date.strftime('%Y-%m-%d')}" if task.due_date else ""
                st.write(f"- {task.title} at {task.time} ({status}{due_text})")
                if not task.completion_status and task.frequency.lower() in {"daily", "weekly"}:
                    if st.button(
                        f"Mark complete: {task.title}",
                        key=f"complete_{pet.pet_id}_{task.title}_{id(task)}",
                    ):
                        task.mark_complete(pet=pet)
                        st.success(f"{task.title} marked complete and the next occurrence was added.")
        else:
            st.write("- No tasks yet")
else:
    st.info("No pets yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    st.warning(
        "Not implemented yet. Next step: create your scheduling logic (classes/functions) and call it here."
    )
    st.markdown(
        """
Suggested approach:
1. Design your UML (draft).
2. Create class stubs (no logic).
3. Implement scheduling behavior.
4. Connect your scheduler here and display results.
"""
    )
