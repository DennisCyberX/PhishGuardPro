from app import db

class AnalysisLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_input = db.Column(db.String(500), nullable=False)
    is_phishing = db.Column(db.Boolean, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
