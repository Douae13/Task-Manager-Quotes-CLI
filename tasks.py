import db

def add_task(user_id, task):
    conn = db.get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO tasks (user_id, task) VALUES (?, ?)", (user_id, task))

    conn.commit()
    conn.close()

def view_tasks(user_id):
    conn = db.get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, task, done FROM tasks WHERE user_id=?",
        (user_id,)
    )

    tasks = cursor.fetchall()
    conn.close()

    return tasks

def mark_done(task_id):
    conn = db.get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tasks SET done=1 WHERE id=?",
        (task_id,)
    )

    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = db.get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id=?",
        (task_id,)
    )

    conn.commit()
    conn.close()