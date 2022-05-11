"""This module contains user models."""
import os
import platform
import secrets
import numpy as np

from flask_login import UserMixin
from sqlalchemy import func
from werkzeug.datastructures import FileStorage

from helpers.img import center_crop
from modules.core.app import login_manager, app
from modules.core.db import db
from modules.games.models.games import game_participants_table
from PIL import Image


@login_manager.user_loader
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
        if not self.image_file_path or self.image_file_path == 'default.jpg':
            return
        picture_path = os.path.join(app.root_path, 'static/profile_pics', self.image_file_path)
        os.remove(picture_path)

    def set_user_picture(self, picture: FileStorage):
        random_hex = secrets.token_hex(16)
        _, f_ext = os.path.splitext(picture.filename)
        picture_fn = random_hex + f_ext
        picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
        picture_path_tmp = picture_path + "-tmp"
        picture.save(picture_path_tmp)
        image = Image.open(picture_path_tmp)
        Image.fromarray(center_crop(np.array(image))).save(picture_path)
        os.remove(picture_path_tmp)
        self.image_file_path = picture_fn

    def get_win_rate(self):
        if self.losses == 0:
            return "100%" if self.wins > 0 else "0%"

        return f"{self.wins / self.losses * 100}%"

    def __eq__(self, other):
        """Check equality."""
        return self.id == other.id
