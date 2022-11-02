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
   
    for f in all_files_in_folder:
        if ".jpg" in f:
            to_continue_loop = False
            # the written file were currently checking
            new_counter = 0

            # this loop checks if the file is already written, if it is, we mark to_continue_loop as true and continue to the next file
            if len(data['files'][0]) != 0:
                for i in data['files'][0]:
                    if f in data['files'][0]["file_"+str(new_counter)]:
                        to_continue_loop = True
                        break
                    new_counter = new_counter + 1

            if to_continue_loop == True:
                continue

            if_updated = True
            append_to_json = {"file_"+str(counter):f}
            counter = counter + 1
            data['files'][0].update(append_to_json)

    if if_updated == True:
        with open('files.json', 'w') as fpn:
            data['files'][0].update(append_to_json)
            json.dump(data, fp = fpn, indent=2)
        fpn.close()
    # else:
        # print("no files")

    json_file.close()

change_values_of_files()
change_values_of_num.change_values_of_num()
create_logo.create_logo()
