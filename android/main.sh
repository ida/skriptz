# Usage: $ bash main.sh an-app-name

# bash install_android.sh # TODO

set -e # abort if exitcode is not 0

test ! $1 && (echo You must give an app-name.; exit 1)

python create_android_app.py $1

cd $1

cp ../build_android_app.sh .

./build_android_app.sh

echo "You have an installable android-app-file: ./$1/build/$1.apk"
