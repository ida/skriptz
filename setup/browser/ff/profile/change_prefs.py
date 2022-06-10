# Theoretically one can set prefs per profile/user.js, but
# since that doesn't work always, we write a script to
# modify profile/prefs.js directly.

# A line in prefs.js looks like this:

#   user_pref("full-screen-api.ignore-widgets", "true")


def main():
    nulines = []
    nuprops = {
        "full-screen-api.ignore-widgets": "true"
    }
    with open('prefs.js') as fil:
        lines = fil.readlines()
    for i, line in enumerate(lines):
        splits = line.split(',')
        prop = splits[1]
        val = splits[3]
        print(prop, val)

if __name__ == '__main__':
    main()
