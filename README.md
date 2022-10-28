# change-neofetch-ascii-logo-daily
changes the ascii art that would usually display your distro's logo form a pool of images you choose, autommaticlly changes every day.

## warning
to use this app you need to change a little bit of configurations in your distro, make sure that you know what is changing before you do so.

## dependencies
you will need to install pillow and tkinter, it's supposed to come with python3 but for me it didn't so i will include it here just in case:
```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```
```
pip3 install tk
```

## installation
first copy this line into your .bashrc located in your home directory at the line before ``` unset rc ```:
```
neofetch='neofetch --ascii /home/path_to_directory_of_app/new_logo.txt'
```

for now you also need to replace the ``` "file_0": "example.jpg" ``` to one of your images, the other ones will be added automaticlly.

finally add ``` 0 0 * * * /usr/bin/python3 /path_to_folder_of_app/change_neofetch_logos/main.py ```
this will make my script run every day changing the logo
