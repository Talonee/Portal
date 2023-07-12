#!/usr/bin/zsh

######## Start up ########
#if command -v tmux &> /dev/null && [ -n "$PS1" ] && [[ ! "$TERM" =~ screen ]] && [[ ! "$TERM" =~ tmux ]] && [ -z "$TMUX" ]; then
#  exec tmux new-session -A -s main
#fi

#cd ~/OneDrive/Documents/Github/
source ~/OneDrive/Documents/Github/Portal/init/Mac/.aliases
frog

######## Pomodoro ########
# Requires https://github.com/caarlos0/timer to be installed. 

# Mac setup for pomo
alias pomo="timer 25m && terminal-notifier -message 'Pomodoro'\
        -title 'Work Timer is up! Take a Break 😊'\
        -appIcon '~/Pictures/pumpkin.png'\
        -sound Crystal"
        
alias rest="timer 5m && terminal-notifier -message 'Pomodoro'\
        -title 'Break is over! Get back to work 😬'\
        -appIcon '~/Pictures/pumpkin.png'\
        -sound Crystal"
