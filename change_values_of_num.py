#!/usr/bin/python
import os
import json
import datetime

def change_values_of_num(amount_of_files):
    current_directory = os.path.dirname(os.path.realpath(__file__))

    json_file = open(current_directory+'/files.json')
    data = json.load(json_file)

    num = int(data['date_and_time'][1]['num_to_use_file'])

    current_time = datetime.datetime.now()
    current_day = current_time.day

    if current_day != data['date_and_time'][0]['date']:
        with open('files.json', 'w') as fpn:
            data['date_and_time'][0]['date'] = current_day

            # if the num of file we want to use is bigger then the amount of images we can use then we circle back to 0
            if amount_of_files <= num+1:
                data['date_and_time'][1]['num_to_use_file'] = 0

            else:
                data['date_and_time'][1]['num_to_use_file'] = num+1
            
            json.dump(data, fp = fpn, indent=2)

    else:
        data['date_and_time'][0]['date'] = current_day
