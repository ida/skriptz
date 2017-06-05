fn() {
# Search for files whose names contain
# the passed searchterm.
# Usage: `fn somesearchterm`
    term=$1
    find . -name "*$term*"
}
gr() {
# Search file-contents recursively for
# the passed searchterm.
# Usage: `gr somesearchterm`
    term=$1
    grep -r "$1" .
}
grr() {
# Search file-contents recursively for
# the first passed searchterm in files
# whose names end with the second passed
# searchterm, show the filenames.
# Usage: `grr somesearchterm .css`
    firstterm=$1
    secondterm=$2
    find . -type f -name "*$secondterm" -exec grep -il "$firstterm" {} \;
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
    echo -e '\033k'$1'\033\\'
}
vimAndSetScreenTitleToFileName() {
    setScreenWindowTitleToFilename $1
    vim $1
}
alias dg='devgen'
alias sq='devgen squash'

alias ..='cd ..'
alias ...='..;..'
alias ....='...;..'
alias .....='....;..'
alias ......='.....;..'
alias ca='cat'
alias cl='clear'
alias diff='colordiff -u'
alias l='ls -l'
alias py='python'
alias psy='ps aux|grep python'
alias scd='screen -dRR'
alias scl='screen -ls'
alias scr='screen -r'
alias scs='screen -S'
alias rf='rm -rf'
alias vi='vim'
alias v=vimAndSetScreenTitleToFileName

alias bb='./bin/buildout'
alias bi='./bin/instance fg'
alias bo='buildout -o'
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
alias koma='coma; push'
alias ga='git add'
alias ash='git stash'
alias pop='git stash pop'
alias tag='git tag'
alias tagg='git tag -a `date +%y%m%d%H%M%S` -m "Create annotated tag."'
alias tagp='git push origin --tags'

alias ali='cat ~/.bash_aliases'
alias src='. ~/.bashrc; . ~/.bash_aliases;'
