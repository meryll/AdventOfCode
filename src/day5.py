from src.utils import data_provider
from string import ascii_lowercase
import copy

def should_explode(letterA, letterB):
    not_the_same = letterA != letterB
    lower_the_same = letterA.lower() == letterB.lower()

    return not_the_same & lower_the_same

def process(data):

    data = list(data)
    prev_letter = data[0]

    i = 1
    while i<len(data):
        current_letter = data[i]

        if should_explode(prev_letter, current_letter):
            del data[i - 1:i + 1]


            if i >= 2:
                prev_letter = data[i - 2]
            else:
                prev_letter: None
            i-=1

        else:
            prev_letter = current_letter
            i+=1

    return len(data)


def get_shortest(data):

    results = {}

    for c in ascii_lowercase:
        copied = copy.deepcopy(data)
        removed = copied.replace(c,'').replace(c.upper(),'')
        result = process(removed)
        results[c] = result


    min_value = min(results, key=lambda k: results[k])
    return results[min_value]

if __name__ == '__main__':

    data = data_provider.load('../data/day5.txt')
    input = data[0]

    # print("Len",process(input))
    print(get_shortest(input))
