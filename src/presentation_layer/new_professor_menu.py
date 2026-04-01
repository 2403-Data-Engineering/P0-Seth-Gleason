from menu import Menu
from main_menu import MainMenu
from Models.professor import Professor

class NewProfessorMenu(Menu):
    def render(self) -> None:
        print("""
-=-=-=-=-=-=-=-=-=-
New Professor Menu
-=-=-=-=-=-=-=-=-=- 
              """)
        
        print("Enter first name: ")
        first_name: str = input()

        print("Enter last name: ")
        last_name: str = input()

        print("Enter department: ")
        department: str = input()

        print("Enter email: ")
        email: str = input()

        new_professor: Professor = Professor(first_name, last_name, department, email)
        self.terminal.student_service.save(new_professor)

        self.terminal.navigate(MainMenu(self.terminal))