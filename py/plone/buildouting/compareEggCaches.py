# Compare two egg-caches and print additional, respectively missing egg-names.
# Usage:
# $ python [this_script_path] [path_to_an_egg_cache] [path_to_another_egg_cache]

import os
import sys


def getEggNamesOfEggCache(eggs_path):
    egg_name = None
    egg_names = []
    egg_paths = os.listdir(eggs_path)
    for egg_path in egg_paths:
        egg_name = egg_path.split('-')[0]
        egg_names.append(egg_name)
    return egg_names

def compareEggNames(names, other_names):
    additional_names = []
    missing_names = []
    for name in names:
        if not name in other_names:
            additional_names.append(name)
    for name in other_names:
        if not name in names:
            missing_names.append(name)
    print "These eggs are additional:\n" + ', '.join(additional_names) + '\n'\
          "These eggs are missing:\n" + ', '.join(missing_names)

def main():
    eggs_cache_path = sys.argv[1]
    other_eggs_cache_path = sys.argv[2]
    egg_names = getEggNamesOfEggCache(eggs_cache_path)
    other_egg_names = getEggNamesOfEggCache(other_eggs_cache_path)
    compareEggNames(egg_names, other_egg_names)

main()
