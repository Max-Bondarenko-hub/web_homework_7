from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql+psycopg2://postgres:pass123@localhost/students")

DBSession = sessionmaker(bind=engine)
session = DBSession()