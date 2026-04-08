from data_layer.db_connection_manager import get_connection
from Models.professor import Professor

def get_professor_by_id(id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM professors WHERE id = %s", [id])
        return cursor.fetchone()

def save(new_professor: Professor):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("INSERT INTO professors (first_name,last_name,department,email) VALUES (%s,%s,%s,%s)",[new_professor.first_name,new_professor.last_name,new_professor.department, new_professor.email])
        
        new_id = cursor.lastrowid
        return get_professor_by_id(new_id)
    
def remove(id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("DELETE FROM professors WHERE id = %s",[id])

def get_all_professors():
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM professors")
        return cursor.fetchall()
    
def update_email(new_email: str, id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE professors SET email = %s WHERE id = %s", [new_email,id])

def update_first_name(new_first_name: str, id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE professors SET first_name = %s WHERE id = %s", [new_first_name,id])

def update_last_name(new_last_name: str, id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE professors SET first_name = %s WHERE id = %s", [new_last_name,id])

def update_department(department: str, id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE courses SET department = %s WHERE id = %s", [department, id])
        