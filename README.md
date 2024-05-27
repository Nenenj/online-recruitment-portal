## Online Recruitment Portal
##Project Overview
The Online Recruitment Portal MVP aims to provide a platform where job seekers can browse and apply for jobs, and recruiters can post job listings. This MVP will be simple yet functional, focusing on core features to deliver a user-friendly experience.
## Key Features
Job Listings: View and search job listings without needing an account.
Job Details: Detailed view of job information.
User Registration: Recruiters can create accounts.
Job Posting: Recruiters can post job listings.
Application Submission: Job seekers can apply for jobs.

## Technologies Used
Frontend: HTML, CSS, JavaScript
Backend: Python (Flask)
Database: SQLite
User Authentication: Flask-Login for session management

##Project Structure
online-recruitment-portal/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── job_details.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── post_job.html
│   │   └── apply_job.html
│   ├── static/
│   │   ├── css/
│   │   └── js/
├── instance/
│   ├── config.py
├── migrations/
├── venv/
├── .gitignore
├── README.md
├── config.py
├── requirements.txt
└── run.py

## Installation and Setup
1. Clone the Repository
git clone https://github.com/nenenj/online-recruitment-portal.git
cd online-recruitment-portal

2. Set Up Virtual Environment
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install Dependencies
pip install -r requirements.txt
4. Set Up Database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
5. Run the Application
flask run

##Project Components
# Frontend
HTML: Structure of the web pages.
CSS: Styling for the web pages.
JavaScript: Client-side scripting for interactivity.
# Backend
Flask: Micro web framework for Python.
SQLite: Lightweight database for development purposes.
Flask-Login: User session management.
# Database Models
User: Stores user information (recruiters).
JobListing: Stores job listings.
JobApplication: Stores job applications submitted by job seekers.
# Routes and Views
Homepage (/): Displays job listings.
Job Details (/job/<id>): Displays details of a specific job.
Register (/register): User registration for recruiters.
Login (/login): User login.
Post Job (/post-job): Form for recruiters to post jobs.
Apply Job (/apply-job/<id>): Form for job seekers to apply for jobs.

## User Stories
# User Registration
As a recruiter, I want to register for an account so that I can post job listings.

# Acceptance Criteria:
Provide company name, email, and password during registration.
Receive a confirmation email upon successful registration.
Log in using the registered email and password.

# Job Posting
As a registered recruiter, I want to post job listings to attract potential candidates.

# Acceptance Criteria:
Fill out a form with job title, description, location, and application details.
View the posted job listing on the platform.
Edit or delete my job listings.

# Job Application
As a job seeker, I want to apply for jobs listed on the platform.

# Acceptance Criteria:
Fill out an application form with required details.
Upload a resume and cover letter.
Receive a confirmation email upon successful application submission.

## Development Plan
Setup: Initialize the project structure and environment.
Frontend Development: Create basic HTML templates and CSS for styling.
Backend Development: Implement Flask routes, models, and forms.
User Authentication: Integrate Flask-Login for user sessions.
CRUD Operations: Implement job posting, viewing, editing, and deleting features.
Job Application: Implement application submission and recruiter view for applications.
Testing: Perform manual testing of core functionalities.
Deployment: Deploy the application on a basic hosting solution like Heroku or AWS.

## Contribution Guide
Fork the Repository: Create a fork of the repository on GitHub.
Create a Branch: Create a new branch for your feature or bug fix.
Commit Changes: Commit your changes with descriptive messages.
Push to Branch: Push your changes to the new branch.
Create a Pull Request: Submit a pull request to the main repository for review.

## Authors
Nnenna Njoku <nnennanjoku08@gmail.com> - Initial work and documentation.
Ibraihim Fuhad Suma - Contributions and feature development.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

