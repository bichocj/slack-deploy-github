echo
echo "cd /srv/www/eventus/src/"
cd /srv/www/eventus/src/

echo
echo "git pull"
git pull

echo
echo ". /srv/venv/bin/activate"
. /srv/venv/bin/activate

echo
echo "python manage.py migrate"
python manage.py migrate

echo
echo "python manage.py collectstatic --no-input"
python manage.py collectstatic --no-input

echo
echo "service apache2 restart"
service apache2 restart