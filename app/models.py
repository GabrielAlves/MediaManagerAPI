from datetime import datetime
from . import db

class File(db.Model):
    id = Column(db.Integer, primary_key = True, index = True)
    file_name = Column(db.String(255), nullable = False)
    file_type = Column(db.String(30), nullable = False)
    file_url = Column(db.String(500), nullable = False)
    created_at = Column(db.DateTime, default = datetime.utcnow)