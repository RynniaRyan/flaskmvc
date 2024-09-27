from .student import create_student
from .competition import create_competition
from .participation import create_participation
from App.database import db
from App.models import Student
from App.models import Competition
import csv
import os


def initialize():
    db.drop_all()
    db.create_all()

    try:
        with open('database.csv', 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                newstudent = Student.query.filter_by(id=row['Student ID']).first()

                if not newstudent:
                    student = create_student(
                        id=row['Student ID'],
                        firstname=row['First Name'],
                        lastname=row['Last Name'],
                        email=row['Email'],
                        degree=row['Degree']
                    )
                else:
                    student = newstudent

                newcompetition = Competition.query.filter_by(name=row['Competition Name']).first()

                if not newcompetition:
                    competition = create_competition(
                        name=row['Competition Name'],
                        location=row['Location'],
                        date=row['Date'],
                        organizer=row['Organizer']
                    )
                else:
                    competition = newcompetition

                create_participation(
                    student_id=student.id,  
                    competition_id=competition.id, 
                    rank=row['Rank'],
                    score=float(row['Score']),
                )

    except FileNotFoundError:
        cwd = os.getcwd()  # Get the current working directory (cwd)
        files = os.listdir(cwd)  # Get all the files in that directory
        print("Files in %r: %s" % (cwd, files))

    # bob = create_student(
    #         id="816012345"
    #         firstname="Bob",
    #         lastname="Smith",
    #         email="bob.smith@example.com",
    #         degree="Computer Science",

    # return bob