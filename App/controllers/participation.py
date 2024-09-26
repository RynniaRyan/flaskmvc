from App.models import Participation
from App.database import db


def create_participation(student_id, competition_id, results=None):
    newparticipation = Participation(student_id=student_id, competition_id=competition_id, results=results)
    db.session.add(newparticipation)
    db.session.commit()
    return newparticipation

def get_results(student_id, competition_id):
    return Participation.query.filter_by(student_id=student_id, competition_id=competition_id).first()
