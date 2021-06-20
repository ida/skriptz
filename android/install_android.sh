# Usage: $ bash install_android.sh

# All used paths must correspond with those in './build_android_app.sh':
SDK_PATH=$HOME/.android-sdk-linux

# Abort, if exitcode is not 0, or used var is not set:
set -eu

# Install Java-Development-Kit, including Java, if not done already:
bash ../setup/installs/install_system_packages.sh default-jdk

# Do nothing, if SDK directory exists already:
test -d $SDK_PATH && exit 0 || (


    # Otherwise create SDK directory:
    mkdir $SDK_PATH

    # Locate into SDK directory:
    cd $SDK_PATH

    echo 'Installing Android and Android-App-build-tools...'

    # Install Android 4:
    curl -O https://dl.google.com/android/repository/android-16_r05.zip
    unzip android-16_r05.zip
    mkdir $SDK_PATH/platforms
    mv android-4.1.2 $SDK_PATH/platforms/android-16

    # Install Android 6:
    # curl -O https://dl.google.com/android/repository/android-23_r02.zip
    # unzip android-23_r02.zip
    #mkdir $SDK_PATH/platforms
    #mv android-6.0 $SDK_PATH/platforms/android-24

    # Install tools for building an Android app file (.apk) vs 30, for vs 25 simply switch numbers :
    curl -O https://dl.google.com/android/repository/build-tools_r30-linux.zip
    unzip build-tools_r30-linux.zip
    mkdir -p $SDK_PATH/build-tools
    mv android-11 $SDK_PATH/build-tools/30.0.0


) # End of SDK_PATH does not exist already.
