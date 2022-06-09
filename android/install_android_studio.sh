# This is only for achive purposes, my machine froze regurlary when using android-studio.
# Also a generated minimum app has a size about 40MB! That's ridiculous, ain't it? Ja!
# Instead take the other script ( see README.txt ), you'll then have sweet 40KB.
# No, really. Yes, it's a thousand times smaller than the dictatorships' way.

sudo apt-get install libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 libbz2-1.0:i386
# Download AndroidStudio from https://developer.android.com/studio
sudo mv ~/Downloads/android-studio-ide-202.7351085-linux.tar.gz /usr/local
cd /usr/local
sudo tar -xvzf android-studio-ide-202.7351085-linux.tar.gz
# We now have an executable to start AndroidStudio:
./android-studio/bin/studio.sh
