/Flask Project/
This is a chanllenge project for PearlHack on March 21 -22

@author Jiaoling Chen, Yiqi Wang

Package Requirement:

flask==0.10.1
Flask-SQLALchemy==1.0
Flask-WTF

To run this application

open terminal:

cd /path/to/LettersToJuliet

source env/bin/activate

//install packages stated above

pip install flask==0.10.1

pip install Flask-SQLALchemy==1.0

pip install Flask-WTF

//customize your configure

modified the BASE_PATH to the path of yourfolder in  config.py

//initialize database

$ python db_create.py

//run application

python run.py
