#!/usr/bin/env python3

from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    company_name = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    jobs = db.relationship('JobListing', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class JobListing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    description = db.Column(db.Text)
    location = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

class JobApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job_listing.id'))
    applicant_name = db.Column(db.String(64))
    applicant_email = db.Column(db.String(120))
    resume = db.Column(db.LargeBinary)
    cover_letter = db.Column(db.Text)
    date_applied = db.Column(db.DateTime, default=datetime.utcnow)
