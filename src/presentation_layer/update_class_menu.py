from presentation_layer.menu import Menu, Validator

class UpdateClassMenu(Menu):

    def render(self):
        print("""
-=-=-=-=-=-=-=-=-=-
Update Class Menu
-=-=-=-=-=-=-=-=-=-
1) Change professor
2) Change name
3) Delete       
              """)
        user_input = input().lower()

        match user_input:

            case '1':
                course_id: int = int(self.get_input("Enter course id: ", Validator.ID))
                professor_id: int = int(self.get_input("Enter new professor's id: ", Validator.ID))
                self.terminal.class_service.assign_professor(course_id, professor_id)

            case '2':
                course_id: int = int(self.get_input("Enter course id: ", Validator.ID))
                new_name: str = self.get_input("Enter new course name: ")
                self.terminal.class_service.update_name(course_id, new_name)

            case '3':
                course_id: int = int(self.get_input("Enter course id: ", Validator.ID))
                self.terminal.class_service.remove(course_id)
        
        self.terminal.navigate('main_menu')