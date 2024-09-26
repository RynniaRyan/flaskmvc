from App.models import Competition
from App.database import db


def create_competition(name, date, location, organizer):
    newcompetition = Competition(name=name, date=date, location=location, organizer=organizer)
    return newcompetition

def get_all_competitions():
    return Competition.query.all()