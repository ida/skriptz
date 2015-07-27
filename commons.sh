# ======
# Remind
# ======

# Get string of file:
# str_of_file=$( <path/to/file )

# Get last returned val:
# last_returned_val=$?
#
# Nota: A function's return cannot be fethed like 'var=funk.
# Functions can only return numeric values, conveniently
# 0 and 1 are used for symbolizing False and True.

# Declare an array:
# arrayname=(a b c)

# Get an array:
# arraycontent="${arrayname[@]}"
# Nota: Calling arrayname alone, will only return first item.

# Convert array to string:
# strg=$( printf "%s" "${arrayname[@]}" )

# =======
# Compare
# =======
strEqualsStr () { if [ "$1" = "$2" ]; then return 1; else return 0; fi }
strStartswithStr () { if [[ "$1" = "$2"* ]]; then return 1; else return 0; fi }
strContainsStr () { if [[ "$1" = *"$2"* ]]; then return 1; else return 0; fi }
strEndswithStr () { if [[ "$1" = *"$2" ]]; then return 1; else return 0; fi }
#
# Example:
# strEndswithStr 'The end.' 'end.'
# if [[ $? = 1]]; then $doSth; fi

# ====
# Loop
# ====
forEachDo() { arrayname=$1[@] array=("${!arrayname}") kommand=$2; for i in "${array[@]}" ; do "$kommand" "$i"; done }
#
# Example:
# items=("Hello world!" "What a wonderful day." "Couldn't be better." "Ciao!")
# forEachDo items "echo"
#
# Nota:
# http://stackoverflow.com/questions/16461656/bash-how-to-pass-array-as-an-argument-to-a-function:

