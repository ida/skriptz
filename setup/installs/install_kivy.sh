# After: http://kivy.org/docs/installation/installation-linux.html#ubuntu-11-10-or-newer

# Ubuntu 12.04 with Python 2.7¶

# Install necessary system packages
sudo apt-get install -y build-essential mercurial git python2.7 \
python-setuptools python-dev ffmpeg libsdl-image1.2-dev \
libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libsdl1.2-dev \
libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev

# Bootstrap a current Python environment
sudo apt-get remove --purge -y python-virtualenv python-pip
sudo easy_install-2.7 -U pip
sudo pip2.7 install -U virtualenv

# Install current version of Cython
sudo apt-get remove --purge -y cython
sudo pip2.7 install -U cython

# Install other PyGame dependencies
sudo apt-get remove --purge -y python-numpy
sudo pip2.7 install -U numpy

# Install PyGame
sudo apt-get remove --purge python-pygame
hg clone https://bitbucket.org/pygame/pygame
cd pygame
python2.7 setup.py build
sudo python2.7 setup.py install
cd ..
sudo rm -rf pygame

# Create a vitualenv
rm -rf venv
virtualenv -p python2.7 --system-site-packages venv

# Install stable version of Kivy into the virtualenv
venv/bin/pip install kivy
# For the development version of Kivy, use the following command instead
# venv/bin/pip install git+https://github.com/kivy/kivy.git@master

# Install development version of buildozer into the virtualenv
venv/bin/pip install git+https://github.com/kivy/buildozer.git@master

# Install development version of plyer into the virtualenv
venv/bin/pip install git+https://github.com/kivy/plyer.git@master

# Install a couple of dependencies for KivyCatalog
venv/bin/pip install -U pygments docutils

