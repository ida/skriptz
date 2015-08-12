setScreenWindowTitleToFilename() {
    echo -e '\033k'$1'\033\\'
}
vimAndSetScreenTitleToFileName() {
    setScreenWindowTitleToFilename $1
    vim $1
}
alias vi='vim'
alias vv=vimAndSetScreenTitleToFileName
alias scd='screen -dRR'
alias scl='screen -ls'
alias scs='screen -S'
alias ..='cd ..'
alias ...='cd ../..'
alias rf='rm -rf'
alias ca='cat'
alias cl='clear'
alias py='python'
alias psy='ps aux|grep python'

alias bo='buildout'
alias bi='./bin/instance fg'
alias ibi='./instance/bin/instance fg'
alias boi='buildout; ./bin/instance fg'

alias br='git branch'
alias pull='git pull origin master'
alias push='git push origin master'
alias puff='git push origin forumail'
alias st='git status'
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
alias ga='git add'
alias ash='git stash'
alias pop='git stash pop'

alias ali='cat ~/.bash_aliases'
