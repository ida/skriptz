fileIsEmpty () { if [[ $( <"$1" ) = '' ]]; then return 1; else return 0; fi; }
inEachFirstDirDo() { for file in *; do if [ -d $file ]; then cd $file; $1; cd ..; fi done; }

checkForDiffs() {
# Assumes we are inside of a repo's 1st-level-dir,
# and the other repos live in the same dir, as this one does:
    cd ..
    current_location=$(pwd)
    reportfile_name='git-diff-report.txt'
    reportfile=$current_location/$reportfile_name
    inEachFirstDirDo 'git diff' > "$reportfile"
    fileIsEmpty $reportfile
    if [[ $? == 1 ]]; then echo ':-)'; else echo Not clean, check: $reportfile; fi
}
checkForDiffs
