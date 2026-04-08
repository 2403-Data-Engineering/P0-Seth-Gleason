from presentation_layer.menu import Menu, Validator

class UpdateStudentMenu(Menu):

    def render(self):
        print("""
-=-=-=-=-=-=-=-=-=-
Update Student Menu
-=-=-=-=-=-=-=-=-=-
1) Update first name
2) Update last name
3) Update major
4) Update email
5) Update year
6) Delete student                    
              """)
        user_input = input().lower()

        match user_input:
            case '1':
                id: int = int(self.get_input("Enter student id number: ",Validator.ID))
                new_first_name: str = self.get_input("Enter new first name: ", Validator.NAME)
                self.terminal.student_service.update_first_name(new_first_name,id)

            case '2':
                id: int = int(self.get_input("Enter student id number: ",Validator.ID))
                new_last_name: str = self.get_input("Enter new last name: ", Validator.NAME)
                self.terminal.student_service.update_last_name(new_last_name, id)

            case '3':
                id: int = int(self.get_input("Enter student id number: ",Validator.ID))
                new_major: str = self.get_input("Enter new major: ")
                self.terminal.student_service.update_major(new_major,id)

            case '4':
                id: int = int(self.get_input("Enter student id number: ",Validator.ID))
                new_email = self.get_input("Enter new email: ", Validator.EMAIL)
                self.terminal.student_service.update_email(new_email, id)

            case '5':
                id: int = int(self.get_input("Enter student id number: ",Validator.ID))
                new_year: str = self.get_input("Enter new year: ", Validator.YEAR)
                self.terminal.student_service.update_year(new_year,id)

            case '6':
                id: int = int(self.get_input("Enter student id number: ",Validator.ID))
                self.terminal.student_service.remove(id)                

        self.terminal.navigate('main_menu')