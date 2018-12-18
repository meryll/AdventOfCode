from src.utils import data_provider
import numpy as np
np.set_printoptions(threshold=np.nan)


def clean(data):
    cleaned = []

    for d in data:
        clean = d.replace('\n','')
        clean = clean.replace(' ', '')
        splitted = clean.split('@')
        id = splitted[0]
        coords_size = splitted[1].split(':')
        x_y =list(map(int, coords_size[0].split(',')))
        size =  list(map(int, coords_size[1].split('x')))

        cleaned.append([x_y, size, id])

    return cleaned

def fill(data, arr):

    for d in data:
        # print("d",d)
        x = d[0][0]
        y = d[0][1]

        w  = d[1][0]
        h =  d[1][1]

        # print("----")
        # print(arr[x:x+w, y:y+h])

        arr[x:x + w, y:y + h]+=1

    return arr

def find_id(data, filled):
    size = 1000

    for d in data:

        arr = np.zeros((size, size))
        x = d[0][0]
        y = d[0][1]

        w = d[1][0]
        h = d[1][1]

        arr[x:x + w, y:y + h] += 1

        mul = arr*filled
        if np.array_equal(mul, arr):
            return d[2]

    return None

if __name__ == '__main__':

    data = data_provider.load('../data/day3.txt')
    data = clean(data)

    size = 1000

    arr = np.zeros((size, size))
    filled = fill(data=data, arr=arr)
    more = np.where( filled > 1 )
    print("Overlapping:",more[0].shape)
    print(find_id(data=data, filled=filled))
