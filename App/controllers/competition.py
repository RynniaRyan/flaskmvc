from App.models import Competition
from App.models import Participation
from App.database import db


def create_competition(name, date, location, organizer):
    newcompetition = Competition(name=name, date=date, location=location, organizer=organizer)
    db.session.add(newcompetition)
    db.session.commit()
    return newcompetition

def get_all_competitions():
    return Competition.query.all()

def get_json(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'degree': self.degree
        }

def get_all_competitions_json():
    competitions = Competition.query.all()
    if not competitions:
        return []
    competitions = [competition.get_json() for competition in competitions]
    return competitions

def delete_participations_by_id(competition_id):
    # Fetch all participations for the competition
    participations = Participation.query.filter_by(competition_id=competition_id).all()

    for participation in participations:
        db.session.delete(participation)

    db.session.commit()