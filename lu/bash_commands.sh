. /srv/venv/bin/activate
cd /srv/www/eventus/src/
git pull
python manage.py migrate
python manage.py collectstatic --no-input
service apache2 restart