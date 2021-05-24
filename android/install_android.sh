SDK_PATH=$HOME/.android-sdk-linux

# Install Java-Development-Kit, including Java, if not done already:
bash ../setup/installs/install_system_packages.sh default-jdk

# Abort, if exitcode is not 0, or used var is not set:
set -eu

# Do nothing, if SDK directory exists already:
test -d $SDK_PATH && echo \"$SDK_PATH\" exists. Delete to recreate. || (


    # Otherwise create SDK directory:
    mkdir $SDK_PATH

    # Locate into SDK directory:
    cd $SDK_PATH

    echo 'Installing Android and Android-App-build-tools...'

    # Install Android:
    curl -O https://dl.google.com/android/repository/android-16_r05.zip
    unzip android-16_r05.zip
    mkdir $SDK_PATH/platforms
    mv android-4.1.2 $SDK_PATH/platforms/android-16

    # Install tools for building an Android app file (.apk):
    curl -O https://dl.google.com/android/repository/build-tools_r25-linux.zip
    unzip build-tools_r25-linux.zip
    mkdir -p $SDK_PATH/build-tools
    mv android-7.1.1 $SDK_PATH/build-tools/25.0.0


) # End of SDK_PATH does not exist already.
