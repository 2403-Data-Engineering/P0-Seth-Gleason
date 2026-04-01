from menu import Menu

class MainMenu(Menu):
    def render(self) -> None:
        print("""
-=-=-=-=-=-=-=-=-=-=-=-
Please choose one of the following options
1) Add new student
2) Add new professor    
3) Add new class
4) Enroll student in class
5) Run Report                         
Q) Quit
        """)
        user_input = input().lower()
        match user_input:
            case "1":
                #self.terminal.navigate(NewStudentMenu(self.terminal))
                pass
            case "2":
                #self.terminal.navigate(NewProfessorMenu(self.terminal))
                pass
            case "3":
                #self.terminal.navigate(NewClassMenu(self.terminal))
                pass
            case "4":
                #self.terminal.navigate(EnrollmentMenu(self.terminal))
                pass
            case "5":
                print("TO DO")
            case 'q':
                self.terminal.quit()