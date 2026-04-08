from presentation_layer.menu import Menu, Validator
# from main_menu import MainMenu
from Models.course import Course

class NewClassMenu(Menu):
    def render(self) -> Course:
        print("""
-=-=-=-=-=-=-=-=-=-
New Class Menu
-=-=-=-=-=-=-=-=-=-

Enter class name: """)
        name: str = input()
        
        professor_id = self.get_input("Enter professor id: ", Validator.ID)

        new_class: Course = Course(None, name, professor_id)
        course = self.terminal.class_service.save(new_class)
        print(course)
        self.terminal.navigate('main_menu')