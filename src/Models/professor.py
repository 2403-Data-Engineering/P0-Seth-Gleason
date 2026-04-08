from dataclasses import dataclass

@dataclass
class Professor:
    id: int
    first_name: str
    last_name: str
    department: str
    email: str
    