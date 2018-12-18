from src.utils import data_provider
import numpy as np
from datetime import datetime
import operator
np.set_printoptions(threshold=np.nan)

def clean(data):
    cleaned = []

    for d in data:
        clean = d.replace('\n','')
        clean = clean.replace('[', '')
        clean = clean.replace(']', '')

        splitted = clean.split(' ')

        date_time = ' '.join(splitted[:2])
        dt = datetime.strptime(date_time, '%Y-%m-%d %H:%M')
        label = ' '.join(splitted[2:])

        id = None
        if '#' in label:
            id = int(label.split('#')[1][:4])


        cleaned.append([dt, id, label])

    cleaned.sort()
    return cleaned

WAKES_UP = 'wakes up'
FALLS_ASLEEP = 'falls asleep'

def find_max_overlap(data):

    arr = get_overlap_arr(data)
    max_index = np.where(arr == max(arr))[0]
    return max_index

def find_max_count(data):
    arr = get_overlap_arr(data)
    arr_max = max(arr)
    max_index = np.where(arr == arr_max)[0]
    return max_index, arr_max

def get_overlap_arr(data):
    fixed_size = 60
    arr = np.zeros((fixed_size))

    for d in data:
        arr[d[0]:d[1]] += 1

    return arr

def prepare(data):

    last_guard = None
    last_fall_asleep = None
    guards_dict = {}
    minutes_dict = {}

    for d in data:

        if d[1]:
            last_guard = d[1]
            last_fall_asleep = None

            if last_guard not in guards_dict.keys():
                minutes_dict[last_guard] = []
                guards_dict[last_guard]=0

        if d[2] == FALLS_ASLEEP:
            last_fall_asleep = d[0]


        if d[2] == WAKES_UP:
            diff = d[0]-last_fall_asleep
            minutes_after = (diff.seconds/60)
            minute_asleep = last_fall_asleep.minute
            minute_wokeup = d[0].minute

            minutes_dict[last_guard].append((minute_asleep, minute_wokeup))

            last_fall_asleep = None
            guards_dict[last_guard] +=(minutes_after)

    return guards_dict, minutes_dict

def most_recurrent(minutes_dict):

    most_id = None
    most_count = 0
    most_minute = 0

    for k, v in minutes_dict.items():
        max_index, max_count = find_max_count(v)
        if max_count>most_count:
            most_count=max_count
            most_minute = max_index
            most_id=k

    return most_id* most_minute


def find(guards_dict, minutes_dict):
    max_id = max(guards_dict.items(), key=operator.itemgetter(1))[0]
    minutes = minutes_dict[max_id]
    minute_max = find_max_overlap(minutes)
    return max_id * minute_max


if __name__ == '__main__':

    data = data_provider.load('../data/day4.txt')
    data = clean(data)
    guards_dict, minutes_dict = prepare(data)

    print(find(guards_dict, minutes_dict))
    most_recurrent(minutes_dict)