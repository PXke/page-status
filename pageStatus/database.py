# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database

engine = create_engine('postgresql+psycopg2://docker:docker@db/pagestatusdb')
if not database_exists(engine.url):
    create_database(engine.url)

# Creation of a session of the psql database
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    """
    Import all modules here that might define models so that they will be registered properly on the metadata.
    """
    import pageStatus.Monitoring.models
    Base.metadata.create_all(bind=engine)

def drop_db():
    Base.metadata.drop_all(bind=engine)

