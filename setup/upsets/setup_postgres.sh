app_name=appy
postgresql_db_name=$app_name
postgresql_db_user_name=$app_name
postgresql_db_user_pw=$app_name
dump_file_name=${app_name}.sql
dump_file_path=${dump_file_name}
#
# SYS-PCKGS
#
updateSysPckgsManager() {
sudo apt-get update
sudo apt-get dist-upgrade
}
installSysPckgs() {
sudo apt-get install python-virtualenv git python-dev build-essential python-lxml libxslt1-dev libxml2 python-tk openjdk-7-jre redis-server libffi-dev postgresql libpq-dev libnotify-bin poppler-utils wv -y
}
setupSysPckgs() {
updateSysPckgsManager
installSysPckgs    
}
#
# NODEJS
#
installNodejs() {
# Following:
# https://docs.npmjs.com/getting-started/installing-node
# Leads to:
# https://github.com/nodesource/distributions#installation-instructions
# Which tells us to do this:
curl -sL https://deb.nodesource.com/setup_5.x | sudo -E bash -
# For the curious, the latest vs. of the script can be seen on GitHub, here:
# https://github.com/nodesource/distributions/blob/master/deb/setup_5.x
# Script ends with:
# "Run `apt-get install nodejs` (as root) to install Node.js 5.x and npm"
# So, we do it:
sudo apt-get install nodejs -y
}
updateNpm() {
# https://docs.npmjs.com/getting-started/installing-node
# "Node comes with npm installed so you should have a version of npm. However, npm gets updated more frequently than Node does, so you'll want to make sure it's the latest version."
sudo npm install npm -g
}
installNodejsPckgs() {
sudo npm install -g jshint csslint bower grunt-cli gulp blueimp-tmpl uglify-js less
}
installNodejsPckgsOfConfig() {
# Install node-pckgs defined in 'package.json':
sudo npm install
}
setupNodejs() {
installNodejs
updateNpm
installNodejsPckgs
installNodejsPckgsOfConfig
}
#
# POSTGRESQL
#
# https://help.ubuntu.com/community/PostgreSQL
#
restoreDump() {
sudo -u postgres psql $database_name < $dump_file_path
}
listAllPostgresqlDBs() {
sudo -u postgres psql -c "\l"
}
deletePostgresqlDB() {
sudo -u postgres dropdb $postgresql_db_name
}
createPostgresqlDB() {
sudo -u postgres createdb $postgresql_db_name
}
createPostgresqlDBUser() {
sudo -u postgres createuser $postgresql_db_user_name
}
setPostgresqlDBUserPassword() {
sudo -u postgres psql -c "ALTER USER $postgresql_db_user_name WITH PASSWORD '$postgresql_db_user_pw';"
}
grantPostgresqlDBPrivsToUser() {
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $postgresql_db_name TO $postgresql_db_user_name;"
}
reloadPostgresqlConfig() {
sudo /etc/init.d/postgresql reload
}
modifyPostgresqlConf() {
echo "TODO: Scriptify setting 'peer' to 'md5' for 'local all' in conf."
# Always update conf-settings after a modification:
reloadPostgresqlConfig
}
setupPostgresql() {
modifyPostgresqlConf
createPostgresqlDB
createPostgresqlDBUser
setPostgresqlDBUserPassword 
grantPostgresqlDBPrivsToUser
}
#
# BOWER
#
setupBower() {
bower install
}
#
# GRUNT
#
setupGrunt() {
grunt
}
#
# SOLR
#
setupSolr() {
./bin/solr-instance start
}
#
# PLONE
#
setupPlone() {
cp auth.cfg.in auth.cfg
virtualenv .virtenv
./.virtenv/bin/python bootstrap.py
./bin/buildout
# If you'd get "Error: There is a version conflict. We already have: zope.interface/zc.buildout/setuptools/...",
# try destroying+recreating virtenv, bootstrap with virt-py and redo bin/buidout.
}
#
# ZODB
#
setupZodb() {
./bin/fetch-from-staging
# ./bin/fetch-from-staging: 8: ./bin/fetch-from-staging: bin/supervisorctl: not found
# ./bin/fetch-from-live
}
#
# MAIN
#
main() {
# setupSysPckgs
# setupNodejs
# setupPostgresql
# setupBower
# setupGrunt
# setupPlone
setupZodb
}

main

#
# EOF
#
