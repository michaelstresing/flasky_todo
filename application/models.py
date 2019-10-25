from . import db
from sqlalchemy import Column, Integer, String, DateTime, Date
from sqlalchemy.sql import func


class Todo(db.Model):
    """Data model for Todos"""

    __tablename__ = 'todos'

    id = Column(Integer,
                   primary_key=True)

    taskname = Column(String(64))

    taskdifficulty = Column(Integer)

    time_created = Column(DateTime(timezone=True),
                             server_default=func.now())
                             
    duedate = Column(Date)

    @staticmethod
    def from_dict(dict):

        return Todo(
            taskname=dict['taskname'],
            taskdifficulty=dict['taskdifficulty'],
            duedate=dict['duedate']
            )

    def to_dict(self):
       """Return object data in easily serializable format"""
       return {
           'id'  : self.id,
           'taskname': self.taskname,
           'taskdifficulty': self.taskdifficulty,
           'time_created': self.time_created,
           'duedate':self.duedate
       }