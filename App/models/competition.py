from App.database import db

class Competition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    organizer = db.Column(db.String,nullable=False)
    # Relationship with Participation to access students
    participations = db.relationship('Participation', backref='competition', lazy=True)
    

    def __init__(self, name, date, location, organizer):
        self.name = name
        self.location = location
        self.date = date
        self.organizers = organizer        
    
    def __repr__(self):
      return (f"<Competition: {self.name} | "
              f"Organizers: {self.formatted_organizers()} | "
              f"Date: {self.formatted_date()}>")
    
    def formatted_date(self):
        # Only shows date format (YYYY/MM/DD)
        return self.date.strftime("%Y/%m/%d")
    
    def formatted_organizers(self):
        # Split the organizers string and format it
        return ', '.join(organizer.strip() for organizer in self.organizers.split(','))  # List of organizers