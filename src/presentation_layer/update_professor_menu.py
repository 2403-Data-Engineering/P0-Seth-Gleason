from presentation_layer.menu import Menu, Validator

class UpdateProfessorMenu(Menu):

    def render(self):
        print("""
-=-=-=-=-=-=-=-=-=-
Update Professor Menu
-=-=-=-=-=-=-=-=-=-
1) Update first name
2) Update last name
3) Update department
4) Update email
5) Delete professor                    
              """)
        user_input = input().lower()

        match user_input:
            case '1':
                id: int = int(self.get_input("Enter professor id number: ",Validator.ID))
                new_first_name: str = self.get_input("Enter new first name: ", Validator.NAME)
                self.terminal.professor_service.update_first_name(new_first_name,id)

            case '2':
                id: int = int(self.get_input("Enter professor id number: ",Validator.ID))
                new_last_name: str = self.get_input("Enter new last name: ", Validator.NAME)
                self.terminal.professor_service.update_last_name(new_last_name, id)

            case '3':
                id: int = int(self.get_input("Enter professor id number: ",Validator.ID))
                new_department: str = self.get_input("Enter new department: ")
                self.terminal.professor_service.update_department(new_department,id)

            case '4':
                id: int = int(self.get_input("Enter professor id number: ",Validator.ID))
                new_email = self.get_input("Enter new email: ", Validator.EMAIL)
                self.terminal.professor_service.update_email(new_email, id)

            case '5':
                id: int = int(self.get_input("Enter professor id number: ",Validator.ID))
                self.terminal.professor_service.remove(id)                

        self.terminal.navigate('main_menu')