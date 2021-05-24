# Usage:
#
# In your app's directory do on the commandline: ./build_android_app.sh
#



APP_NAME=$(basename $PWD)

APP_ID_PATH="com/example/$APP_NAME"

JAVA_HOME=/usr/bin/java

PATH=${JAVA_HOME}/bin:$PATH

SDK="${HOME}/android-sdk-linux"

BUILD_TOOLS="${SDK}/build-tools/25.0.0"

PLATFORM="${SDK}/platforms/android-16"




# If exitcode of a line is not 0, or if a var is not set, exit with error:

set -eu


# Create needed directories:

mkdir -p build/gen build/obj build/apk


# Generate build files of res-directory:

"${BUILD_TOOLS}/aapt" package -f -m -J build/gen/ -S res \
    -M AndroidManifest.xml -I "${PLATFORM}/android.jar"


# Compile Java-file:

javac -source 1.7 -target 1.7 -bootclasspath "${JAVA_HOME}/jre/lib/rt.jar" \
    -classpath "${PLATFORM}/android.jar" -d build/obj \
    build/gen/$APP_ID_PATH/R.java java/$APP_ID_PATH/MainActivity.java


# Generate build files of compiled Java-file:

"${BUILD_TOOLS}/dx" --dex --output=build/apk/classes.dex build/obj/


# Build unsigned apk:
"${BUILD_TOOLS}/aapt" package -f -M AndroidManifest.xml -S res/ \
    -I "${PLATFORM}/android.jar" \
    -F build/$APP_NAME.unsigned.apk build/apk/

# Build aligned apk:
"${BUILD_TOOLS}/zipalign" -f -p 4 \
    build/$APP_NAME.unsigned.apk build/$APP_NAME.aligned.apk

# Generate key for the app-signature, if not existing:
test ! -f keystore.jks &&
keytool -genkeypair -keystore keystore.jks -alias androidkey \
     -validity 10000 -keyalg RSA -keysize 2048 \
     -storepass android -keypass android

# Build signed apk:
"${BUILD_TOOLS}/apksigner" sign --ks keystore.jks \
    --ks-key-alias androidkey --ks-pass pass:android \
    --key-pass pass:android --out ../$APP_NAME.apk \
    build/$APP_NAME.aligned.apk
