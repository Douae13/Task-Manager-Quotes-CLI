import db
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    conn = db.get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                    (username, hash_password(password)))
        
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()


def login(username, password):
    conn = db.get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id from users WHERE username=? and password=?",
                   (username, hash_password(password)))
    
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return user[0]
    return None