from presentation_layer.menu import Menu, Validator
from Models.student import Student
from Models.course import Course
from service_layer.class_service import ClassService



class EnrollmentMenu(Menu):
    def render(self):
        print("""
-=-=-=-=-=-=-=-=-
Enrollment Menu
-=-=-=-=-=-=-=-=-   
              
1) Enroll Student in course
2) Remove Student from course
              """)
        
        user_input = input().lower()

        match user_input:
            case '1':
                student_id = int(self.get_input("Enter student id: ", Validator.ID))
                course_id = int(self.get_input("Enter course id: ", Validator.ID))
                self.terminal.class_service.enroll_student(student_id, course_id)

            case '2':
                student_id = int(self.get_input("Enter student id: ", Validator.ID))
                course_id = int(self.get_input("Enter course id: ", Validator.ID))
                self.terminal.class_service.drop_student_from_course(student_id, course_id)

        self.terminal.navigate('main_menu')       


        

