

def sort(text):
    temp = list()
    t = text.split('\n')
    for item in t:
        k = item.split(',')
        temp.append(k)
    temp.sort()
    return temp











if __name__ == '__main__':
    text = open('./route-costs-10.txt', 'r').read()
    sorted_records = sort(text)
    print('Cost items:  {}'.format(sorted_records))