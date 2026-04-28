import db

def add_task(user_id, task):
    conn = db.get_connection
    cursor = conn.cursor()

    cursor.execute("INSERT INTO tasks (user_id, task) VALUES (?, ?)", (user_id, task))

    conn.commit()
    conn.close()