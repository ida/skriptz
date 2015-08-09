fileExists() { if [ -f $1 ]; then return 1; else return 0; fi }
strEqualsStr () { if [ "$1" = "$2" ]; then return 1; else return 0; fi }
strStartswithStr () { if [[ "$1" = "$2"* ]]; then return 1; else return 0; fi }
strContainsStr () { if [[ "$1" = *"$2"* ]]; then return 1; else return 0; fi }
strEndswithStr () { if [[ "$1" = *"$2" ]]; then return 1; else return 0; fi }
forEachDo() { arrayname=$1[@] array=("${!arrayname}") kommand=$2; for i in "${array[@]}" ; do "$kommand" "$i"; done }
###########################################################################
#
# 
# Sticky notes
# ============
# 
# 
# Variable-retrievals to remember
# -------------------------------
#
# last_returned_val=$?
#
# this_script_path=$0
# this_script_realpath=$(readlink -f $0)
#
# execution_location_path=$(pwd)
# execution_location_realpath=$(readlink -f $execution_location)
#
# Thank for getting real to Barry, as cited on:
# https://andy.wordpress.com/2008/05/09/bash-equivalent-for-php-realpath/
#
# 
# Read a file's str into a variable, if file-name exists
# ------------------------------------------------------
# 
# str_of_file=''
# this_script_location=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
# file_path=$this_script_location/README.txt
# fileExists $file_path # This shoud return '1'
# if [[ $? = 1 ]]; then str_of_file=$( <$file_path ); fi
# echo $str_of_file
# 
# 
# Usage
# =====
# 
# Executing this file
# -------------------- 
# 
# You can easily test the commands given in this doc, by uncommenting 
# them and executing this file of the command-line, like:
#
# ./commons.sh 
# 
# If the shell should complain, you aren't allowed to do so, make
# sure it's an executable, by making it executable:
# 
# chmod +x commons.sh 
# 
# 
# Execute functions in this file
# ------------------------------
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
# Hint: This function returns a boolean, either '0' for false,
#       or '1' for true, you can fetch its return with:
#
# last_returned_val=$?
#
# After getting the returned val, one often wants to continue with a condition,
# that takes care, whether furthermore code is to be executed, or not:
#
# if [[ $last_returned_val = 1 ]]       # "1" stands for: "yes", "true", "expression met"
#       then echo 'Met condition, what shall we do now?"
# else                                  # returned val wasn't "1", there's only "0" left as a possibility
#       echo "No, no, no, this is not true!"
# fi                                    # shell's way to say "end of the conditionial part"
#
#
# Shell-basics
# ============
#
# Loop
# ----
# for item in 1 2 3; do echo $item; done
# for item in '1 1 1' '2 2 2' '3 3 3'; do echo $item; done
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
# Call a function
# ---------------
#
# functionName
#
#
# Call a function and pass parameters
# -----------------------------------
#
# functionName argument1 argument2
#
#
# Declare a Condition
# -------------------
#
# if [abcdefgh == ijhklmnop]
#   then echo "How did you make it here? It's impossible."
# else
#   echo "See, I knew it, this can't be true."
# fi
# 
# Nota: Shells always want to hav an explicit declaration, when a 
#       conditions ends, that's "fi" (it's "if" backwards). 
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
# Convert array to string
# -----------------------
#
# strg=$( printf "%s" "${arrayname[@]}" )
#
#
# Loop over array
# -----------------------
#
# forEachDo() { arrayname=$1[@] array=("${!arrayname}") kommand=$2; for i in "${array[@]}" ; do "$kommand" "$i"; done }
#
# Example:
# items=("Hello world!" "What a wonderful day." "Couldn't be better." "Ciao!")
# forEachDo items "echo"
#
# Nota:
# http://stackoverflow.com/questions/16461656/bash-how-to-pass-array-as-an-argument-to-a-function
#
###########################################################
