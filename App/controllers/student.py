from App.models import Student
from App.database import db


def create_student(firstname, lastname, email, degree, university, year_of_study, password):
    newstudent = Student(firstname=firstname, lastname=lastname, email=email, degree=degree, university=university, year_of_study=year_of_study, password=password)
    db.session.add(newstudent)
    db.session.commit()
    return newstudent

def get_user_by_name(firstname, lastname):
    return Student.query.filter_by(firstname=firstname, lastname=lastname).first()

def get_all_students():
    return Student.query.all()