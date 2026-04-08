from presentation_layer.terminal import Terminal
from service_layer.student_service import StudentService
from service_layer.class_service import ClassService
from service_layer.professor_service import ProfessorService


if __name__ == "__main__":
    
    terminal = Terminal(StudentService(), ProfessorService(), ClassService())
    while(terminal.running):
        terminal.current_menu.render()
    print("...Goodbye!")