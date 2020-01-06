from sqlalchemy import Integer, String, Column
from database import Base

class Add(Base):
    __tablename__ = "add"

    id = Column(Integer, primary_key=True, index=True)
    val1 = Column(Integer)
    val2 = Column(Integer)
    sum = Column(Integer)

    

















