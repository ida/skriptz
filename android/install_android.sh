sudo apt install default-jdk -y # install java development kit

export JAVA_HOME=/usr/bin/java
export PATH=${JAVA_HOME}/bin:$PATH

cd


curl -O https://dl.google.com/android/repository/android-ndk-r13b-linux-x86_64.zip
unzip android-ndk-r13b-linux-x86_64.zip
NDK="${HOME}/android-ndk-r13b"

curl -O https://dl.google.com/android/repository/build-tools_r25-linux.zip
unzip build-tools_r25-linux.zip
mkdir android-sdk-linux/build-tools
mv android-7.1.1 android-sdk-linux/build-tools/25.0.0

curl -O https://dl.google.com/android/repository/android-16_r05.zip
unzip android-16_r05.zip
mv android-4.1.2 android-sdk-linux/platforms/android-16

curl -O https://dl.google.com/android/repository/platform-tools_r25-linux.zip
unzip platform-tools_r25-linux.zip -d android-sdk-linux/
