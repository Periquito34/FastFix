
# FastFix

Requisito tener Docker bien instalado en tu pc.

1. Eliminar la carpeta enviroment.
2. Instalar venv cono pip install virtualenv
3. Crear un entorno python -m venv enviroment
4. activar el entorno enviroment/Scripts/activate
5. Realizar las siguientes instalaciones pip install django --- pip install django-bootstrap4  ---  pip install django-widget-tweak.
6. Ingresar el siguiente comando docker-compose up -d
7. Realizar esta instalacion pip3 install psycopg2-binary==2.9.5
8. Abrir Pgadmin y crear el servidor
9. ingresar el siguiente comando cd .\fastFixSystem\
10. Realizar las migraciones python manage.py makemigrations fastFix_app
11. python manage.py migrate
12. Correr el proyecto el siguiente comando: python manage.py runserver 0.0.0.0:8888
13. y ya esta.
