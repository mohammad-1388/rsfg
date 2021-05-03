import os
from time import sleep
activate = r"venv\Scripts\activate.bat"
activate = str(activate)
os.system(activate)
sleep(2)
os.system("python manage.py runserver 9012")