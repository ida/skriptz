export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

export PATH=$HOME/.local/bin:$JAVA_HOME/bin:$PATH # pip2.7 && jdk-tools

export NVM_DIR=$HOME/.nvm
test ! $(command -v nvm) && . $NVM_DIR/nvm.sh
test ! $(command -v npm) && nvm use 12






#export SDK_PATH=$HOME/.android-sdk-linux # github.com/ida/akriptz/android

# cordova (npm):
#export ANDROID_SDK_ROOT=$SDK_PATH # /.android-sdk-linux/platforms/android-16
#export ANDROID_SDK_ROOT=/usr/lib/jvm/java-11-openjdk-amd64/bin
export ANDROID_SDK_ROOT=$HOME/.androidjs/cache/androidjs-sdk
# COLORS
# ======
#
CYAN='\033[0;36m'
RED='\033[0;31m'
NO_COLOR='\033[0m'


# PROMPT
# ======
#
# stackoverflow.com/questions/3058325
#
# Make prompt look like this:
# username@hostname|gitbranchname Error: errormessage $
#
# Where gitbranchname and errormessage are only shown, if given.
PROMPT_COMMAND='RET=$?;\
  CUSTOM_HOSTNAME=$HOSTNAME;\
  if [[ "$CUSTOM_HOSTNAME" = "localhost"* ]]; then\
    CUSTOM_HOSTNAME=loco;\
  fi;\
  BRANCH="";\
  ERRMSG="";\
  if [[ $RET != 0 ]]; then\
    ERRMSG=" $RET";\
    ERRMSG=" Error:$ERRMSG";\
  fi;\
  if git branch &>/dev/null; then\
    BRANCH=$(git branch 2>/dev/null | grep \* |  cut -d " " -f 2);\
    BRANCH="|$BRANCH";\
  fi;
PS1="$GREEN\u@$CUSTOM_HOSTNAME$CYAN$BRANCH$RED$ERRMSG$NO_COLOR\$ ";'



# STATUSBAR-TITLE IN SCREEN, WHEN NOT EDITING FILE:
# ==========================-----------------------
#
# Set screen window-title to show currently opened file-name or complete path:
# Thanks to Gilles: http://unix.stackexchange.com/questions/6065/gnu-screen-new-window-name-change
if [[ "$TERM" == screen* ]]; then
  screen_set_window_title () {
    local HPWD="$PWD"
    case $HPWD in
      $HOME) HPWD="~";;
# Full path:
#      $HOME/*) HPWD="~${HPWD#$HOME}";;
# Only dirname:
            *) HPWD=`basename "$HPWD"`;;
    esac
    printf '\ek%s\e\\' "$HPWD"
  }
  PROMPT_COMMAND="screen_set_window_title; $PROMPT_COMMAND"
fi

##########################################################################
##########################################################################
##########################################################################
# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# colored GCC warnings and errors
#export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi
