from presentation_layer.menu import Menu, Validator

class StudentInfoMenu(Menu):
    def render(self):
        print("""
-=-=-=-=-=-=-=-=-
Student Info Menu
-=-=-=-=-=-=-=-=-
1) View all students
2) View student         
        """)
        
        user_input = input()
        
        match user_input:

            case '1':
                print(self.terminal.student_service.get_all_students())

            case '2':
                id: int = int(self.get_input("Enter student id: ", Validator.ID))
                print(self.terminal.student_service.get_by_id(id))
        
        self.terminal.navigate('main_menu')
        