def decide_priority(tasks, student_history):
    priority_tasks = []

    for task in tasks:
        if "deadline missed" in student_history:
            priority_tasks.append("URGENT: " + task)
        else:
            priority_tasks.append(task)

    return priority_tasks
