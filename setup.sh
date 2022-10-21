#!/usr/bin/env bash

if [ $(id -u) != 0 ]; then
    echo "please run as root/sudo!"
    exit
fi

echo "you only need to run this once! after that dont run this"

echo ~/aliases.list >> ${HOME}/.bashrc
echo alias neofetch=\'neofetch --ascii ${PWD}/new_logo.txt\' > ${HOME}/.aliases.list