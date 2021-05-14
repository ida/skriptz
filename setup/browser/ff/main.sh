# Note: Firefox must *not* be running when executing this.

# Get default profile:
pattern='Default='
profileDirectoriesPath=$(realpath ~/.mozilla/firefox)
profileDirectoryName=$(grep $pattern $profileDirectoriesPath/profiles.ini)
profileDirectoryName=$(echo "${profileDirectoryName//$pattern/}")
profileDirectoryName=$(echo "${profileDirectoryName//1/}")
profileDirectoryPath=$profileDirectoriesPath/$profileDirectoryName

# Copy preferences into profile:
test ! -f $profileDirectoryPath/user.js &&
cp user.js $profileDirectoryPath

# Install addon (will open firefox and ask to confirm install):
test ! -f $profileDirectoryPath/extensions/sharpcuts@example.org.xpi &&
firefox -install -extensions extensions/sharpcuts@example.org.xpi
