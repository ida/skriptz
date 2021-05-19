####################
# INSTALL ELECTRON #
####################

npm i -D electron@latest


##########################
# CREATE AN ELECTRON APP #
##########################

git clone https://github.com/electron/electron-quick-start

cd electron-quick-start

npm install && npm start


################################
# BUILD SYSTEM PACKAGES OF APP #
################################

# Needed for package-builder electron-forge:
sudo apt-get install rpm -y

# Install package-builder electron-forge:
npm install --save-dev @electron-forge/cli

npx electron-forge import

# Build packages:
npm run make

# Install package:
sudo dpkg -i ./electron-quick-start_1.0.0_amd64.deb

# Uninstall package and its possible dependencies:
sudo apt-get autoremove electron-quick-start -y


#####################
# BUILD ANDROID APP #
#####################

sudo apt install default-jdk -y # install java development kit

npm install -g androidjs-builder

androidjs init # answer with 'my-android-app'

cd my-android-app

npm run build

# Gives us an apk-file in ./dist :) Upload it to e.g. glitch.com, send
# download-link e.g. via mail, open link in android, after download go
# to folder-app, click on file, confirm install.
