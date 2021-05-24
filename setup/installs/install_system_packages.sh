# Install system-packages. Tested with Ubuntu 20. Usage:
# ./install_system_packages.sh git vim screen curl wget


# Update package-manager, if not done already within the last day:
(find /var/lib/apt/periodic/update-success-stamp -mtime +1 |
grep update-success-stamp &> /dev/null) && (sudo apt update &> /dev/null)

# For each passed package-name:
for pkg in $@; do

    # Check if package is installed:
    ( dpkg -s $pkg &> /dev/null ) && true || ( # true makes exitcode be 0

        # If not, check if it's installable:
        ( ! apt-cache show $pkg &> /dev/null ) && exit 1 || (

            # If so, install it:
            ( ! sudo apt-get install $pkg &> /dev/null ) && exit 1 || exit 0

        )
    )

    # If an error ocurred say bye and break loop:
    if [ $? != 0 ]; then

        echo Install failed! Correct \"$pkg\" before re-running.; exit 1

    fi

done
