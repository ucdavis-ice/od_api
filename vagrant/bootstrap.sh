

sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt trusty-pgdg main" >> /etc/apt/sources.list'
wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get -y install postgresql-9.3-postgis-2.1 postgresql-contrib postgresql-server-dev-9.3 python-dev
sudo -u postgres psql -U postgres -c 'CREATE EXTENSION adminpack;'
sudo -u postgres psql -U postgres -c "CREATE ROLE django_user WITH SUPERUSER;"
sudo -u postgres psql -U postgres -c "ALTER ROLE django_user WITH PASSWORD 'g0';"
sudo -u postgres psql -U postgres -c "CREATE DATABASE django_postgis WITH ENCODING 'UTF8';"
sudo -u postgres psql -U postgres -d django_postgis -c 'CREATE EXTENSION postgis;'


cd /vagrant
python get-pip.py
pip install Django==1.7
pip install psycopg2

