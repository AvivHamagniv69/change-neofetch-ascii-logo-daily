#!/usr/bin/python
import os
import json
import change_values_of_num
import create_logo

def change_values_of_files():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    all_files_in_folder = os.listdir(current_directory)

    with open(current_directory+'/files.json') as json_file:
        data = json.load(json_file)

    counter = int(data['date_and_time'][1]['num_to_use_file'])
    # we only dump data to json if we added a file
    if_updated = False
    counter_for_jpg = 0
    amount_of_files = 0

    for i in all_files_in_folder:
        if ".jpg" in i:
            amount_of_files = amount_of_files + 1

    for f in all_files_in_folder:
        if ".jpg" in f:
            if counter == counter_for_jpg:
                return f, amount_of_files

            counter_for_jpg = counter_for_jpg + 1

    json_file.close()

f, amount_of_files = change_values_of_files()
change_values_of_num.change_values_of_num(amount_of_files)
create_logo.create_logo(f)
