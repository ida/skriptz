prependStrToFile() { sed -i '1i"$1"' $2 } # works if file exists and contains at least one line
forEachDo() { arrayname=$1[@] array=("${!arrayname}") kommand=$2; for i in "${array[@]}" ; do "$kommand" "$i"; done }
fileExists() { if [ -f $1 ]; then return 1; else return 0; fi }
fileIsEmpty () { if [[ $( <"$1" ) = '' ]]; then return 1; else return 0; fi; }
strEqualsStr () { if [ "$1" = "$2" ]; then return 1; else return 0; fi }
strStartswithStr () { if [[ "$1" = "$2"* ]]; then return 1; else return 0; fi }
strContainsStr () { if [[ "$1" = *"$2"* ]]; then return 1; else return 0; fi }
strEndswithStr () { if [[ "$1" = *"$2" ]]; then return 1; else return 0; fi }
now() { now="$(date +%y%m%d%H%M%S)"; echo "${now}"; }
splitStringIntoArray() { IFS=', ' read -a $1 <<< $2; }
# splitStringIntoArray arrayname "${string}"
###############################################################################
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
# THIS_DIR_PATH=$(basename $PWD)
#
# Thanks for getting real to Barry, as cited on:
# https://andy.wordpress.com/2008/05/09/bash-equivalent-for-php-realpath/
#
# Thanks for parental advisory to "cfajohnson":
# http:///www.unix.com/shell-programming-and-scripting/117958-get-parent-directory-file.html
# 
# 
# Read a file's str into a variable, if file-name exists
# ------------------------------------------------------
# 
# str_of_file=''
# file_path=$this_script_realpath/README.txt
# fileExists $file_path # this shoud return '1'
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
# Also possible with absolute path:
#
# /home/someuser/somedir/commons.sh
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
# Execute a shell-script
# ----------------------
# 
# By absolute path:
#
# /home/someuser/somedir/commons.sh
#
# With relative path, prepend './':
#
# ./commons.sh
#
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
# all_array_values="${arrayname[@]}"
#
# all_array_indizi="${!arrayname[@]}"
#
# Nota:
# Calling arrayname alone, will only return first item's val.
#
#
# Get array-items' values and indizi
# ----------------------------------
#
# for index in "${!arrayname[@]}"; do echo "$index ${arrayname[index]}"; done
#
# Thanks to Dennis Williamson:
# http://stackoverflow.com/questions/10586153/split-string-into-an-array-in-bash
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
#
# Split string into an array
# ---------------------------
#
# IFS=', ' read -a arrayname <<< "Python, Go, Rust, Ruby"
# echo "${array[@]}"
#
#
# Convert array to string
# -----------------------
#
# strg=$( printf "%s" "${arrayname[@]}" )
#
#
# Get nth item of array
# ---------------------
#
# item=${@:$n:1}
#
# Note: Replace 'n' with the desired index-position to grab,
# where '1' defines how many items starting from that position,
# are supposed to be returnded, it can be more, if desired.
#
#
# Further reading
# ===============
#
# Some arbitrary sources, I stumbled over and liked:
#
# http://linuxconfig.org/bash-scripting-tutorial
# http://bash.cyberciti.biz/guide/If..else..fi#Number_Testing_Script
# http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-5.html
# http://mywiki.wooledge.org/BashFAQ/100#Extracting_parts_of_strings
# http://shell.cfajohnson.com/
#
###########################################################
