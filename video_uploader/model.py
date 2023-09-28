from video_uploader import db
# video class/model
class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    video_url = db.Column(db.string(200), unique=True, nullable=False)


