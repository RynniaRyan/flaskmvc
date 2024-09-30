from App.models import Competition
from App.models import Participation
from App.models import Student
from App.controllers import (create_participation, create_student)
import csv
from App.database import db


def create_competition(name, date, location, organizer):
    newcompetition = Competition(name=name, date=date, location=location, organizer=organizer)
    db.session.add(newcompetition)
    db.session.commit()
    return newcompetition

def get_all_competitions():
    return Competition.query.all()

def get_all_competitions_json():
    competitions = Competition.query.all()
    if not competitions:
        return []
    competitions = [competition.get_json() for competition in competitions]
    return competitions

def add_results_from_csv(competition, csv_file):
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                student = Student.query.filter_by(id=row['Student ID']).first()

                if not student:
                    student = create_student(
                        id=row['Student ID'],
                        firstname=row['First Name'],
                        lastname=row['Last Name'],
                        email=row['Email'],
                        degree=row['Degree']
                    )

                create_participation(
                    student_id=student.id,  
                    competition_id=competition.id,  # Access the competition ID from the instance
                    rank=row['Rank'],
                    score=float(row['Score']),
                )
        print(f"\n Results added to competition '{competition.name}' successfully.\n")

    except FileNotFoundError:
        print(f"\n File '{csv_file}' not found.\n")