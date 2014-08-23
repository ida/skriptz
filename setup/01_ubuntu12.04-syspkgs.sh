#adduser ida sudo

# Update pck-managers:
apt-get update
apt-get dist-upgrade
aptitude update
aptitude dist-upgrade

# General:
apt-get install git screen wget python-virtualenv

# Plone min:
apt-get install python-setuptools python-dev build-essential libssl-dev libxml2-dev libxslt1-dev libbz2-dev libjpeg62-dev

# Plone opt:
apt-get install libreadline-dev wv poppler-utils

# Archive: Ubuntu 10:
#apt-get install g++ zlibc python-imaging zlib1g-dev python-dev build-essential

# Archive: Ubuntu 11:
#apt-get install build-essentials g++ g++-4.2 zlibc python-imaging zlib1g-dev python-dev

# PostgreSQL:
aptitude install libapache2-mod-php5 postgresql-8.4 postgresql-contrib-8.4 postgresql-client-8.4 php5-pgsql postgresql-plperl-8.4 rsync patch ed python-virtualenv git gcc g++ python-dev dpkg-dev mysql-client apt-get install libmysqlclient-dev libjpeg-dev zlib1g-dev zlibc  python2.7-lxml libxml2-dev libxslt-dev  curl-dev pycurl python2.7-pycurl  libcurl4-openssl-dev postgresql-server-dev-8.4 libmemcached-dev libmemcached-tools libsvn-dev libatlas-dev libatlas-base-dev  python-liblas liblapack-dev python2.7-numpy




