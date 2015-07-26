showLastReturnedVal() { last_returned_val=$?; echo $last_returned_val; }

strEqualsStr () { if [ "$1" = "$2" ]; then return 1; else return 0; fi }
strStartswithStr () { if [[ "$1" = "$2"* ]]; then return 1; else return 0; fi }
strContainsStr () { if [[ "$1" = *"$2"* ]]; then return 1; else return 0; fi }
strEndswithStr () { if [[ "$1" = *"$2" ]]; then return 1; else return 0; fi }

showFileStrOfPath() { echo $( <$1 ); }
showFileStrOfPath '/home/uzer/fil.txt'
