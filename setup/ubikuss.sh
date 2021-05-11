# Install git:
wget -qO- https://raw.githubusercontent.com/ida/skriptz/master/setup/installs/install_system_packages.sh | bash -s git 

# Clone and source dotfiles:
mkdir -p ~/repos/github/ida
cd ~/repos/github/ida
git clone https://github.com/ida/skriptz.git
. ./skriptz/setup/syspckgs/min.sh
cp skriptz/setup/dotfiles/.[!.]* ~
. ~/.bashrc

# Configure git:
git config --global user.name "A User"
git config --global user.email "auser@example.org"
git config --global credential.helper "cache --timeout=36000" 
git config --global core.excludesfile ~/.gitignore_global
