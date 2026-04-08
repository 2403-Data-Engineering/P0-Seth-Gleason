from dataclasses import dataclass

@dataclass
class Course:
    id: int
    name: str
    professor_id: int