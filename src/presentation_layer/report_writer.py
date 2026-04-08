from mdutils.mdutils import MdUtils
from mdutils.tools.Table import Table
# from presentation_layer.terminal import Terminal
from service_layer.class_service import ClassService
from service_layer.student_service import StudentService
from service_layer.professor_service import ProfessorService

class ReportWriter:

    def __init__(self, student_service: StudentService, class_service: ClassService, professor_service: ProfessorService):
        self.student_service = student_service
        self.class_service = class_service
        self.professor_service = professor_service


    def course_report(self, course_id: int):

        course = self.class_service.get_by_id(course_id)

        headers = ['ID','First Name', 'Last Name', 'Major', 'Year', 'Email']
        student_dict = self.class_service.get_students_in_course(course_id)
        student_id_list = []
        for d in student_dict:
            student_id_list.append(d.get('student_id'))
        rows = []
        for id in student_id_list:
            student = self.student_service.get_by_id(id)
            rows.append([student.get('id'),student.get('first_name'),student.get('last_name'),student.get('major'),student.get('year'),student.get('email')])

        course_name = course.get("name")
        professor_name = self.professor_service.get_name(course.get('professor_id'))
        mdFile = MdUtils(file_name='course_report', title='Enrollments in '+ course_name)
        mdFile.new_paragraph('Professor: '+ professor_name)

        table_data = headers

        for row in rows:
            table_data.extend(row)
        
        mdFile.new_table(columns=6,rows = len(rows)+1,text=table_data)
        mdFile.create_md_file()

    def student_report(self, student_id: int):
        
        student = self.student_service.get_by_id(student_id)
        headers = ['ID','Course Name', 'Professor']

        course_dict = self.student_service.get_

