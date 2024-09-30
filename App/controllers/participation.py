from App.models import Participation
from App.database import db


def create_participation(student_id, competition_id, rank, score):
    newparticipation = Participation(student_id=student_id, competition_id=competition_id, rank=rank, score=score)
    db.session.add(newparticipation)
    db.session.commit()
    return newparticipation

def get_results(student_id, competition_id):
    return Participation.query.filter_by(student_id=student_id, competition_id=competition_id).first()

def get_participation_by_student_id(student_id):
    return Participation.query.filter_by(student_id=student_id).all()

def delete_participations_by_id(competiiton_id):
    participations = Participation.query.filter_by(competition_id=competiiton_id).all()

    for participation in participations:
        db.session.delete(participation)

    db.session.commit()