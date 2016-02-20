#
# NODEJS
#
installNodejs() {
# https://github.com/creationix/nvm
# We use node-vs-mngr, to be able to do a sudo-less local install.
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.30.2/install.sh | bash
nvm install 5.0
source ~/.bashrc
}
updateNpm() {
# https://docs.npmjs.com/getting-started/installing-node
# "Node comes with npm installed so you should have a version of npm. However, npm gets updated more frequently than Node does, so you'll want to make sure it's the latest version."
npm install npm -g
}
installNodejsPckgs() {
npm install -g jshint csslint bower grunt-cli gulp blueimp-tmpl uglify-js less
}
installNodejsPckgsOfConfig() {
# Install node-pckgs defined in 'package.json':
npm install -g
}
setupNodejs() {
installNodejs
updateNpm
installNodejsPckgs
installNodejsPckgsOfConfig
}

