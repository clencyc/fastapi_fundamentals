from sqlalchemy import column, create_engine, String, integer, Datetime, Date

from sqlalchemy.org import sessionmaker, declarative_base

Base = declarative_base()

class Student(Base):
    id = column(Integer, primary_key=True)
    first_name = column(String)
    last_name = column(String)
    email = column(String)
    deb = column(Datetime)
    
    
    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine)
    sessionmaker = sessionmaker(bind=engine)