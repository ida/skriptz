# !usr/bin/bash
#
# Perform git-actions over several repos at once,
# given, they live in the same directory.
#
# Assumes we are inside of one of a repos' 1st-level-dir,
# and the other repos live in the same dir, as this one does.

strContainsStr () { if [[ "$1" = *"$2"* ]]; then return 1; else return 0; fi }
fileIsEmpty () { if [[ $( <"$1" ) = '' ]]; then return 1; else return 0; fi; }
inEachFirstDirDo() { for file in *; do if [ -d $file ]; then cd $file; $1; cd ..; fi done; }

checkForDiffs() {
# Checks for git-diffs in all repos living in the same directory
# and creates a reportfile of it in the, one level above of where this
# script is executed.
    reportfile_name='git-diff-report.txt'
    reportfile=$basket_lokus/$reportfile_name
    cd $basket_lokus
    inEachFirstDirDo 'git diff' > "$reportfile"
    fileIsEmpty $reportfile
#    if [[ $? == 1 ]]; then echo 'Everythings clean, no diffs :-)'; else echo Not clean, check: $reportfile; fi
}

checkForUnpushedCommits() {
    reportfile_name='git-unpushed-commits-report.txt'
    reportfile=$basket_lokus/$reportfile_name
    echo "
The following repos have commits, waiting to be pushed:
" > "$reportfile"
    cd $basket_lokus
    for file in *; do
        if [ -d $file ]; then
            cd $file
            string=$(git status)
            strContainsStr "${string}" 'Your branch is ahead of '
            if [[ $? == 1 ]]; then echo '    -' $file '
                '>> "$reportfile"; fi
            cd ..
        fi
    done
}
#    inEachFirstDirDo 'git status' > "$reportfile"
#    if [[ $? == 1 ]]; then echo 'Everythings clean, no diffs :-)'; else echo Got diffs, check: $reportfile; fi

main() {
    cd ..
    basket_lokus=$(pwd) # pwd == this location
    checkForDiffs
    checkForUnpushedCommits
}

main
