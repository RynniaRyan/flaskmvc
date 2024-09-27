from .student import create_student
from .competition import create_competition
from .participation import create_participation
from App.database import db
from App.models import Student
from App.models import Competition
import csv


def initialize():
    db.drop_all()
    db.create_all()

    with open('results.csv') as file:
        reader = csv.DictReader(file)  # Fixed the typo here

        for row in reader:
            student = create_student(
                first_name=row['First_Name'],
                last_name=row['Last_Name'],
                email=row['Email'],
                degree=row['Degree'],
                university=row['University'],
                year_of_study=int(row['Year_of_Study'])
            )

            competition = create_competition(
                name=row['Competition Name'],
                location=row['Location'],
                date=row['Date'],
                organizer=row['Organizer']
            )

            create_participation(
                student_id=student.id,  
                competition_id=competition.id, 
                rank=int(row['Rank']),
                score=int(row['Score']),
                #time_taken=int(row['Time Taken'].split()[0])  # Add time taken if required
            )
            
    bob = create_student(
            firstname="Bob",
            lastname="Smith",
            email="bob.smith@example.com",
            degree="Computer Science",
            university="University of Technology",
            year_of_study="3rd Year",
            password="bobpass")
    return bob