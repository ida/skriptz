# Usage: $ bash main.sh an-app-name

# bash install_android.sh # TODO

set -e # abort if exitcode is not 0

test ! $1 && (echo You must give an app-name.; exit 1)

python create_android_app.py $1

bash build_android_app.sh $1
