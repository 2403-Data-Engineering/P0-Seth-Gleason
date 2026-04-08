from service_layer.student_service import StudentService
from service_layer.professor_service import ProfessorService
from service_layer.class_service import ClassService
from presentation_layer.main_menu import MainMenu
from presentation_layer.new_class_menu import NewClassMenu
from presentation_layer.new_professor_menu import NewProfessorMenu
from presentation_layer.new_student_menu import NewStudentMenu
from presentation_layer.enrollment_menu import EnrollmentMenu
from presentation_layer.update_student_menu import UpdateStudentMenu
from presentation_layer.update_professor_menu import UpdateProfessorMenu
from presentation_layer.update_class_menu import UpdateClassMenu
from presentation_layer.class_info_menu import ClassInfoMenu
from presentation_layer.student_info_menu import StudentInfoMenu
from presentation_layer.professor_info_menu import ProfessorInfoMenu
from presentation_layer.report_menu import ReportMenu

class Terminal:
    
    menu_map: dict
    
    def __init__(self, student_service: StudentService, professor_service: ProfessorService, class_service: ClassService):
        self.menu_map = {
            'main_menu': MainMenu(self),
            'new_student_menu': NewStudentMenu(self),
            'new_professor_menu': NewProfessorMenu(self),
            'new_class_menu': NewClassMenu(self),
            'enrollment_menu': EnrollmentMenu(self),
            'update_student_menu': UpdateStudentMenu(self),
            'update_professor_menu': UpdateProfessorMenu(self),
            'update_class_menu': UpdateClassMenu(self),
            'class_info_menu': ClassInfoMenu(self),
            'student_info_menu': StudentInfoMenu(self),
            'professor_info_menu': ProfessorInfoMenu(self),
            'report_menu': ReportMenu(self)

        }
        self.navigate('main_menu')
        self.running = True
        self.student_service = student_service
        self.professor_service = professor_service
        self.class_service = class_service


    def navigate(self, menu: str):
        self.current_menu = self.menu_map.get(menu)
            
    def quit(self):
        self.running = False
        print("Quitting...")