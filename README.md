# change-neofetch-ascii-logo-daily
changes the ascii art that would usually display your distro's logo form a pool of images you choose, autommaticlly changes every day.

## warning
to use this app you need to change a little bit of configurations in your distro, make sure that you know what is changing before you do so.

## dependencies
you will need to install pillow:
```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```

## installation
copy these commands into your .bashrc:

```
neofetch='neofetch --ascii /home/[path_to_directory_of_app]/new_logo.txt'
```
also add
```
/usr/bin/python3 /path_to_script/main.py [size_of_image]
``` 
