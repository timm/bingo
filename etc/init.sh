#!/usr/bin/env bash
# vim: ft=bash ts=2 sw=2 sts=2 et :
hi() { 
  clear
  echo -ne "\033[1;33m"
  figlet -W -f larry3d `basename $PWD`
  tput sgr0 bold
  echo "Short cuts:"; tput setaf 4
  alias | sed 's/alias /  /'
  echo ""
  tput sgr0
}

there() { cd $1; basename `pwd`; }
alias ..='cd ..'
alias ...='cd ../../../'

alias h="history"
alias ls="ls -G"
alias py="python3 -B "
alias vi="nvim -u $here/etc/init.lua"

#--clean -p -c "colorscheme slate" -c "set number" -c "set ts=2 sw=2 sts=2 et" -c "setlocal spell spelllang=en_us" ' 

export BASH_SILENCE_DEPRECATION_WARNING=1
export PATH="$PWD:/opt/homebrew/bin:$PATH"
export PATH="$PWD:/Library/Frameworks/Python.framework/Versions/3.13/bin:$PATH"

EDITOR=vi

PROMPT_COMMAND='echo -ne "🎲 $(git branch 2>/dev/null | grep '^*' | colrm 1 2):";PS1="$(there ..)/$(there .):\!\e[m ▶ "'
hi
echo $here
