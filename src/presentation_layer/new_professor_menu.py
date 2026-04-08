from presentation_layer.menu import Menu, Validator
# from main_menu import MainMenu
from Models.professor import Professor

class NewProfessorMenu(Menu):
    def render(self) -> None:
        print("""
-=-=-=-=-=-=-=-=-=-
New Professor Menu
-=-=-=-=-=-=-=-=-=- 
              """)
        
        first_name: str = self.get_input("Enter first name: ",Validator.NAME)

        last_name: str = self.get_input("Enter last name: ",Validator.NAME)

        print("Enter department: ")
        department: str = input()

        email: str = self.get_input("Enter email: ",Validator.EMAIL)

        new_professor: Professor = Professor(None, first_name, last_name, department, email)
        professor = self.terminal.professor_service.save(new_professor)
        print(professor)
        self.terminal.navigate('main_menu')