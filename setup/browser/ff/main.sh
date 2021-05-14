addonPath='extensions/sharpcuts@example.org.xip'

profileName=ala

profilePath=''

displayLogs=0

main() {
    setProfilePath # ini
    setupProfile
    installAddon
    #firefox example.org -P $profileName
# xip is missing
}


allowUnsignedAddons() {
    local text='user_pref("xpinstall.signatures.required", false);'
    local path=$profilePath/user.js
    (grep "$text" $path &> /dev/null) && log Unsigned addons are allowed. || (
        log Unsigned addons are not allowed.
        echo 'user_pref("xpinstall.signatures.required", false);' >> $profilePath/user.js
        log Unsigned addons are now allowed.
    )
}

copyAddonToAddonsFolder() {
    test -f $profilePath/extensions/$addonPath && cp $addonPath $profilePath/extensions
}

createAddonsFolder() {
    test ! -d $profilePath/extensions && mkdir $profilePath/extensions
}

createProfileDirectory() {
    test ! -z $profilePath && log We have a profile-directory. || (
        log Creating profile.
        firefox -CreateProfile $profileName
        setProfilePath
        log Created profile.
    )
}

createProfileFiles() {
    test -f $profilePath/extensions.json && log We have profile-files. || (
        log Running profile once in background, so profile-files get generated.
        firefox -P $profileName --headless > /dev/null 2>&1 &
        sleep 7
        # Assume we are the only firefox process:
        pkill firefox &> /dev/null
        log Profile-files were generated.
    )
}


installAddon() {
    allowUnsignedAddons
    registerAddon
    createAddonsFolder
    copyAddonToAddonsFolder
}

log() {
    test $displayLogs == 0 && echo $@
}

registerAddon() {
    echo '{"schemaVersion":33,"addons":[{"id":"sharpcuts@example.org","syncGUID":"{717ca71f-ce17-4223-bf50-9c7f04b0f64d}","version":"0.1","type":"extension","loader":null,"updateURL":null,"optionsURL":null,"optionsType":null,"optionsBrowserStyle":true,"aboutURL":null,"defaultLocale":{"name":"sharpcuts","description":"Add custom shortcuts to every page.","creator":null,"developers":null,"translators":null,"contributors":null},"visible":true,"active":true,"userDisabled":false,"appDisabled":false,"embedderDisabled":false,"installDate":1620912254417,"updateDate":1620912383215,"applyBackgroundUpdates":1,"path":"'$profilePath'/extensions/sharpcuts@example.org.xpi","skinnable":false,"sourceURI":"file:///home/user/repos/github/ida/skriptz/setup/browser/ff/extensions/sharpcuts@example.org.xip","releaseNotesURI":null,"softDisabled":false,"foreignInstall":false,"strictCompatibility":true,"locales":[],"targetApplications":[{"id":"toolkit@mozilla.org","minVersion":null,"maxVersion":null}],"targetPlatforms":[],"signedState":0,"signedDate":null,"seen":true,"dependencies":[],"incognito":"spanning","userPermissions":{"permissions":[],"origins":["*://*/*"]},"optionalPermissions":{"permissions":[],"origins":[]},"icons":{},"iconURL":null,"blocklistState":0,"blocklistURL":null,"startupData":null,"hidden":false,"installTelemetryInfo":{"source":"about:addons","method":"install-from-file"},"recommendationState":null,"rootURI":"jar:file://'$profilePath'/extensions/sharpcuts@example.org.xpi!/","location":"app-profile"}]}' > $profilePath/extensions.json

    echo 'user_pref("extensions.webextensions.uuids", "{\"sharpcuts@example.org\":\"9f708e6d-e513-4132-ac94-73ae6703c5a4\"}");' >> $profilePath/user.js
}

setProfilePath() {
    # Assume find returns only one result:
    profilePath=$( find ~/.mozilla/firefox -name "*.$profileName" )
    log Now profilePath is: $profilePath
}

setupProfile() {
    createProfileDirectory
    createProfileFiles
}

main
