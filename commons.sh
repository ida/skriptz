# Reminders
str_of_file=$( <path/to/file )
last_returned_val=$?

# Comparisons
strEqualsStr () { if [ "$1" = "$2" ]; then return 1; else return 0; fi }
strStartswithStr () { if [[ "$1" = "$2"* ]]; then return 1; else return 0; fi }
strContainsStr () { if [[ "$1" = *"$2"* ]]; then return 1; else return 0; fi }
strEndswithStr () { if [[ "$1" = *"$2" ]]; then return 1; else return 0; fi }
# strEndswithStr 'The end.' 'end.'
# if [[ $? = 1]]; then...........

# Loop
forEachDo() { for i in $1; do $2 $i; done }
# forEachDo 'a b c' echo


