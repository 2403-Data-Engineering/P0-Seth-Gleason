from menu import Menu
from new_class_menu import NewClassMenu
from new_professor_menu import NewProfessorMenu
from new_student_menu import NewStudentMenu
class MainMenu(Menu):
    def render(self) -> None:
        print("""
-=-=-=-=-=-=-=-=-=-=-=-
Please choose one of the following options
1) Add new student
2) Add new professor    
3) Add new class
4) Enroll student in class
5) Run Report                         
Q) Quit
        """)
        user_input = input().lower()
        match user_input:
            case "1":
                self.terminal.navigate(NewStudentMenu(self.terminal))
                
            case "2":
                self.terminal.navigate(NewProfessorMenu(self.terminal))
                
            case "3":
                self.terminal.navigate(NewClassMenu(self.terminal))
                
            case "4":
                #self.terminal.navigate(EnrollmentMenu(self.terminal))
                pass
            case "5":
                print("TO DO")
            case 'q':
                self.terminal.quit()