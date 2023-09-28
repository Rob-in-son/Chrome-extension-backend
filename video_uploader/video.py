from chrome_extension import db
# video class/model
class Video(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    video_url = db.Column(db.string(200), unique=True, nullable=False)

    def __init__(self, video_url):
        self.video_url = video_url



