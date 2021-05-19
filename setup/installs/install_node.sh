installNodejs() {
# Install node's version-manager 'nvm':
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.38.0/install.sh | bash
# With it install node's latest stable release:
nvm install node
# Source added enviroment-var 'NVM':
. ~/.bashrc
}
updateNpm() {
# https://docs.npmjs.com/getting-started/installing-node
# "Node comes with npm installed so you should have a version of npm. However, npm gets updated more frequently than Node does, so you'll want to make sure it's the latest version."
npm install npm -g
}
setupNodejs() {
installNodejs
updateNpm
}
setupNodejs()
