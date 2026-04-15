'''
python -m venv env1
python -m venv env2

env1\Scripts\activate
pip install numpy
pip install requests
pip freeze > requirements.txt
deactivate 

env2\Scripts\activate
pip install -r requirements.txt
deactivate 

'''