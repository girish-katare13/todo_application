# todo_application

Project Name: To-Do List Application

Prerequisites:
- Make sure you have the following installed:
  - Python
  - pip (Python package installer)
  - pipenv (if not installed, run: pip install pipenv)


Instructions to Run the Project:
1. Clone the project repository from GitHub:
   git clone https://github.com/girish-katare13/todo_application.git

2. Activate pipenv virtual environment:
   pipenv

3. Install depandancies:
   (this will install all depandancies for this project)
   pipenv install

5. Navigate to the project directory:
   cd todo_app

6. Make migrations to set up the database:
   python manage.py makemigrations
   python manage.py migrate

7. Start the Django development server:
   python manage.py runserver
