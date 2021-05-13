addonPath='extensions/sharpcuts.xip'
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
    echo '{"schemaVersion":33,"addons":[{"id":"sharpcuts@example.org","syncGUID":"{717ca71f-ce17-4223-bf50-9c7f04b0f64d}","version":"0.1","type":"extension","loader":null,"updateURL":null,"optionsURL":null,"optionsType":null,"optionsBrowserStyle":true,"aboutURL":null,"defaultLocale":{"name":"sharpcuts","description":"Add custom shortcuts to every page.","creator":null,"developers":null,"translators":null,"contributors":null},"visible":true,"active":true,"userDisabled":false,"appDisabled":false,"embedderDisabled":false,"installDate":1620912254417,"updateDate":1620912383215,"applyBackgroundUpdates":1,"path":"/home/user/.mozilla/firefox/owclmdyt.default/extensions/sharpcuts@example.org.xpi","skinnable":false,"sourceURI":"file:///home/user/repos/github/ida/skriptz/setup/browser/ff/extensions/sharpcuts.xip","releaseNotesURI":null,"softDisabled":false,"foreignInstall":false,"strictCompatibility":true,"locales":[],"targetApplications":[{"id":"toolkit@mozilla.org","minVersion":null,"maxVersion":null}],"targetPlatforms":[],"signedState":0,"signedDate":null,"seen":true,"dependencies":[],"incognito":"spanning","userPermissions":{"permissions":[],"origins":["*://*/*"]},"optionalPermissions":{"permissions":[],"origins":[]},"icons":{},"iconURL":null,"blocklistState":0,"blocklistURL":null,"startupData":null,"hidden":false,"installTelemetryInfo":{"source":"about:addons","method":"install-from-file"},"recommendationState":null,"rootURI":"jar:file:///home/user/.mozilla/firefox/owclmdyt.default/extensions/sharpcuts@example.org.xpi!/","location":"app-profile"}]}' > $profilePath/extensions.json
}
runProfileOnce() {
    # Run profile once in background, so profile-files get generated:
    firefox -P $profileName --headless &
    sleep 7
    pkill firefox
}

installAddon() {
    allowUnsignedAddons
    registerAddon
    createAddonsFolder
    cp $addonPath $profilePath/extensions
}

setupProfile() {
    runProfileOnce
}

main() {

    createProfile # ini
    getProfilePath
    echo profilePath is $profilePath
#rm -rf $profilePath/*; echo destroyed profile # destroy

    setupProfile

    installAddon

firefox example.org -P $profileName
# seems xip is missing
}; main

