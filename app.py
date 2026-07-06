from datetime import datetime

import streamlit as st

from pawpal_system import Owner, Pet, Scheduler, Task

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
                task_text = f"- {task.title} at {task.time} ({status}{due_text})"

                if task.completion_status:
                    st.markdown(f"<div style='opacity:0.5'>{task_text}</div>", unsafe_allow_html=True)
                else:
                    st.write(task_text)

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
st.caption("Your active itinerary is sorted, filtered, and formatted for quick review.")

scheduler = Scheduler(scheduler_id="scheduler-1")
all_tasks = []
for pet in owner.get_pets():
    all_tasks.extend(pet.tasks)

if all_tasks:
    conflict_warning = scheduler.check_conflicts(all_tasks)
    if conflict_warning:
        st.warning(f"⚠️ {conflict_warning}")

    with st.sidebar:
        st.subheader("Schedule Filters")
        pet_filter = st.selectbox("Filter by pet", ["All pets", *sorted({pet.name for pet in owner.get_pets()})])
        status_filter = st.selectbox("Filter by status", ["All", "Pending", "Completed"])

    if pet_filter != "All pets":
        filtered_tasks = scheduler.filter_tasks(all_tasks, pet_name=pet_filter)
    else:
        filtered_tasks = list(all_tasks)

    if status_filter == "Pending":
        filtered_tasks = scheduler.filter_tasks(filtered_tasks, status=False)
    elif status_filter == "Completed":
        filtered_tasks = scheduler.filter_tasks(filtered_tasks, status=True)

    ordered_tasks = scheduler.sort_by_time(filtered_tasks)

    if ordered_tasks:
        st.success("Your schedule has been arranged chronologically.")
        schedule_data = []
        for task in ordered_tasks:
            pet_name = task.pet.name if task.pet else "Unknown"
            status_text = "✅ Completed" if task.completion_status else "⏳ Pending"
            schedule_data.append(
                {
                    "Time": task.time,
                    "Pet": pet_name,
                    "Task": task.title,
                    "Status": status_text,
                    "Frequency": task.frequency,
                }
            )

        st.dataframe(schedule_data, use_container_width=True)
    else:
        st.info("No tasks match the selected filters.")
else:
    st.info("Schedule tasks first to view your itinerary.")
