from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db=SQLAlchemy()

class Document(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    filename=db.Column(db.String(100) )
    created_at = db.Column(db.DateTime, default=datetime.now)
    operation=db.Column(db.JSON)

    def __init__(self,filename,request_time,operation):
        self.filename=filename
        self.operation=operation


