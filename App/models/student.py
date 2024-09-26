from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname =  db.Column(db.String(20), nullable=False)
    lastname =  db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False, unique=True)
    degree = db.Column(db.String(120), nullable=False)
    university = db.Column(db.String(120), nullable=False)
    year_of_study = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(120), nullable=True)
    # Relationship with Participation to access participated competitions
    participations = db.relationship('Participation', backref='student', lazy=True, cascade="all, delete-orphan")


    def __init__(self, firstname, lastname, email, degree, university, year_of_study, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.degree = degree
        self.university = university
        self.year_of_study = year_of_study
        self.set_password(password)

    def __repr__(self):
        return (f"<Student: {self.firstname} {self.lastname} | "
                f"Email: {self.email} | Degree: {self.degree} | "
                f"University: {self.university} | Year: {self.year_of_study}>")

    def get_json(self):
        return{
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'degree': self.degree,
            'university': self.university
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)