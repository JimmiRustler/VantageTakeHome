cd %~dp0
python -m venv venv
call venv\Scripts\activate.bat
pip install -r requirements.txt
cd frontend
start cmd /k installfront.bat