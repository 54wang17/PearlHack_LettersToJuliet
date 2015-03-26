/Flask Project/

This is a chanllenge project for PearlHack on March 21-22,2015
@author Jiaoling Chen, Yiqi Wang

//Package Requirement described in "requirements.txt"

To run this application,firstly deploy virtural environment and activate it:
$ virtualenv yourprojectname
>>>New python executable in env/bin/python

$ source ./env/bin/activate
// clone repository
$ git clone ...

//install required packages
$pip install -r requirements.txt

//customize your configure
modified the BASE_PATH to the path of yourfolder in config.py

//initialize database
$ python db_create.py

//run application
python run.py
