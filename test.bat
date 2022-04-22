cd %~dp0
call venv\Scripts\activate.bat
cd backend
pytest --cov-report term-missing --cov=adDatabase tests/tests.py
pause