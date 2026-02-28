from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql import func

Base = DeclarativeBase()

class File(Base):
    id = Column(Integer, primary_key = True, index = True)
    file_name = Column(String, nullable = False)
    file_type = Column(String, nullable = False)
    file_url = Column(String, nullable = False)
    created_at = Column(DateTime(timezone = True), server_default = func.now(), index = True)