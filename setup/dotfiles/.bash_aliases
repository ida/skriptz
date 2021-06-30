append() {
# append whatever you need to write file.txt
	array=( "$@" )
	lastArg="${@: -1}" # bash only
	unset "array[${#array[@]}-1]" # remove last item
    echo "${array[@]}" >> $lastArg
}
doing() {

test ! -f ~/DOING.txt && touch ~/DOING.txt || (

  if [[ $@ != '' ]] ; then append "$@" ~/DOING.txt; fi

  clear

  cat ~/DOING.txt

)

}
doo() {
test ! -f ~/DOING.txt && touch ~/DOING.txt || (

  if [[ $@ != '' ]] ; then prepend "$@" ~/DOING.txt; fi

  clear

  cat ~/DOING.txt

)


}

doon() {
removeFirstLine ~/DOING.txt
clear
cat ~/DOING.txt
}

donn() {
# echo Take last line of DOING.txt, add it to CHANGELOG, commit changes with last line as commit-message. Rmove last line of DOING.txt.
lastLine=$(getLastNthLineOfFile 1 ~/DOING.txt)
echo lastLine is $lastLine
#insertAttNthLineToFile "* $lastLine" 3 CHANGELOG.md
#insertAttNthLineToFile "..........." 3 CHANGELOG.md
#insertAttNthLineToFile "..........." 3 CHANGELOG.md
git add .
git commit -m "$lastLine"
removeLastLine ~/DOING.txt
cat ~/DOING.txt
}
fn() {
# Search for files whose names contain the passed searchterm.
# Usage: `fn somesearchterm`
    find . -name "*$1*"
}
getNthLineOfFile(){

    head -$1 $2 | tail -1

}
getLastNthLineOfFile(){

    tail -$1 $2 | head -1

}
getValueOfJsonFile(){ # Usage: getValueOfJsonFile version package.json

    versionline=$(grep $1 $2)

    IFS='"' read -ra arrayname <<< "$versionline"

    for index in "${!arrayname[@]}"; do
        if [[ $index == 3 ]] ; then
            echo "${arrayname[index]}"
        fi
    done


}
getVersionOfPackageJson(){

    versionline=$(grep version package.json)

    IFS='"' read -ra arrayname <<< "$versionline"

    for index in "${!arrayname[@]}"; do
        if [[ $index == 3 ]] ; then
            version="${arrayname[index]}"
        fi
    done

    echo version is \'$version\'

}
gr() {
# Search this directory recursively for the passed searchterm, ignore upper- and lowercase differentiation.
# Usage: `gr somesearchterm`
    grep -ir "$1" .
}
grx() {
# Same as `gr`, but exclude directories named 'tests' and files ending with '.pyc'.
    find . -type f ! -path "./*bak*" ! -path "./tests*" ! -path "*.pyc" -exec grep -ir "$1" {} \;
}
grr() {
# Search term only in files with certain extension:
#     grr somesearchterm .css
# Optionally exclude a directory:
#     grr somesearchterm .css tests
    firstterm=$1
    secondterm=$2
    thirdterm=$3
#    find . -type f -name "*$secondterm" -exec grep -il "$firstterm" {} \;
    find . -type f -name "*$secondterm" -not -path "./$thirdterm/*" -exec grep -il "$firstterm" {} \;
}
insertAttNthLineToFile() {
# Usage: 'some text' 3 file.txt
    sed -i $2i"$1" $3
}
prepend() {
# prepend "some string" file.txt

# If file does not exist or is empty, write str, otherwise prepend str:
if [[ ! -f $2 ]] || [[ $( <"$2" ) == '' ]]; then echo $1 > $2; else sed -i 1i"$1" $2; fi
}
pushToWhateverIsAvailable() {
git push origin master &> /dev/null
if [[ $? != 0 ]]; then git push origin main; fi
}
readyou() { # Generate a READYOU.md from package.json:

    wallju=$(getValueOfJsonFile name package.json)
    echo "# $wallju" > READYOU.md
    echo "" >> READYOU.md

    wallju=$(getValueOfJsonFile description package.json)
    echo "$wallju" >> READYOU.md
    echo "" >> READYOU.md
    echo "" >> READYOU.md

    wallju=$(getValueOfJsonFile license package.json)
    echo "# License" >> READYOU.md
    echo "" >> READYOU.md
    echo "$wallju" >> READYOU.md
    echo "" >> READYOU.md
    echo "" >> READYOU.md

    wallju=$(getValueOfJsonFile repository package.json)
    echo "# Contact" >> READYOU.md
    echo "" >> READYOU.md
    echo "For questions, suggestions and bug-reports, please open an issue:" >> READYOU.md
    echo "" >> READYOU.md
    echo "$wallju"/issues/new >> READYOU.md
    echo "" >> READYOU.md
    echo "" >> READYOU.md

    wallju=$(getValueOfJsonFile repository package.json)
    echo "# Repository" >> READYOU.md
    echo "" >> READYOU.md
    echo "$wallju" >> READYOU.md
    echo "" >> READYOU.md
    echo "" >> READYOU.md



}
replace() {
# What: Replace one string with another in
# all child-files of the current directory.
# Usage:
# $ replace 'Replace me' 'With this'||
    regex=s/$1/$2/g
    find ./ -type f -exec sed -i "$regex" {} \;
}
removeFirstLine() {
    sed -i '1d' $1
}
removeLastLine() {
    sed -i '$d' $1
}
setScreenWindowTitleToFilename() {
    filename=$(basename $1)
    echo -e '\033k'$filename'\033\\'
}
vimAndSetScreenTitleToFileName() {
    setScreenWindowTitleToFilename $1
    vim $1
}
alias ly='lynx localhost:3000'
alias ff='firefox'
alias ff='firefox'
alias dg='devgen'
alias sq='devgen squash'
alias ap='append'
alias pp='prepend'
alias ..='cd ..'
alias ...='..;..'
alias ....='...;..'
alias .....='....;..'
alias ......='.....;..'
alias ca='cat'
alias cl='clear'
alias he='head -n42'
alias l='ls -l'
alias rmf=removeFirstLine
alias rml=removeLastLine
alias rf='rm -rf'
alias vi='vim'
alias v=vimAndSetScreenTitleToFileName
alias :wq='exit'

