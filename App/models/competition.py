from App.database import db

class Competition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    location = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    organizer = db.Column(db.String,nullable=False)
    # Relationship with Participation to access students
    participations = db.relationship('Participation', backref='competition', lazy=True)
    

    def __init__(self, name, date, location, organizer):
        self.name = name
        self.location = location
        self.date = date
        self.organizer = organizer        
    
    def __repr__(self):
      return (f"<{self.name} | "
              f"{self.formatted_organizers()} | "
              f"{self.location} | "
              f"{self.date}>")
    
    def get_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'date': self.date,
            'organizer': self.organizer
        }
    
    def formatted_organizers(self):
        return ', '.join(organizer.strip() for organizer in self.organizer.split(','))