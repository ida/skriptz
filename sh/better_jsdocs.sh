#!/bin/bash
#
# Turn comments in js-files into docs.
#
#
# Usage:
#
# bash better_jsdocs.sh somescript.js
#
#
# Example:
#
# If 'somescript.js' look like this:
#
#   function doSthGreat(aVar, anotherVar) {
#       // This function does sth great.
#       // Don't use multiline comments.
#
#       // This comment does not belong to the header, a non-comment-line was in between.
#
#   }
#
#
# You get a file 'somescript.js.md', looking like this:
#   
#   ## doSthGreat aVar anotherVar
#   This function does sth great.
#   Don't use multiline comments.
#

filename="$1"

inFunction=1

comments=()


# For each line of $filename:
while read line; do

#    echo beg $inFunction "$line"

    # Line starts with 'function':
    if [[ "$line" = "function"* ]]; then
        
        # Set inFunction to true:
        inFunction=0;
        
        searchStr='function '
        
        # Remove 'function ' and '{' of line, prepend '## ':
        line=$(echo $line | sed -e "s/function /## /g"); #works
        #line=$("s/$line//function/fantastisch /g"); # works not
        line=$(echo $line | sed -e "s/{//g");
        line=$(echo $line | sed -e "s/(/ /g");
        line=$(echo $line | sed -e "s/)//g");
        line=$(echo $line | sed -e "s/,/ /g");

        # Collect funcName-line:
        comments+=("$line")

        # Add newline:
        comments+=("")

    # Were in a function and line startsWith '//':
    elif [[ $inFunction = '0' && ( "$line" = "//"*) ]]; then

            # Remove '//' of line:
            line=$(
                echo $line | sed -e "s/\/\///g"
            );
            # Collect comment-line:
            comments+=("$line")

    # In a function and not comment, out we go:
    elif [[ $inFunction = '0' && ( ! "$line" = "//"*) ]]; then
        
        # Set inFunction to false:
        inFunction=1

        # Add newline:
        comments+=("")
    
        # Add newline:
        comments+=("")
    
    fi
    
#    echo end $inFunction "$line"

    
done < $filename # for each line

for value in "${comments[@]}"; do echo $value >> "$filename".md ; done
