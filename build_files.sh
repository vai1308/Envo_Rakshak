python3.9 -m venv venv
source venv/Scripts/activate
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear