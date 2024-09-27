from App.models import Student
from App.database import db


def create_student(id, firstname, lastname, email, degree):
    newstudent = Student(id=id, firstname=firstname, lastname=lastname, email=email, degree=degree)
    db.session.add(newstudent)
    db.session.commit()
    return newstudent

def get_user_by_name(firstname, lastname):
    return Student.query.filter_by(firstname=firstname, lastname=lastname).first()

def get_all_students():
    return Student.query.all()