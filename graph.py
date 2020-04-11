import csv
import datetime

import numpy as np
import matplotlib.pyplot as plt


WaveType = {'Alpha', 'Beta', 'Gamma', 'Delta', 'Theta'}
ScalpNode = {'TP9', 'AF7', 'AF8', 'TP10'}


def average_brain_reading(data, wave_type: WaveType) -> float:
    average = 0
    indices = []
    num_indices = 0

    for node in ScalpNode:
        indices.append(wave_type + '_' + node)

    for index in indices:
        print(data[index])
        if data[index] != '':
            average += float(data[index])
            num_indices += 1

    if num_indices > 0:
        average = average / num_indices
        return average
    else:
        return 0


with open('data.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        # print(row)
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print(row['TimeStamp'])
            # date_time_str = row[0]
            # date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
            # print('Date:', date_time_obj.date())
            # print('Time:', date_time_obj.time())
            # print('Date-time:', date_time_obj)
            for wave in WaveType:
                print(f'Wave: {wave}, Average: {average_brain_reading(row, wave)}')
            line_count += 1
    print(f'Processed {line_count} lines.')

if __name__ == "__main__":
    pass
