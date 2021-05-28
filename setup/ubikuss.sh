# Install git and ubuntu-restricted-extras(video-codecs):
wget -qO- https://raw.githubusercontent.com/ida/skriptz/master/setup/installs/install_system_packages.sh | bash -s git ubuntu-restricted-extras

# Clone and source dotfiles:
mkdir -p ~/repos/github/ida
cd ~/repos/github/ida
git clone https://github.com/ida/skriptz.git
cp skriptz/setup/dotfiles/.[!.]* ~
. ~/.bashrc

# Configure git:
git config --global user.name "ida"
git config --global user.email "1715762+ida@users.noreply.github.com"
git config --global credential.helper "cache --timeout=36000" 
git config --global core.excludesfile ~/.gitignore_global
