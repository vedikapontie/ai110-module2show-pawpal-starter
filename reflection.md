# PawPal+ Project Reflection

## 1. System Design
Three core actions that a user should be able to perform:
1. enter the user and pet information
2. add and edit pet care tasks such as a walk or doctor appointmet or grooming
3. access, view, and edit schedule

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

Based on the requirements, the initial UML design works around the four core classes in an optimal manner for scheduling coordination. The four classes that were used were Owner, Pet, Task, and Scheduler. The Owner class manages the user's profile information and has the access to the pet, essentially a container for the Pet objects. The Pet class has a data object which tracks the pets' information such as its name, species, and age. It also is the owner/manager of the tasks. The Task class has to hold the scheduled time, keep track of the description, amount of time, priority, and if the task has been completed. Finally, the schedule is the central brain which handles the operations, figuring out needs based on the pet/s, sorting chronologically based on times and priority, and detecting time conflicts. 

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

Yes I made a design change during implementation, there was a lack of the Pet being linked back to the Owner, I made sure to add that line of code just to have a way to cross check the relationship. Additionally, if there are multiple pets I also added a link from the Task to the Pet. 

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

My schedule considers the time immensely as a consraint. I decided this mattered the most due to the use of the scheduler, which is to plan out events based off of time. 

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

I made the scheduler check for conflicts by looking at the tasks that have the same starting time; however, it does not check how long a task takes. I believe that this tradeoff is reasonable because it allows the code to run simply without needing complex math. Although the user has to check for these it is fine because the schedule manager makes it clear when the next activity starts. I would like to implement this possibly in the future. 

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?


I used AI for brainstorming, debugging, and testing. I believe prompts that contained multiple requirements and specific targeted areas were the most helpful. 

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

I rejected an AI approach that produced too non-human text that was hard to read, I made sure everything made sense by running through the code and cross checking the code through multiple tests and making sure by running the app to confirm the expected behavior. Overall, I made sure I kept the code readable and testable. 
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested the chronological sorting of tasks based on the HH:MM format. I also made sure the reoccurence was actually taking place. In addition, I made sure that warning were created for duplicate tasks. These tests were important to make sure the user had a simple and straightforward experience. 
**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I am pretty confident that my scheduler works correctly, I would like to have added more requirements and that is something I will do in the future. Additional edge cases I would have tested are tasks with teh duration times that overlap as well as pets' activity times that overlap, and make a slight adjustment for timezones and daylight-savings transitions. 
---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

Overall, I am proud of the core model of the project and how it stayed consistent and efficent throughout. I also believe the tests were cruicial and went really well. 

**b. What you would improve**

- Add explicit task durations, smarter conflict resolution, persistent storage, and richer UI editing capabilities for tasks.
If I had more time I would improve the duration part and making sure that the timings don't overlap, I would also make separate areas for multiple pets, and I would make sure after a task got completed it got struckthrough and doesn't duplicate itself when it checks off. 
**c. Key takeaway**

- Keep models simple and verify AI output with tests and runtime checks. Human oversight—setting requirements, choosing tradeoffs, and validating code—remains essential when pairing with AI.

Overall my key takeaway was to consistently check the AI code, test it using pytest, and making sure to understand the tradeoffs being made, make intentional and smart decisions that are for the best interests of the app. 