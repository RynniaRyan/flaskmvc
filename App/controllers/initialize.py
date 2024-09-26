from .student import create_student
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    bob = create_student(
            firstname="Bob",
            lastname="Smith",
            email="bob.smith@example.com",
            degree="Computer Science",
            university="University of Technology",
            year_of_study="3rd year",
            password="bobpass")
    return bob   
    
