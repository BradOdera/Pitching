from . import login_manager
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    pass_secure = db.Column(db.String(255))
