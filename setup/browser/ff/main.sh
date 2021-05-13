addonFilesPath='/home/user/tmp/test-firefox/addon-files'
profileName=some-profile
profilePath=''


createAddonsFolder() {
    firefox -CreateProfile $profileName
}

createProfile() {
    firefox -CreateProfile $profileName
}

getProfilePath() {
    # Assume find returns only one result:
    profilePath=$( find ~/.mozilla/firefox -name "*.$profileName" )
}

allowUnsignedAddons() {
    echo 'user_pref("xpinstall.signatures.required", false)' >> $profilePath/user.js
}

registerAddon() {
    echo 'registerAddon' $profilePath/extensions.json
}
runProfileOnce() {
    # Run profile once in background, so profile-files get generated:
    firefox -P $profileName --headless &
    sleep 7
    pkill firefox
}

installAddon() {
    allowUnsignedAddons
    #registerAddon
    createAddonsFolder
    # Copy files into profile:
    getProfilePath
    echo profilePath is $profilePath
    cp -r $addonFilesPath/* $profilePath
}

setupProfile() {
    runProfileOnce
}

main() {

#    createProfile # ini
    getProfilePath
    echo profilePath is $profilePath
#rm -rf $profilePath/*; echo destroyed profile # destroy

    setupProfile

    installAddon

firefox example.org -P $profileName
# seems xip is missing
}; main

