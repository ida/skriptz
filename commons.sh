
fileExists() { if [ -f $1 ]; then return 1; else return 0; fi }
strEqualsStr () { if [ "$1" = "$2" ]; then return 1; else return 0; fi }
strStartswithStr () { if [[ "$1" = "$2"* ]]; then return 1; else return 0; fi }
strContainsStr () { if [[ "$1" = *"$2"* ]]; then return 1; else return 0; fi }
strEndswithStr () { if [[ "$1" = *"$2" ]]; then return 1; else return 0; fi }
forEachDo() { arrayname=$1[@] array=("${!arrayname}") kommand=$2; for i in "${array[@]}" ; do "$kommand" "$i"; done }

str_of_file=''
fileExists README.md
if [[ $? = 1 ]]; then str_of_file=$( <README.md ); fi
echo $str_of_file

# =====
# Usage
# =====
# 
# $1, $2 and so on, fetch the passed arguments in numeric order, execute a function like:
#
# functionName argument1 argument2
#
# Examples:
# strEndswithStr 'This is the end.' 'the end.'
# strEndswithStr 'This is the end.' 'The end.'
#
# Quiz: Which of the above two expressions is true?
# 
# ============
# Shell-basics
# ============
#
#
# Declare a function
# ------------------
#
# functionName() { functionContent }
#
# Example:
# showMeTheWayToTheNext() { echo $HOME }
# 
#
# Condition based on a functions returned val
# -------------------------------------------
#
# last_returned_val=$?
#
# Example:
# strEndswithStr 'The end.' 'end.'
# if [[ $? = 1]]; then $doSth; fi
#
# Nota: A function's return cannot be fetched like 'var=funk'.
# Functions can only return numeric values, conveniently
# 0 and 1 are used for symbolizing False and True.
#
#
# Get string of file
# ------------------
#
# fileExists path/to/file.ext
# if [[ $? = 1 ]]; then str_of_file=$( <$1 ); fi
#
# Nota: We can't put this in a function, if we want to fetch it as a var,
# as shell-functions can only return numeric values, no strings.
#
#
# Declare an array
# ----------------
#
# arrayname=(a b c)
#
#
# Get an array
# ------------
#
# arraycontent="${arrayname[@]}"
#
# Nota: Calling arrayname alone, will only return first item.
#
#
# Loop over array
# -----------------------
# forEachDo() { arrayname=$1[@] array=("${!arrayname}") kommand=$2; for i in "${array[@]}" ; do "$kommand" "$i"; done }
#
# Example:
# items=("Hello world!" "What a wonderful day." "Couldn't be better." "Ciao!")
# forEachDo items "echo"
#
# Nota:
# http://stackoverflow.com/questions/16461656/bash-how-to-pass-array-as-an-argument-to-a-function
#
#
# Convert array to string
# -----------------------
#
# strg=$( printf "%s" "${arrayname[@]}" )
#
#
#
#
###########################################################
