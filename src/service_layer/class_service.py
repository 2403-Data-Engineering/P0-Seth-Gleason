from Models.course import Course
import data_layer.course_dao as course_dao
class ClassService:

    def save(self, course: Course) -> Course:
        return course_dao.save(course)
    
    def get_by_id(self, id: int) -> Course:
        return course_dao.get_course_by_id(id)

    def get_all_courses(self):
        return course_dao.get_all_courses()

    def assign_professor(self, course_id:int, professor_id: int) -> None:
        course_dao.assign_professor(course_id, professor_id)

    def update_name(self, id: int, name: str) -> None:
        course_dao.update_name(id, name)

    def enroll_student(self, student_id: int, course_id: int) -> None:
        course_dao.enroll_student(student_id, course_id)

    def drop_student_from_course(self, student_id: int, course_id: int) -> None:
        course_dao.drop_student_from_course(student_id, course_id)

    def get_students_in_course(self, course_id: int):
        return course_dao.get_students_in_course(course_id)

    def remove(self, course_id: int):
        course_dao.remove(course_id)

    def get_professors_courses(self, professor_id: int):
        return course_dao.get_professors_courses(professor_id)
    
        
        