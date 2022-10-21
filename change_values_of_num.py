#!/usr/bin/python
import os
import json
from datetime import date

def change_values_of_num():
    json_file = open('files.json')
    data = json.load(json_file)

    today = date.today()
    if today.day != data['files'][1]['date']:
        num = int(data['files'][2]['num_to_use_file'])
        length_of_files = len(data['files'][0])
        print(length_of_files)
        print(num)

        with open('files.json', 'w') as fpn:
            data['files'][1]['date'] = today.day

            if length_of_files <= num+1:
                data['files'][2]['num_to_use_file'] = 0

            else:
                data['files'][2]['num_to_use_file'] = num+1
            
            json.dump(data, fp = fpn, indent=2)

change_values_of_num()