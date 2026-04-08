from Models.professor import Professor
import data_layer.professor_dao as professor_dao

class ProfessorService:

    def save(self, professor: Professor) -> Professor:
        return professor_dao.save(professor)

    def get_by_id(self, id: int) -> Professor:
        return professor_dao.get_professor_by_id(id)
    
    def remove(self, id: int):
        professor_dao.remove(id)

    def get_all_professors(self):
        return professor_dao.get_all_professors()
    
    def update_email(self, new_email: str, id: int):
        professor_dao.update_email(new_email, id)

    def update_first_name(self, new_first_name: str, id: int):
        professor_dao.update_first_name(new_first_name, id)

    def update_last_name(self, new_last_name: str, id: int):
        professor_dao.update_last_name(new_last_name, id)

    def update_department(self, department: str, id: int):
        professor_dao.update_department(department, id)

    def get_name(self, id: int):
        first_name = professor_dao.get_professor_by_id(id).get('first_name')
        last_name = professor_dao.get_professor_by_id(id).get('last_name')

        return last_name +", "+ first_name