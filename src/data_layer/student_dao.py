from data_layer.db_connection_manager import get_connection
from Models.student import Student

def get_student_by_id(id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students WHERE id = %s", [id])
        return cursor.fetchone()

def save(new_student: Student):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("INSERT INTO students (first_name,last_name,major,email,year) VALUES (%s,%s,%s,%s,%s)",[new_student.first_name,new_student.last_name,new_student.major, new_student.email,new_student.year])
        
        new_id = cursor.lastrowid
        return get_student_by_id(new_id)
    
def remove(id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("DELETE FROM students WHERE id = %s",[id])

def get_all_students():
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students")
        return cursor.fetchall()
    
def get_courses(id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT course_id FROM enrollments WHERE student_id = %s", [id])
        return cursor.fetchall()

def update_major(new_major: str, id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE students SET major = %s WHERE id = %s", [new_major,id])

def update_year(new_year: str, id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE students SET year = %s WHERE id = %s", [new_year,id])

def update_email(new_email: str, id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE students SET email = %s WHERE id = %s", [new_email,id])

def update_first_name(new_first_name: str, id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE students SET first_name = %s WHERE id = %s", [new_first_name,id])

def update_last_name(new_last_name: str, id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE students SET first_name = %s WHERE id = %s", [new_last_name,id])