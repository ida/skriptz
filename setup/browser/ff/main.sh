addonPath='extensions/sharpcuts@example.org.xip'
profileName=ala
profilePath=''

main() {
    setupProfile
    installAddon
    #firefox example.org -P $profileName
# xip is missing
}


allowUnsignedAddons() {
    echo 'user_pref("xpinstall.signatures.required", false);' >> $profilePath/user.js
}

createAddonsFolder() {
    mkdir $profilePath/extensions
}

createProfileDirectory() {
    firefox -CreateProfile $profileName
    setProfilePath
}

createProfileFiles() {
    # Run profile once in background, so profile-files get generated:
    firefox -P $profileName --headless &
    sleep 7
    pkill firefox
}

installAddon() {
    setProfilePath
    allowUnsignedAddons
    registerAddon
    createAddonsFolder
    cp $addonPath $profilePath/extensions
}

registerAddon() {
    echo '{"schemaVersion":33,"addons":[{"id":"sharpcuts@example.org","syncGUID":"{717ca71f-ce17-4223-bf50-9c7f04b0f64d}","version":"0.1","type":"extension","loader":null,"updateURL":null,"optionsURL":null,"optionsType":null,"optionsBrowserStyle":true,"aboutURL":null,"defaultLocale":{"name":"sharpcuts","description":"Add custom shortcuts to every page.","creator":null,"developers":null,"translators":null,"contributors":null},"visible":true,"active":true,"userDisabled":false,"appDisabled":false,"embedderDisabled":false,"installDate":1620912254417,"updateDate":1620912383215,"applyBackgroundUpdates":1,"path":"'$profilePath'/extensions/sharpcuts@example.org.xpi","skinnable":false,"sourceURI":"file:///home/user/repos/github/ida/skriptz/setup/browser/ff/extensions/sharpcuts@example.org.xip","releaseNotesURI":null,"softDisabled":false,"foreignInstall":false,"strictCompatibility":true,"locales":[],"targetApplications":[{"id":"toolkit@mozilla.org","minVersion":null,"maxVersion":null}],"targetPlatforms":[],"signedState":0,"signedDate":null,"seen":true,"dependencies":[],"incognito":"spanning","userPermissions":{"permissions":[],"origins":["*://*/*"]},"optionalPermissions":{"permissions":[],"origins":[]},"icons":{},"iconURL":null,"blocklistState":0,"blocklistURL":null,"startupData":null,"hidden":false,"installTelemetryInfo":{"source":"about:addons","method":"install-from-file"},"recommendationState":null,"rootURI":"jar:file://'$profilePath'/extensions/sharpcuts@example.org.xpi!/","location":"app-profile"}]}' > $profilePath/extensions.json

    echo 'user_pref("extensions.webextensions.uuids", "{\"sharpcuts@example.org\":\"9f708e6d-e513-4132-ac94-73ae6703c5a4\"}");' >> $profilePath/user.js
}

setProfilePath() {
    # Assume find returns only one result:
    profilePath=$( find ~/.mozilla/firefox -name "*.$profileName" )
}

exists() {
    test -f $1 && exit 0
    test -d $1 && exit 0
    exit 1
}
setupProfile() {
                                               setProfilePath
    test ! -d $profilePath &&                  createProfileDirectory
    test ! -f $profilePath/extensions.json &&  createProfileFiles
}

main
