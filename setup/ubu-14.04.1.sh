sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install build-essential libssl-dev libjpeg62-dev libreadline-gplv2-dev wv libxml2-dev libxslt1-dev libsasl2-dev poppler-utils libdb-dev libldap2-dev

virtualenv .virtenv
. .virtenv/bin/activate

# Overcome "pkg_resources.DistributionNotFound: setuptools>=3.3"
pip install setuptools -U

mkdir .buildout
mkdir .buildout/eggs
cat <<EOM > '.buildout/default.cfg'
[buildout]
parts = 
    instance
    plonesite
eggs-directory = $HOME/.buildout/eggs
extends = http://dist.plone.org/release/4-latest/versions.cfg
[instance]
recipe = plone.recipe.zope2instance
user = admin:admin
eggs = 
    Pillow
    Plone
[plonesite]
recipe = collective.recipe.plonesite
EOM


mkdir builds
mkdir builds/plone
cd builds/plone
touch buildout.cfg
wget http://downloads.buildout.org/2/bootstrap.py
python bootstrap.py
./bin/buildout
./bin/instance fg
