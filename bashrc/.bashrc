#export OCIO= ... /imageworks-OpenColorIO-Configs-0bb079c/spi-anim/config.ocio

#export OCIO_ACTIVE_DISPLAYS="sRGB"
#export OCIO_ACTIVE_VIEWS="Film:Log:Raw"

alias sourceme='source ~/.bashrc'
alias editme='gedit ~/.bashrc&'
alias hfx='/opt/hfs17.5.425/bin/houdini'
alias freqs='watch -n 1 "cat /proc/cpuinfo | grep "MHz"|sort -r"'
alias tlog='tail -f /var/log/syslog'  
alias tlog1='gnome-terminal --window-with-profile=tail && tlog'
alias torstop='sudo service tor stop'
alias updateall='sudo apt-get update && sudo apt-get dist-upgrade'
alias meminfo='sudo dmidecode -t 17'

alias mt='mate-terminal'
alias mtl="mt --window-with-profile=log -e 'tail -f /var/log/syslog' "
alias gpu='watch nvidia-smi'
alias br='brave-browser'
alias cdd='cd ~/Documents'
alias cdw='cd ~/Downloads'
alias nvs='nvidia-settings'

alias rcuda='sudo rmmod nvidia_uvm && sudo modprobe nvidia_uvm'

alias lsh='ls -lh'
alias lsd='ls -alt -r -h'
alias jpg2pdf="ls -1 ./*jpg | xargs -L1 -I {} img2pdf {} -o {}.pdf"
alias png2pdf="ls -1 ./*png | xargs -L1 -I {} img2pdf {} -o {}.pdf"
alias pdfs2pdf="pdftk *.pdf cat output combined.pdf"
alias nospace="for file in *; do mv "$file" `echo $file | tr ' ' '_'` ; done"
alias dff="df -h|grep nvme && df -h|grep sd"

alias addswap="sudo swapon /mnt/hdd3tb/swapfile"

h18() { /opt/houdini/hfs18.$@/bin/houdini -n; }#