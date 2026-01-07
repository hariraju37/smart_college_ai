student_memory = {}

def update_memory(student_id, action):
    if student_id not in student_memory:
        student_memory[student_id] = []
    student_memory[student_id].append(action)

def get_memory(student_id):
    return student_memory.get(student_id, [])
