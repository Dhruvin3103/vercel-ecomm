pip install -r build.sh

pip install -r requirements.txt

pip install whitenoise

python manage.py collectstatic --no-input

python manage.py migrate

