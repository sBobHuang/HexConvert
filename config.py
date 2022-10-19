#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import os
import sqlite3
from datetime import datetime

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # CURRENT_TERM = '20下'
    BASE_DIR = basedir
    SECRET_KEY = "BobHuang"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASK_MAIL_SUBJECT_PREFIX = '[Flask]'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN = None
    FLASK_POSTS_PER_PAGE = 10

    @staticmethod
    def init_app(app):
        pass


config = {
    'default': Config,
}
