#!/usr/bin/python
import os
import json
from datetime import date

def change_values_of_num():
    current_directory = os.path.dirname(os.path.realpath(__file__))

    json_file = open(current_directory+'/files.json')
    data = json.load(json_file)

    today = date.today()
    if today.day != data['date_and_time'][0]['date']:
        num = int(data['date_and_time'][1]['num_to_use_file'])
        length_of_files = len(data['files'][0])

        with open('files.json', 'w') as fpn:
            data['date_and_time'][0]['date'] = today.day

            if length_of_files <= num+1:
                data['date_and_time'][1]['num_to_use_file'] = 0

            else:
                data['date_and_time'][1]['num_to_use_file'] = num+1
            
            json.dump(data, fp = fpn, indent=2)
