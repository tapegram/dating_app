# dating_app

0) Activate virtual env:
`source venv/bin/activate`

1) Install requirements
`pip install -r requirements.txt`

2) To run:
`export FLASK_APP=app.py` (only needs to be run once)
`python -m flask run`


# Database
Currently the app is using firebase for the DB, which is basically just a rest api. That way there is no setup required to get the DB working locally.
