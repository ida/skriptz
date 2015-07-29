# !usr/bin/bash
#
# Perform git-actions over several repos at once,
# given, they live in the same directory.
#
# Produces reportfiles in this directory:
unpushed_commits_report='git-unpushed-commits-report.txt'
diff_report='git-diff-report.txt'

#
#
# Assumes we are inside of one of a repos' 1st-level-dir,
# and the other repos live in the same dir, as this one does.

strContainsStr () { if [[ "$1" = *"$2"* ]]; then return 1; else return 0; fi }
fileIsEmpty () { if [[ $( <"$1" ) = '' ]]; then return 1; else return 0; fi; }
inEachFirstDirDo() { for file in *; do if [ -d $file ]; then cd $file; $1; cd ..; fi done; }

checkForUnpushedCommits() {
    reportfile=$basket_lokus/$unpushed_commits_report
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
checkForDiffs() {
# Checks for git-diffs in all repos living in the same directory
# and creates a reportfile of it in the, one level above of where this
# script is executed.
    reportfile=$basket_lokus/$diff_report
    cd $basket_lokus
    inEachFirstDirDo 'git diff' > "$reportfile"
    fileIsEmpty $reportfile
    if [[ $? == 1 ]]; then echo 'Everythings clean, no diffs :-)'; else echo There are diffs, check: $reportfile; fi
}

main() {
    cd ..
    basket_lokus=$(pwd) # pwd == this location
    checkForUnpushedCommits
    checkForDiffs
}

main
