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
    #bob = initialize()
    initialize()
    print('Database Intialized')
    #print(bob)



'''
|   User Group Commands
|   These are a list of commands used to perform operations involving student users
'''
student_cli = AppGroup('student', help='Student object commands') 

@student_cli.command("create", help="Creates a new user")
@click.argument('id', default=816067890)
@click.argument('firstname', default='Bob')
@click.argument('lastname', default='Smith')
@click.argument('email', default='bob.smith@uni.edu')
@click.argument('degree', default='Computer Science (Special)')
def add_student(id,firstname, lastname, email, degree):
    newstudent = create_student(id, firstname, lastname, email, degree)
    try:
        db.session.add(newstudent)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        print("Student user already exists!")
    else:
        print(f"Student user {student.firstname} {student.lastname} created!")


@student_cli.command("list", help="Displays all student users")
def view_student_list():
    students = get_all_students()
    if not students:
        print("No student users found.")
    else:
        for student in students:
            print(student)  
            print()


@student_cli.command("view-competitions", help="Displays all competitions participated by student")
@click.argument('firstname', default='Bob')
@click.argument('lastname', default='Smith')
def view_students_showcase(firstname, lastname):
    student = get_user_by_name(firstname, lastname)
    
    if not student:
        print(f"{firstname} {lastname} not found within database.")
        return

    # Use the relationship to access participations directly
    participations = student.participations
    
    if not participations:
        print(f"{student.firstname} {student.lastname} has not participated in any competitions.")
        return
    
    # Printing each competition
    for participation in participations:
        competition = Competition.query.filter_by(id=participation.id).first()
        if competition:
            print(participation)
        else:
            print("Uh oh, something is not right.")

app.cli.add_command(student_cli)



'''
|   User Group Commands
|   These are a list of commands used to perform operations involving student users
'''
competition_cli = AppGroup('competition', help='Competition object commands') 

@competition_cli.command("create",help="Creates a new competition")
@click.argument('name', default="Bob's Code Challenge")
@click.argument('date', default='30/09/2024')
@click.argument('location', default="Bob Centre")
@click.argument('organizer', default="Bob")
def add_competition(name, date, location, organizer):
    
    newcompetition = Competition.query.filter_by(name=name).first()

    if not newcompetition:
        create_competition(name, date, location, organizer)
        print(f"New Competition '{name}' created!")
    else:
        print(f"Competition '{name}' already exists!")
        return


@competition_cli.command("list", help="View competitions list")
def view_competition_list():
    competitions = get_all_competitions()
    if not competitions:
        print("No competitions found.")
    else:
        for competition in competitions:
            print(competition)  
            print()


@competition_cli.command("add-result", help="Import competition results from file.csv")
@click.argument('competition_name', default="Bob's Code Challenge")
def add_competition_results(competition_name):
    competition = Competition.query.filter_by(name=competition_name).first

    if not competition:
        print(f"Competition {competition_name} does not exist")
        return

    with open('results.csv', 'r') as file:
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
                    score=int(row['Score']),
                )


app.cli.add_command(competition_cli)











'''
User Commands
'''
# Commands can be organized using groups

# # create a group, it would be the first argument of the comand
# # eg : flask user <command>
# user_cli = AppGroup('user', help='User object commands') 

# # Then define the command and any parameters and annotate it with the group (@)
# @user_cli.command("create", help="Creates a user")
# @click.argument("username", default="rob")
# @click.argument("password", default="robpass")
# def create_user_command(username, password):
#     create_user(username, password)
#     print(f'{username} created!')

# # this command will be : flask user create bob bobpass
# @user_cli.command("list", help="Lists users in the database")
# @click.argument("format", default="string")
# def list_user_command(format):
#     if format == 'string':
#         print(get_all_users())
#     else:
#         print(get_all_users_json())

# app.cli.add_command(user_cli) # add the group to the cli