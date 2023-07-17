pip install -r build.sh

pip install -r requirements.txt

pip uninstall decouple

python manage.py collectstatic --no-input

python manage.py migrate

python createsuperuser.py

