from db.db import Column, String, Model, Integer, DateTime
from datetime.datetime import now

class Message(Model):
    __table__='messages'

    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    role = Column(String, nullable=False)
    datetime = Column(DateTime(timezone=True), server_default=now())
