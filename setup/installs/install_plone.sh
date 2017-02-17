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
