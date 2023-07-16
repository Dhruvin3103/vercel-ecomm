pip install -r build.sh

pip install -r requirements.txt

pip install Django

python manage.py collectstatic --no-input

python manage.py migrate

