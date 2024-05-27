#!/usr/bin/env python3

from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from app import db
from app.forms import LoginForm, RegistrationForm, JobForm, ApplicationForm
from app.models import User, JobListing
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/')
def index():
    jobs = JobListing.query.all()
    return render_template('index.html', jobs=jobs)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, company_name=form.company_name.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/post-job', methods=['GET', 'POST'])
@login_required
def post_job():
    form = JobForm()
    if form.validate_on_submit():
        job = JobListing(title=form.title.data, description=form.description.data,
                         location=form.location.data, user_id=current_user.id)
        db.session.add(job)
        db.session.commit()
        flash('Your job has been posted.')
        return redirect(url_for('index'))
    return render_template('post_job.html', form=form)

@app.route('/job/<int:job_id>')
def job_details(job_id):
    job = JobListing.query.get_or_404(job_id)
    return render_template('job_details.html', job=job)

@app.route('/apply-job/<int:job_id>', methods=['GET', 'POST'])
def apply_job(job_id):
    form = ApplicationForm()
    job = JobListing.query.get_or_404(job_id)
    if form.validate_on_submit():
        application = JobApplication(job_id=job.id, applicant_name=form.applicant_name.data,
                                     applicant_email=form.applicant_email.data,
                                     resume=form.resume.data, cover_letter=form.cover_letter.data)
        db.session.add(application)
        db.session.commit()
        flash('Your application has been submitted.')
        return redirect(url_for('index'))
    return render_template('apply_job.html', form=form, job=job)
