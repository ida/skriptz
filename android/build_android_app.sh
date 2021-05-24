# Usage:
#
# In your app's directory do on the commandline: bash build_android_app.sh an-app-name
#
# Important: app-name must not end with a slash.



# If exitcode of a line is not 0, or if a var is not set, exit with error:

set -eu

test ! $1 && (echo You must give an app-name.; exit 1)

APP_NAME=$1

APP_ID_PATH="com/example/$APP_NAME"

JAVA_HOME=/usr/bin/java

PATH=${JAVA_HOME}/bin:$PATH

SDK="${HOME}/android-sdk-linux"

BUILD_TOOLS="${SDK}/build-tools/25.0.0"

PLATFORM="${SDK}/platforms/android-16"






# Create needed directories:

mkdir -p $APP_NAME/build/gen $APP_NAME/build/obj $APP_NAME/build/apk


# Generate build files of res-directory:

"${BUILD_TOOLS}/aapt" package -f -m -J $APP_NAME/build/gen/ -S $APP_NAME/res \
    -M $APP_NAME/AndroidManifest.xml -I "${PLATFORM}/android.jar"


# Compile Java-file:

javac -source 1.7 -target 1.7 -bootclasspath "${JAVA_HOME}/jre/lib/rt.jar" \
    -classpath "${PLATFORM}/android.jar" -d $APP_NAME/build/obj \
    $APP_NAME/build/gen/$APP_ID_PATH/R.java $APP_NAME/java/$APP_ID_PATH/MainActivity.java


# Generate build files of compiled Java-file:

"${BUILD_TOOLS}/dx" --dex --output=$APP_NAME/build/apk/classes.dex $APP_NAME/build/obj/


# Build unsigned apk:
"${BUILD_TOOLS}/aapt" package -f -M $APP_NAME/AndroidManifest.xml -S $APP_NAME/res/ \
    -I "${PLATFORM}/android.jar" \
    -F $APP_NAME/build/$APP_NAME.unsigned.apk $APP_NAME/build/apk/

# Build aligned apk:
"${BUILD_TOOLS}/zipalign" -f -p 4 \
    $APP_NAME/build/$APP_NAME.unsigned.apk $APP_NAME/build/$APP_NAME.aligned.apk

# Generate key for the app-signature, if not existing:
test ! -f $APP_NAME/keystore.jks &&
keytool -genkeypair -keystore $APP_NAME/keystore.jks -alias androidkey \
     -validity 10000 -keyalg RSA -keysize 2048 \
     -storepass android -keypass android

# Build signed apk:
"${BUILD_TOOLS}/apksigner" sign --ks $APP_NAME/keystore.jks \
    --ks-key-alias androidkey --ks-pass pass:android \
    --key-pass pass:android --out $APP_NAME.apk \
    $APP_NAME/build/$APP_NAME.aligned.apk

# Remove build-directory:
rm -rf $APP_NAME/build


echo You have an installable android-app: ./$APP_NAME.apk
