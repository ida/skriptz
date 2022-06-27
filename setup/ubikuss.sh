# Disable unattended upgrades on Ubuntu:
# sudo vi /etc/apt/apt.conf.d/20auto-upgrades

# Remove link-icons to trash and home-folder(set to true, to undo):
gsettings set org.gnome.shell.extensions.desktop-icons show-trash false
gsettings set org.gnome.shell.extensions.desktop-icons show-home false

# Install git and ubuntu-restricted-extras(video-codecs):
wget -qO- https://raw.githubusercontent.com/ida/skriptz/master/setup/installs/install_system_packages.sh | bash -s git ubuntu-restricted-extras

# Install extension to move top-bar to bottom:
# https://tipsonubuntu.com/2020/04/17/enable-single-bottom-panel-ubuntu-20-04-lts/

# Copy and source dotfiles:
mkdir -p ~/repos/github/ida
cd ~/repos/github/ida
git clone https://github.com/ida/skriptz.git
cp skriptz/setup/dotfiles/.[!.]* ~
. ~/.bashrc

# Configure git:
git config --global user.name "ida"
git config --global user.email $GIT_MAIL
git config --global url."https://api:$GIT_TOKEN@github.com/".insteadOf "https://github.com/"
#git config --global credential.helper "cache --timeout=36000"
git config --global core.excludesfile ~/.gitignore_global
