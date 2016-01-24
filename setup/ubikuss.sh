git config --global user.name "Ida Ebkes"
git config --global user.email "contact@ida-ebkes.eu"
git config --global credential.helper "cache --timeout=36000" 
git clone https://github.com/ida/skriptz.git
. ./skriptz/setup/syspckgs/min.sh
cp skriptz/setup/dotfiles/.[!.]* ~
. ~/.bashrc
git config --global core.excludesfile ~/.gitignore_global
