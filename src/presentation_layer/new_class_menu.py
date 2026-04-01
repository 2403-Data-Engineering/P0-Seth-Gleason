from menu import Menu
from main_menu import MainMenu
from Models.clas import Class

class NewClassMenu(Menu):
    def render(self) -> Class:
        print("""
-=-=-=-=-=-=-=-=-=-
New Class Menu
-=-=-=-=-=-=-=-=-=-

Enter class name: """)
        name: str = input()

        new_class: Class = Class(name)
        self.terminal.class_service.save(new_class)

        self.terminal.navigate(MainMenu(self.terminal))