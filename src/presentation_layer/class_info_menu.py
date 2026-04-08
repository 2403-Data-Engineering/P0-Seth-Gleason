from presentation_layer.menu import Menu, Validator

class ClassInfoMenu(Menu):
    def render(self):
        print("""
-=-=-=-=-=-=-=-=-
Class Info Menu
-=-=-=-=-=-=-=-=-
1) View all courses
2) View Course
3) View students in course        
        """)
        
        user_input = input()
        
        match user_input:

            case '1':
                print(self.terminal.class_service.get_all_classs())

            case '2':
                id: int = int(self.get_input("Enter course id: ", Validator.ID))
                print(self.terminal.class_service.get_by_id(id))

            case '3':
                id: int = int(self.get_input("Enter course id: ", Validator.ID))
                print(self.terminal.class_service.get_students_in_course(id))


        self.terminal.navigate('main_menu')
        