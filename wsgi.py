import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup
from sqlalchemy.exc import IntegrityError
from datetime import datetime

from App.database import db, get_migrate
from App.models import * #importing all models
from App.main import create_app
#from App.controllers import ( initialize )
from App.controllers import *

# This commands file allow you to create convenient CLI commands for testing controllers
app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    bob = initialize()
    print('Database Intialized')
    print(bob)



'''
|   User Group Commands
|   These are a list of commands used to perform operations involving student users
'''
student_cli = AppGroup('student', help='Student object commands') 

@student_cli.command("create", help="Creates a new user")
@click.argument('firstname', default='Jhon')
@click.argument('lastname', default='Doe')
@click.argument('email', default='JhonDoe@mail.com')
@click.argument('degree', default='Computer Science (Special)')
@click.argument('university', default='University of Technology')
@click.argument('year_of_study', default='2nd Year')
@click.argument('password', default='jhonpass')
def create_student(firstname, lastname, email, degree, university, year_of_study, password):
    newstudent = create_student(firstname, lastname, email, degree, university, year_of_study, password)
    try:
        db.session.add(newstudent)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        print("Student user already exists!")
    else:
        print(f"Student user created! Welcome {firstname}")


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
        print(f" {student.firstname} {student.lastname} not found within database.")
        return
    
    participations = get_participation_by_student_id(student.id)
    
    if not participations:
        print(f"{student.firstname} {student.lastname} has not participated in any competitions.")
        return
    
    # Print each competition name
    for p in participations:
        competition = Competition.query.filter_by(id=p.competition_id).first()
        if competition:
            print(competition)
        else:
            print(f"Uh oh, something is not right.")

app.cli.add_command(student_cli)



'''
|   User Group Commands
|   These are a list of commands used to perform operations involving student users
'''
competition_cli = AppGroup('competition', help='Competition object commands') 

@competition_cli.command("create",help="Creates a new competition")
@click.argument('name', default='Test')
@click.argument('date', default='2024-01-22')
@click.argument('location', default='Test City')
@click.argument('organizer', default='Test Organizers')
def add_competition(name, date, location, organizer):
    
    newcompetition = create_competition(name, date, location, organizer)
    try:
        db.session.add(newcompetition)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        print("Competition event already exists!")
    else:
        print(f"New Competition created!")


@competition_cli.command("list", help="View competitions list")
def view_competition_list():
    competitions = get_all_competitions()
    if not competitions:
        print("No competitions found.")
    else:
        for competition in competitions:
            print(competition)  
            print()


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