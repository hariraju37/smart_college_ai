def plan_tasks(notice_text):
    tasks = []

    if "exam" in notice_text.lower():
        tasks.append("Add exam reminder")

    if "assignment" in notice_text.lower():
        tasks.append("Add assignment deadline")

    return tasks
