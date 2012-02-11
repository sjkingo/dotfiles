# don't source for interactive shells
if [[ $- != *i* ]] ; then
    return
fi

source /etc/bashrc

export PS1="\[\033[01;32m\]\u@\h\[\033[01;34m\] \w \$\[\033[00m\] "
export PATH="$PATH:/home/sam/scripts:/home/sam/bin"

# android sdk
export PATH="$PATH:/home/sam/android-sdk-linux/tools:/home/sam/android-sdk-linux/platform-tools"

# history control
export HISTFILESIZE="5000"
export HISTCONTROL="ignoreboth"
export PROMPT_COMMAND="history -a"
shopt -s histappend

# python
if [ -r ~/.pythonrc ] ; then
    export PYTHONSTARTUP=~/.pythonrc
fi

# global commands
alias df="df -h"
alias grep="grep --color"
alias ll="ls -Fhl"
alias lsa="ls -aFhl"
alias rm="rm -i"
alias w="w -f"

# allow minor typos in cd paths
shopt -s cdspell

# redraw the window when returning from a command
shopt -s checkwinsize

# 4M core dumps please
ulimit -c 4000

export PGUSER="postgres"
