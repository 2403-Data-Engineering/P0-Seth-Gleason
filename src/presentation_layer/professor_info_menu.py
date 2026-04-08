from presentation_layer.menu import Menu, Validator

class ProfessorInfoMenu(Menu):
    def render(self):
        print("""
-=-=-=-=-=-=-=-=-
Professor Info Menu
-=-=-=-=-=-=-=-=-
1) View all professors
2) View professor         
        """)
        
        user_input = input()
        
        match user_input:

            case '1':
                print(self.terminal.professor_service.get_all_professors())

            case '2':
                id: int = int(self.get_input("Enter professor id: ", Validator.ID))
                print(self.terminal.professor_service.get_by_id(id))
        
        self.terminal.navigate('main_menu')
        