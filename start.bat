cd %~dp0
call venv\Scripts\activate.bat
start cmd /k python backend\manage.py runserver
cd frontend
start cmd /k npm start