"""This module contains user models."""
import os
import secrets
import numpy as np
from flask_babel import format_percent

from flask_login import UserMixin
from sqlalchemy import func
from werkzeug.datastructures import FileStorage
from PIL import Image

from tennis_finder.helpers.img import center_crop
from tennis_finder.modules.core.app_config import AppConfig
from tennis_finder.modules.games.models.games import game_participants_table


db = AppConfig.db
app = AppConfig.app


@AppConfig.login_manager.user_loader
def load_user(user_id):
    """Load user by user_id."""
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """This is the User class, mapped to users table."""

    __tablename__ = "users"

    id = db.Column(db.INT, primary_key=True)
    image_file_path = db.Column(db.String, nullable=False, default='default.jpg')
    full_name = db.Column(db.VARCHAR(100), nullable=False)
    login = db.Column(db.VARCHAR(50), unique=True, nullable=False)
    password = db.Column(db.VARCHAR(512), nullable=False)
    email = db.Column(db.VARCHAR(100))
    phone = db.Column(db.VARCHAR(12))
    skill = db.Column(db.FLOAT, nullable=False)

    wins = db.Column(db.INT, default=0)
    losses = db.Column(db.INT, default=0)

    games = db.relationship("Game", secondary=game_participants_table, back_populates="players")

    created_at = db.Column(db.TIMESTAMP, server_default=func.now())
    updated_at = db.Column(db.TIMESTAMP, server_default=func.now(), onupdate=func.now())

    def delete_user_picture(self):
        """Delete user picture."""
        if not self.image_file_path or self.image_file_path == 'default.jpg':
            return
        picture_path = os.path.join(app.root_path, 'tennis_finder/static/profile_pics', self.image_file_path)
        os.remove(picture_path)
        self.image_file_path = 'default.jpg'

    def set_user_picture(self, picture: FileStorage):
        """
        Set user picture.

        :param picture: FileStorage object with user picture
        :return: None
        """
        random_hex = secrets.token_hex(16)
        _, f_ext = os.path.splitext(picture.filename)
        picture_fn = random_hex + f_ext
        picture_path = os.path.join(app.root_path, 'tennis_finder/static/profile_pics', picture_fn)
        picture_path_tmp = picture_path + "-tmp"
        picture.save(picture_path_tmp)
        image = Image.open(picture_path_tmp)
        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")
        Image.fromarray(center_crop(np.array(image))).save(picture_path)
        os.remove(picture_path_tmp)
        self.image_file_path = picture_fn

    def get_win_rate(self) -> float:
        """
        Get user win rate.

        :return: float
        """
        if self.wins + self.losses == 0:
            return 0
        return self.wins / (self.wins + self.losses)

    def get_win_rate_str(self) -> str:
        """
        Get user win rate as a string.

        :return: str
        """
        return format_percent(self.get_win_rate())

    def __eq__(self, other: 'User') -> bool:
        """
        Check equality between two users.

        :param other: User object
        :return: true if users are equal else false
        """
        return isinstance(other, User) and self.id == other.id
