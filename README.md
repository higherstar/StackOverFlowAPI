## Deployed Instance
https://evening-bastion-23546.herokuapp.com

# GUIDE
1. pull source code
2. create virtualenv on machine
3. * ``virtualenv venv``
4. activate your virtualenv ``source venv/bin/activate`` in macos or ``venv\Scripts\activate.bat`` in windows.
5. install python packages
   * ``(venv) pip install -r requirements.txt``
6. set the FLASK_APP:
   * ``(venv) export FLASK_APP=run.py``
7. Run project
   * ``(venv) flask run``