from sqlalchemy import Column, Integer, String
from pageStatus.database import Base


"""
Contains table's models of the web monitoring part.
"""

class MonitoredWebSite(Base):
    __tablename__ = 'MonitoredWebSite'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=False)
    url = Column(String(255), unique=False)

    def __init__(self, name=None, url=None):
        self.name = name
        self.url = url

    def __repr__(self):
        return '<MonitoredWebSite %r>' % (self.name)

