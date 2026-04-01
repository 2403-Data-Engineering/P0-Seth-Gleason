from menu import Menu
from main_menu import MainMenu
from Models.student import Student

class NewStudentMenu(Menu):
    def render(self) -> None:
        print("""
-=-=-=-=-=-=-=-=-=-
New Student Menu
-=-=-=-=-=-=-=-=-=- 
              """)
        
        print("Enter first name: ")
        first_name: str = input()

        print("Enter last name: ")
        last_name: str = input()

        print("Enter major: ")
        major: str = input()

        print("Enter email: ")
        email: str = input()

        print("Enter year: ")
        year: str = input()

        new_student: Student = Student(first_name, last_name, major, email, year)
        self.terminal.student_service.save(new_student)

        self.terminal.navigate(MainMenu(self.terminal))