from presentation_layer.menu import Menu, Validator
from presentation_layer.report_writer import ReportWriter

class ReportMenu(Menu):

    def render(self):
        report_writer = ReportWriter(self.terminal.student_service, self.terminal.class_service, self.terminal.professor_service)
        print("""
-=-=-=-=-=-=-              
Report Menu              
-=-=-=-=-=-=-
1) Course Enrollment Report
2) Student Enrollment Report
3) Professor Report              
              """)
        user_input = input()

        match user_input:

            case '1':
                id: int = int(self.get_input("Enter Course id: ", Validator.ID))
                report_writer.course_report(id)

            case '2':
                id: int = int(self.get_input("Enter Student id: ", Validator.ID))
                report_writer.course_report(id)

            case '3':
                id: int = int(self.get_input("Enter Professor id: ", Validator.ID))
                report_writer.course_report(id)

        self.terminal.navigate('main_menu')