from fastapi import FastAPI
from tools.notice_reader import read_notice
from agent.planner import plan_tasks
from agent.memory import update_memory, get_memory
from agent.decision import decide_priority
from tools.calendar_tool import add_to_calendar
from tools.reminder import send_reminder

app = FastAPI()

@app.post("/process_notice/")
def process_notice(student_id: str, pdf_path: str):
    notice = read_notice(pdf_path)
    tasks = plan_tasks(notice)

    history = get_memory(student_id)
    final_tasks = decide_priority(tasks, history)

    for task in final_tasks:
        add_to_calendar(task)
        send_reminder(student_id, task)

    update_memory(student_id, "notice_processed")

    return {"status": "success", "tasks": final_tasks}
