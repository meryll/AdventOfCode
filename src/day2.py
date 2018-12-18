from src.utils import data_provider

def clean(data):
    cleaned = []
    for d in data:
        cleaned.append(d.replace('\n',''))

    return cleaned

def get_repeats(id):
    distinc_letters = set(id)
    dict = {i: 0 for i in distinc_letters}

    for letter in id:
        dict[letter] +=1

    twice = any(v ==2 for v in dict.values())
    triple = any(v ==3 for v in dict.values())
    print("Twice, triple",twice,triple)
    return twice, triple

def calc(data):

    twice = 0
    triple = 0

    for id in data:
        t2, t3 = get_repeats(id)

        if t2: twice+=1
        if t3: triple+=1

    print("--------")
    print("Twice, triple", twice, triple)
    return twice*triple

def compare(id1, id2):
    compared = []
    the_same = []
    for i in range(len(id1)):
        same = int(id1[i]==id2[i])
        compared.append(int(not same))
        if same:
            the_same.append(id1[i])


    print("compared",compared)
    return sum(compared)==1, the_same



def get_the_same(data):

    for i in range(len(data)):
        for j in range(len(data)):
            if i==j: continue

            the_same, letters = compare(data[i],data[j])
            if the_same:
                return ''.join(letters)




if __name__ == '__main__':

    data = data_provider.load('../data/ids.txt')
    data = clean(data)
    print(data)
    # print(calc(data))
    print(get_the_same(data))

