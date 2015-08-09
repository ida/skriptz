# !usr/bin/bash
#
# Perform git-actions over several repos at once, given they live in the same
# directory. There, produces two report-files. One is a sum of each repo's
# git-diff, the other is an extraction of 'git status', holding merely the
# names of the repos with unpushed commits. So you know. Buh.
#
# Usage
# -----
#
# Locate into the directory where our repos are living:
#
# cd /path/to/repos-directory
#
# Execute script by its absolute-path:
#
# /path/to/this/script/commons.sh
#
# Or, with relative-path:
#
# ./path/to/this/script/commons.sh
#
# If you get "Permission denied", make this script executable, first:
#
# chmod +x path/to/commons.sh
#
# You might change the following variables' values:

unpushed_commits_report='git-unpushed-commits-report.txt'

diff_report='git-diff-report.txt'


#### Don't change anything after this line, unless you know what you're doing. ####

repos_path=$(readlink -f $(pwd)) # realpath of directory where this script is executed

fileIsEmpty () { if [[ $( <"$1" ) = '' ]]; then return 1; else return 0; fi; }
fileExists() { if [ -f $1 ]; then return 1; else return 0; fi }
inEachFirstDirDo() { for file in *; do if [ -d $file ]; then cd $file; $1; cd ..; fi done; }
strContainsStr () { if [[ "$1" = *"$2"* ]]; then return 1; else return 0; fi }

checkForUnpushedCommits() {
    hasUnpushedCommits='0'
    reportfile=$repos_path/$unpushed_commits_report
    fileExists $reportfile
    if [[ $? == 1 ]]; then rm $reportfile; fi
    echo "
The following repos have commits, waiting to be pushed:
" >> "$reportfile"
    cd $repos_path
    for file in *; do
        if [ -d $file ]; then
            cd $file
            string=$(git status)
            strContainsStr "${string}" 'Your branch is ahead of '
            if [[ $? == 1 ]]; then hasUnpushedCommits='1'; echo '    -' $file '
                '>> "$reportfile"; fi
            cd ..
        fi
    done
    if [[ $hasUnpushedCommits == '1' ]]; then echo There are unpushed commits, check: $reportfile; else echo 'No unpushed commits :-)'; fi
}
checkForDiffs() {
    reportfile=$repos_path/$diff_report
    fileExists $reportfile
    if [[ $? == 1 ]]; then rm $reportfile; fi
    cd $repos_path
    inEachFirstDirDo 'git diff' >> "$reportfile"
    fileIsEmpty $reportfile
    if [[ $? == 1 ]]; then echo 'Everythings clean, no diffs :-)'; else echo There are diffs, check: $reportfile; fi
}
main() {
    checkForUnpushedCommits
    checkForDiffs
}
main

