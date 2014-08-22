PATH="$HOME/.virtenv/bin:$PATH"
git config --global credential.helper "cache --timeout=3600" # cache password for an hour
git clone https://github.com/collective/minimalplone4.git
cd minimalplone4
python bootstrap.py
./bin/buildout
