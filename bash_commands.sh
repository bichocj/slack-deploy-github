cd /srv/www/eventus/src/
git pull
. /srv/venv/bin/activate
python manage.py migrate
python manage.py collectstatic --no-input
service apache2 restart