# !usr/bin/bash
# Checks for git-diffs in all repos living in the same directory
# and creates a reportfile of it, on elevel above of where this
# script is executed.

# Assumes we are inside of one of the repos' 1st-level-dir,
# and the other repos live in the same dir, as this one does:

fileIsEmpty () { if [[ $( <"$1" ) = '' ]]; then return 1; else return 0; fi; }
inEachFirstDirDo() { for file in *; do if [ -d $file ]; then cd $file; $1; cd ..; fi done; }

checkForDiffs() {
    cd ..
    current_location=$(pwd)
    reportfile_name='git-diff-report.txt'
    reportfile=$current_location/$reportfile_name
    inEachFirstDirDo 'git diff' > "$reportfile"
    fileIsEmpty $reportfile
    if [[ $? == 1 ]]; then echo ':-)'; else echo Not clean, check: $reportfile; fi
}
checkForDiffs
