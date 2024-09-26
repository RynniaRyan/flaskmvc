from App.database import db
from App.models import Student #Allows us to access Student model

class Participation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    competition_id = db.Column(db.Integer, db.ForeignKey('competition.id'), nullable=False)
    results = db.Column(db.String(100), nullable=True)

    def __init__(self, student_id, competition_id, results=None):
        self.student_id = student_id
        self.competition_id = competition_id
        self.results = results
    
    def __repr__(self):
        student = Student.query.get(self.student_id)
        return (f"<Participation: {student.firstname} {student.lastname} | "
                f"Results: {self.results}>")
