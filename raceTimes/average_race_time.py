# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
from datetime import datetime, timedelta

file_name = '10k_racetimes.txt'
def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open(file_name, 'rt') as file:
        content = file.readlines()
    return content

def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    lines = get_data()
    data_selected = []
    for line in lines:
        line_splited = line.split('  ')
        filtered_list = [item.lstrip() for item in line_splited if item.strip()]

        line_string = [str(value) for value in filtered_list]
        name_to_check = "Jennifer Rhines"
        pattern = re.compile(r'\b{}\b'.format(re.escape(name_to_check)))

        for string in line_string:
            if re.search(pattern, string):
                data_selected.append(f'{line_string[0]}')
    return data_selected
        

def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    total = timedelta()
    for racetime in racetimes:
        try:
            mins,secs,msecs = re.split(r'[:.]',racetime)
            total+= timedelta(minutes=int(mins),seconds=int(secs), milliseconds=int(msecs))
        except ValueError:
            mins,secs = re.split(r'[:.]',racetime)
            total+= timedelta(minutes=int(mins),seconds=int(secs))
    avg = str(total/len(racetimes))[2:-3]
    return avg

get_average()