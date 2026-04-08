from presentation_layer.menu import Menu
# from new_class_menu import NewClassMenu
# from new_professor_menu import NewProfessorMenu
# from new_student_menu import NewStudentMenu
class MainMenu(Menu):
    def render(self) -> None:
        print("""
-=-=-=-=-=-=-=-=-=-=-=-
Please choose one of the following options
1) Add new student
2) Add new professor    
3) Add new class
4) Enroll student in class
5) Update student info
6) Update professor info
7) Update class info
8) Student Info
9) Professor info
10) Course info
11) Run Report                         
Q) Quit
        """)
        user_input = input().lower()
        match user_input:

            case "1":
                self.terminal.navigate('new_student_menu')
                
            case "2":
                self.terminal.navigate('new_professor_menu')
                
            case "3":
                self.terminal.navigate('new_class_menu')
                
            case "4":
                self.terminal.navigate('enrollment_menu')
                
            case "5":
                self.terminal.navigate('update_student_menu')

            case '6':
                self.terminal.navigate('update_professor_menu')

            case '7':
                self.terminal.navigate('update_class_menu')

            case '8':
                self.terminal.navigate('student_info_menu')

            case '9':
                self.terminal.navigate('professor_info_menu')

            case '10':
                self.terminal.navigate('class_info_menu')

            case '11':
                self.terminal.navigate('report_menu')
                
            case 'q':
                self.terminal.quit()