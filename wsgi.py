import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup
from sqlalchemy.exc import IntegrityError
from datetime import datetime

from App.database import db, get_migrate
from App.main import create_app
#from App.controllers import ( initialize )
from App.controllers import *
from App.models import Student
from App.models import Competition

# This commands file allow you to create convenient CLI commands for testing controllers
app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('\n Database Intialized! \n')

""" This is a helper function to allow a deafult value for user input """
def get_input(prompt, default):
    response = input(f"{prompt} (default: '{default}'): ").strip()
    return response if response else default  # Return response or default if blank


'''
|   User Group Commands
|   These are a list of commands used to perform operations involving student users
'''
student_cli = AppGroup('student', help='Student object commands')

@student_cli.command("list", help="Displays all student users")
def view_student_list():
    students = get_all_students()
    if not students:
        print("\n No student users found. \n")
    else:
        print()
        for student in students:
            print(student)  
        print()


@student_cli.command("view-participation", help="Displays all students who participated in a particular competition")
def view_students_showcase():

    firstname = get_input("\n Enter student's first name", "Bob")
    lastname = get_input("\n Enter student's last name", "Smith")

    student = get_user_by_name(firstname, lastname)
    
    if not student:
        print(f"\n '{firstname} {lastname}' not found within the database \n")
        return

    participations = student.participations
    
    if not participations:
        print(f"\n {student.firstname} {student.lastname} has not participated in any competitions.\n")
        return
    
    print()
    for participation in participations:
        
        competition = Competition.query.filter_by(id=participation.competition_id).first()
        
        print(f"<Competition: {competition.name} | Location: {competition.location} | Date: {competition.date} | "
                f"Rank: {participation.rank} | Score: {participation.score}> ")
    print()

app.cli.add_command(student_cli)



'''
|   Competitions Group Commands
|   These are a list of commands used to perform operations involving existing competitions
'''
competition_cli = AppGroup('competition', help='Competition object commands') 

@competition_cli.command("create",help="Creates a new competition")
def add_competition():

    name = get_input("\n Enter competition name", "Bob's Code Challenge")
    date = get_input("\n Enter competition date (MM/DD/YYYY", "09/30/2024")
    location = get_input("\n Enter competition location ", "Bob Centre")
    organizer = get_input("\n Enter organizer name ", "Bob")

    newcompetition = Competition.query.filter_by(name=name).first()

    if not newcompetition:
        create_competition(name, date, location, organizer)
        print(f"\n New Competition '{name}' created! \n")
    else:
        print(f"\n Competition '{name}' already exists! \n")
        return


@competition_cli.command("list", help="View competitions list")
def view_competition_list():

    competitions = get_all_competitions()

    if not competitions:
        print("\n No competitions found. \n")
    else:
        print()
        for competition in competitions:
            print(competition)  
        print()


@competition_cli.command("add-result", help="Import competition results given a csv file")
def add_competition_results():

    competition_name = input("\n Enter competition name: ").strip()

    import_file = get_input("\n Enter file directory path", "results.csv")

    competition = Competition.query.filter_by(name=competition_name).first()

    if not competition:
        print(f"\n Competition '{competition_name}' does not exist! \n")
        return
    
    results_existing = Participation.query.filter_by(competition_id=competition.id).all()

    if results_existing:
        update_response = input(f"\n Results for competition '{competition_name}' already exist. Would you like to update them? (yes/no): ").strip().lower()
        
        if update_response == 'yes':
            delete_participations_by_id(competition.id)
            print(f"\n Previous results for '{competition_name}' have been deleted successfully! \n")
        else:
            print("\n No changes made. \n")
            return

    try:
        with open(import_file, 'r') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    newstudent = Student.query.filter_by(id=row['Student ID']).first()

                    if not newstudent:
                        student = create_student(
                            id=row['Student ID'],
                            firstname=row['First Name'],
                            lastname=row['Last Name'],
                            email=row['Email'],
                            degree=row['Rank']
                        )
                    else:
                        student = newstudent

                    create_participation(
                        student_id=student.id,  
                        competition_id=competition.id, 
                        rank=row['Rank'],
                        score=float(row['Score']),
                    )
        
        print(f" Results added to competition '{competition_name}' \n")

    except FileNotFoundError:
        cwd = os.getcwd()
        files = os.listdir(cwd)
        print("\n File 'results.txt' not found within directory %r: %s" % (cwd, files))
        print()


@competition_cli.command("view-result", help="Displays the results of a given competition")
def view_compeititon_results():

    competition_name = input("\n Enter competition name: ").strip()

    competition = Competition.query.filter_by(name=competition_name).first()

    if not competition:
        print(f"\n Competition '{competition_name}' does not exsist \n")
        return
    else:

        if not competition.participations:
            print(f"\n There are no results imported yet for '{competition_name}' \n")
        else:
            print()
            for participation in competition.participations:
                    print(participation)
            print()
                
app.cli.add_command(competition_cli)