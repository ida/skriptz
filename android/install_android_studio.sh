sudo apt-get install libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 libbz2-1.0:i386
# Download AndroidStudio from https://developer.android.com/studio
sudo mv ~/Downloads/android-studio-ide-202.7351085-linux.tar.gz /usr/local
cd /usr/local
sudo tar -xvzf android-studio-ide-202.7351085-linux.tar.gz
# We now have an executable to start AndroidStudio:
./android-studio/bin/studio.sh
