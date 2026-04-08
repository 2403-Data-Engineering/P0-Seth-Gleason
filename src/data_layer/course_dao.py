from data_layer.db_connection_manager import get_connection
from Models.course import Course
# from Models.professor import Professor
# from Models.student import Student

def get_course_by_id(id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM courses WHERE id = %s", [id])
        return cursor.fetchone()

def save(new_course: Course):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("INSERT INTO courses (name, professor_id) VALUES (%s,%s)", [new_course.name, new_course.professor_id])
        new_id = cursor.lastrowid
        return get_course_by_id(new_id)
    
def get_all_courses():
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM courses")
        return cursor.fetchall()

def assign_professor(course_id: int, professor_id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE courses SET professor_id = %s WHERE id = %s", [professor_id,course_id])

def update_name(id: int, name: str):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE courses SET name = %s WHERE id = %s", [name, id])

def enroll_student(student_id: int, course_id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("INSERT INTO enrollments (student_id, course_id) VALUES (%s,%s)", [student_id, course_id])

def drop_student_from_course(student_id: int, course_id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("DELETE FROM enrollments WHERE student_id = %s, course_id = %s" [student_id, course_id])

def get_students_in_course(course_id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT student_id FROM enrollments WHERE course_id = %s", [course_id])
        return cursor.fetchall()
    
def remove(course_id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("DELETE FROM professors WHERE id = %s", [course_id])