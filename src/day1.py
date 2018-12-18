def load_data():
    file_path = "../data/freqs.txt"

    with open(file_path, 'r') as f:
        x = f.readlines()

    numbs = []
    for line in x:
        numbs.append(int(line))

    return numbs


def get_last(data):
    freq = 0

    for d in data:
        freq += d

    return freq

def get_repeat(data):

    repeats = []
    freq = 0
    repeats.append(freq)

    while True:
        for d in data:
            freq += d
            # print("freq",freq)

            if freq in repeats:
                return freq

            repeats.append(freq)


if __name__ == '__main__':

    data = load_data()
    # data = data[:200]
    print(data)
    print("Len",len(data))

    print("Last one",get_last(data))
    print("get repeat",get_repeat(data))