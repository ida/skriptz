sas() {
# Requires:
# pip install pyScss
# Usage:
# $ sas stylefile.scss

    # Get passed filename:
    filename=$1
    # Remove its extension (here: '.scss'):
    filename=${filename%.*}
    # And let pyScss do the rest:
    python -m scss < "$1" > "${filename}.css"
}
replace() {
# What: Replace one string with another in
# all child-files of the current directory.
# Usage:
# $ replace 'Replace me' 'With this'
    regex=s/$1/$2/g
    echo $regex
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
alias ...='cd ../..'
alias ....='cd ../../..'
alias .....='cd ../../../..'
alias ca='cat'
alias cl='clear'
alias diff='colordiff -u'
alias l='ls -l'
alias fn='find . -name'
alias py='python'
alias psy='ps aux|grep python'
alias scd='screen -dRR'
alias scl='screen -ls'
alias scr='screen -r'
alias scs='screen -S'
alias rf='rm -rf'
alias vi='vim'
alias v=vimAndSetScreenTitleToFileName
alias l='ls -l'
alias bo='buildout'
alias boo='buildout -O'
alias bou='./bin/buildout'
alias bi='./bin/instance fg'
alias boi='bo; bi'
alias boui='bou; bi'

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
