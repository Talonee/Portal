# Before running zsh files, convert read type from Windows to Unix

brew install dos2unix
cd /Users/<your user>/.oh-my-zsh
find . -name " *.sh" | xargs dos2unix -f
find . -name " *.zsh" | xargs dos2unix -f
dos2unix -f themes/robbyrussel.zsh-theme
cd 
dos2unix -f .zshrc
source ~/.zshrc
