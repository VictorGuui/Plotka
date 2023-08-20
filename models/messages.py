#from db import db
#from datetime import datetime


#class Message(db.Model):
#    __tablename__='messages'
#
#   id = db.Column(db.Integer, primary_key=True)
#    content = db.Column(db.String, nullable=False)
#    role = db.Column(db.String, nullable=False)
#    datetime = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)  # Use datetime.utcnow diretamente
#
#    def __init__(self, content, role):
#        self.content = content
#        self.role = role