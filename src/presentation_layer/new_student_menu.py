from presentation_layer.menu import Menu, Validator
# from main_menu import MainMenu
from Models.student import Student

class NewStudentMenu(Menu):
    def render(self) -> None:
        print("""
-=-=-=-=-=-=-=-=-=-
New Student Menu
-=-=-=-=-=-=-=-=-=- 
              """)
        
        first_name: str = self.get_input("Enter first name: ",Validator.NAME)

        last_name: str = self.get_input("Enter last name: ",Validator.NAME)

        print("Enter major: ")
        major: str = input()

        email: str = self.get_input("Enter email: ",Validator.EMAIL)

        year: str = self.get_input("Enter year: ",Validator.YEAR)

        new_student: Student = Student(None, first_name, last_name, major, email, year)
        print(self.terminal.student_service.save(new_student))

        self.terminal.navigate('main_menu')