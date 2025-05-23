#!/bin/env bash
me=`basename $PWD`
me=${me^^}

hi() { 
  clear; echo -ne "\033[1;33m"
  figlet -W -f slant "$me"
  tput sgr0 bold; aliases; tput sgr0; }

aliases() {
  echo "Short cuts:"; tput setaf 4
  alias | sed 's/alias /  /'
  echo ""; }

there() { 
  cd $1; basename `pwd`; }

alias ..='cd ..'
alias ...='cd ../../../'
alias h="history"
alias ls="ls -G"
alias py="python3 -B "
alias vi="nvim -u $here/etc/init.lua"

export BASH_SILENCE_DEPRECATION_WARNING=1
export PATH="$PWD:/opt/homebrew/bin:$PATH"
export PATH="$PWD:/Library/Frameworks/Python.framework/Versions/3.13/bin:$PATH"

EDITOR=nvim

PROMPT_COMMAND='echo -ne "${me}@$(git branch 2>/dev/null | grep '\''^*'\'' | colrm 1 2):";PS1="$(there ..)/$(there .):\!\e[m ▶ "'
hi
