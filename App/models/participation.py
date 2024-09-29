from App.database import db
from App.models import Student #Allows us to access Student model
from App.models import Competition

class Participation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    competition_id = db.Column(db.Integer, db.ForeignKey('competition.id'), nullable=False)
    rank = db.Column(db.String(10), nullable=True)
    score = db.Column(db.Float, nullable=True)
    

    def __init__(self, student_id, competition_id, rank, score):
        self.student_id = student_id
        self.competition_id = competition_id
        self.rank = rank
        self.score = score
    
    def __repr__(self):
        student = Student.query.get(self.student_id)
        return (f"< {student.firstname} {student.lastname} | "
                f"Rank: {self.rank} | "
                f"Score: {self.score}>")