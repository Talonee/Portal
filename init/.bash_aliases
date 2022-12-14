alias battery='upower -i $(upower -e | grep BAT) | grep --color=never -E "state|to\ full|to\ empty|percentage|capacity"'
alias batterydetail='upower -i $(upower -e | grep BAT)'

alias rsleep='systemctl suspend'
alias hsleep='systemctl hibernate'
alias shutdown='systemctl poweroff'

alias zshark='source ~/Portal/init/.zshrc'
alias zoveride='cat ~/Portal/init/.zshrc > ~/.zshrc'

alias bt1='echo "Activating bluetooth"; sudo systemctl start bluetooth.service'
alias bt0='echo "Deactivating bluetooth"; sudo systemctl stop bluetooth.service'
alias uploc='echo "Updatedb + locate"; sudo updatedb'
alias tdl='xdg-open https://to-do.live.com/tasks/'
alias onedrive='xdg-open https://onedrive.live.com'
alias ethics='xdg-open https://onedrive.live.com/?id=E4A35E02F8A63654%2158566&cid=E4A35E02F8A63654'
alias spotify='xdg-open https://open.spotify.com'
