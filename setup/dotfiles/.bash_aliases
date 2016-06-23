sas() {
    # Requires:
    # pip install pyScss
    # Usage:
    # sas stylefile.scss
    python -m scss < "$1" > "$1.css"
}
setScreenWindowTitleToFilename() {
    echo -e '\033k'$1'\033\\'
}
vimAndSetScreenTitleToFileName() {
    setScreenWindowTitleToFilename $1
    vim $1
}
alias dg='devgen'
alias ..='cd ..'
alias ...='..;..'
alias ....='...;..'
alias .....='....;..'
alias ......='.....;..'
alias ca='cat'
alias cl='clear'
alias diff='colordiff -u'
alias py='python'
alias psy='ps aux|grep python'
alias scd='screen -dRR'
alias scl='screen -ls'
alias scr='screen -r'
alias scs='screen -S'
alias rf='rm -rf'
alias vi='vim'
alias v=vimAndSetScreenTitleToFileName

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

alias ali='cat ~/.bash_aliases'
alias src='. ~/.bashrc; . ~/.bash_aliases;'
