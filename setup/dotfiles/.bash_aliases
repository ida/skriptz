fn() {
# Search for files whose names contain the passed searchterm.
# Usage: `fn somesearchterm`
    find . -name "*$1*"
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
pytojs() {
# Usage:
# pytojs inputfile.pyjs
# Where the extension (here: 'pyjs') can be anything.
# Results in a converted js-file within the same directory.
python /home/ida/repos/github/ida/skriptz/py/pytojs/main.py $1
}
sas() {
# Requires:
# pip install pyScss
# Usage:
# sas stylefile.scss
    # Get passed filename:
    filename=$1
    # Remove its extension (here: '.scss'):
    filename=${filename%.*}
    # (OR: `basename hugo.scss .scss` ---> hugo)
    # And let pyScss do the rest ('-C' means 'do not minify'):
    python -m scss -C < "$1" > "${filename}.css"
}
replace() {
# What: Replace one string with another in
# all child-files of the current directory.
# Usage:
# $ replace 'Replace me' 'With this'
    regex=s/$1/$2/g
    find ./ -type f -exec sed -i "$regex" {} \;
}
setScreenWindowTitleToFilename() {
    filename=$(basename $1)
    echo -e '\033k'$filename'\033\\'
}
vimAndSetScreenTitleToFileName() {
    setScreenWindowTitleToFilename $1
    vim $1
}
alias ff='firefox'
alias dg='devgen'
alias sq='devgen squash'
alias ..='cd ..'
alias ...='..;..'
alias ....='...;..'
alias .....='....;..'
alias ......='.....;..'
alias ca='cat'
alias cl='clear'
alias l='ls -l'
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
alias push='git push origin master'
alias puff='git push origin forumail'
alias st='git status'
alias sd='git status'
alias di='git diff'
alias ch='git checkout'
alias chb='git checkout -b'
alias chm='git checkout master'
alias chf='git checkout forumail'
alias rs='git reset --hard'
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
alias src='. ~/.bashrc; . ~/.bash_aliases;'