alias py='python'
alias psy='ps aux|grep python'

alias scd='screen -dRR'
alias scl='screen -ls'
alias scr='screen -r'
alias scs='screen -S'
sck() {
    screen -X -S $1 quit
}


alias bb='./bin/buildout'
alias bi='./bin/instance fg'
alias bil='bi > instance_output.txt 2>&1'
alias bo='buildout -o'
alias bol='buildout  > build_output.txt 2>&1 ; cat build_output.txt'
alias boi='bo; bi'
alias boo='buildout -O'
alias bu='bo -U'
alias bui='bu; bi'

alias br='git branch'
alias pull='git pull --rebase origin master'
alias push=pushToWhateverIsAvailable
alias puff='git push origin forumail'
alias st='git status'
alias sd='git status'
alias di='clear; git diff'
alias ch='git checkout'
alias chb='git checkout -b'
alias chm='git checkout master'
alias chf='git checkout forumail'
alias rs='git reset --hard'
alias rsf='git checkout HEAD --'
alias lo='git log'
alias co='git commit -m'
alias coa='git commit -am'
alias com='git commit -m "up"'
alias coma='git commit -am "up"'
alias cos='coma; sq'
alias koma='coma; push'
alias ga='git add'
alias ash='git stash'
alias pop='git stash pop'
alias tag='git tag'
alias tagg='git tag -a `date +%y%m%d%H%M%S` -m "Create annotated tag."'
alias tagp='git push origin --tags'

alias ali='cat ~/.bash_aliases'
alias alli='cat ~/.bash_aliases | less'
alias src='. ~/.bashrc; . ~/.bash_aliases'
