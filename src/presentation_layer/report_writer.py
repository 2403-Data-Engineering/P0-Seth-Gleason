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


    def course_table(self, course_id: int, mdFile: MdUtils):
        
        headers = ['ID','First Name', 'Last Name', 'Major', 'Year', 'Email']
        student_dict = self.class_service.get_students_in_course(course_id)
        student_id_list = []
        for d in student_dict:
            student_id_list.append(d.get('student_id'))
        rows = []
        for id in student_id_list:
            student = self.student_service.get_by_id(id)
            rows.append([student.get('id'),student.get('first_name'),student.get('last_name'),student.get('major'),student.get('year'),student.get('email')])

        
        table_data = headers

        for row in rows:
            table_data.extend(row)
        mdFile.new_table(columns=6, rows= len(rows)+1, text=table_data)

    def course_report(self, course_id: int):
        
        course = self.class_service.get_by_id(course_id)

        course_name = course.get("name")
        professor_name = self.professor_service.get_name(course.get('professor_id'))
        
        mdFile = MdUtils(file_name='course_report', title=course_name)
        mdFile.new_header(level=1, title='=================')

        mdFile.new_header(level=2, title='Professor')
        mdFile.new_paragraph(professor_name)

        mdFile.new_header(level=2, title="Enrolled Students")
        self.course_table(course_id, mdFile)       
        
        mdFile.create_md_file()

    def student_report(self, student_id: int):
        
        # student = self.student_service.get_by_id(student_id)
        headers = ['ID','Course Name', 'Professor']

        course_dict = self.student_service.get_courses(student_id)

        course_id_list = []
        for d in course_dict:
            course_id_list.append(d.get('course_id'))
        
        rows = []
        for id in course_id_list:
            course = self.class_service.get_by_id(id)
            rows.append([course.get('id'),course.get('name'),self.professor_service.get_name(course.get('professor_id'))])
        
        name = self.student_service.get_name(student_id)
        mdFile = MdUtils(file_name='student_report', title=name)
        table_data = headers

        for row in rows:
            table_data.extend(row)

        mdFile.new_header(level=1, title='=================')
        mdFile.new_header(level=2, title='Courses')
        mdFile.new_table(columns=3, rows=len(rows)+1, text=table_data)
        mdFile.create_md_file()

    def professor_report(self, professor_id: int):
        course_dict = self.class_service.get_professors_courses(professor_id)
        course_id_list = []
        for d in course_dict:
            course_id_list.append(d.get('id'))

        mdFile = MdUtils(file_name='professor_report', title=self.professor_service.get_name(professor_id))

        mdFile.new_header(level=1, title='=================')
        mdFile.new_header(level=2,title="Courses")

        for id in course_id_list:
            
            name = self.class_service.get_by_id(id).get('name')

            mdFile.new_header(level=2, title = name)
            self.course_table(id, mdFile)

        mdFile.create_md_file()