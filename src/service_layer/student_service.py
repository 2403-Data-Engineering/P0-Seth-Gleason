from Models.student import Student
import data_layer.student_dao as student_dao

class StudentService:

    def save(self, student: Student) -> Student:
        return student_dao.save(student)

    def get_by_id(self, id: int) -> Student:
        return student_dao.get_student_by_id(id)
    
    def remove(self, id: int):
        student_dao.remove(id)

    def get_all_students(self):
        return student_dao.get_all_students()
    
    def update_email(self, new_email: str, id: int):
        student_dao.update_email(new_email, id)

    def update_first_name(self, new_first_name: str, id: int):
        student_dao.update_first_name(new_first_name, id)

    def update_last_name(self, new_last_name: str, id: int):
        student_dao.update_last_name(new_last_name, id)

    def update_major(self, major: str, id: int):
        student_dao.update_major(major, id)

    def update_year(self, year: str, id: int):
        student_dao.update_year(year, id)

    def get_name(self, id: int):
        first_name = student_dao.get_student_by_id(id).get('first_name')
        last_name = student_dao.get_student_by_id(id).get('last_name')

        return first_name + " " + last_name

    def get_courses(self, id: int):
        return student_dao.get_courses(id)