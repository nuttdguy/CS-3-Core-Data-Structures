
def sort(text):
    phone_list = list()
    price_list = list()
    key_list = list()
    cost_dict = dict()
    t = text.split('\n')
    t.sort()
    for item in t:
        if item is not '':
            k = item.split(',')
            phone_list.append(k[0])
            # key_list.append(k[0][1:5])      # returns the area code
            price_list.append(k[1])
            region_key = k[0][1:5]

            cost_dict[region_key]
    # temp.sort()
    return key_list


## “[+][country code][area code][local code][smaller locales]”
# 1. locate country code
# 2. locate area code
# 3. locate local code
# 4. locate smaller locales

# dict[country-code + area-code]  DictValue == 'local-code + smaller-locales'
#


# stuff to consider:
# each lines has
## number + price
## if all lines are properly formatted
### can format into




if __name__ == '__main__':
    text = open('./route-costs-100.txt', 'r').read()
    sorted_records = sort(text)
    print('Cost items:  {}'.format(sorted_records))
