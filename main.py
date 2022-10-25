#!/usr/bin/python
import os
import json
import change_values_of_num
import create_logo

def change_values_of_files():
    with open('files.json') as json_file:
        data = json.load(json_file)

    current_directory = os.path.dirname(os.path.realpath(__file__))
    all_files_in_folder = os.listdir(current_directory)
    print(all_files_in_folder)

    counter = int(data['date_and_time'][1]['num_to_use_file'])
    if_updated = False

    breakpoint()
    for f in all_files_in_folder:
        print(f)
        if ".jpg" in f:
            to_continue_loop = False
            new_counter = 0
            
            for i in data['files'][0]:
                if f in data['files'][0]["file_"+str(new_counter)]:
                    to_continue_loop = True
                    break
                new_counter = new_counter + 1

            if to_continue_loop == True:
                continue

            if_updated = True
            append_to_json = {"file_"+str(counter+1):f}
            counter = counter + 1
            print(append_to_json)
            data['files'][0].update(append_to_json)

    if if_updated == True:
        with open('files.json', 'w') as fpn:
            data['files'][0].update(append_to_json)
            json.dump(data, fp = fpn, indent=2)
    else:
        print("no files")

change_values_of_files()
change_values_of_num.change_values_of_num()
create_logo.create_logo()
