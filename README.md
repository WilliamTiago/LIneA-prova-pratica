# LIneA-prova-pratica
LIneA - processo seletivo full stack developer - prova prática

git clone https://github.com/WilliamTiago/LIneA-prova-pratica.git
python3 -m venv venvcd 
source venv/bin/activate
pip install django djangorestframework
django-admin startproject config . 
python manage.py runserver
python manage.py startapp api
pip install requests
no arquivo de configuração settings.py na past conf deve ser adicionado o app "api" no vetor "INSTALLED_APPS"
python manage.py makemigrations caso precisacemos adicionar um model as migrações
python manage.py migrate
python manage.py createsuperuser admim admin@python.com admin

