from app import db

# video class/model
class video_url(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    video_url = db.Column(db.String(200), unique=True, nullable=False)

    def __init__(self, video_url):
        self.video_url = video_url



