

class Normalize(list):

    def __init__(self, text):
        self.normalize_phone(text)

    def normalize_phone(self, text):
        # format
        ## “[+][country code][area code][local code][smaller locales]”
        temp = str(text).split()
        for phone in temp:
            self.append(('prefix', phone[0],
                         'countryCode', phone[1],
                         'areaCode', phone[2:5],
                         'localCode', phone[5:8],
                         'smallCode', phone[8::]))


if __name__ == '__main__':
    text = open('./teleo/phone-numbers-1000.txt', 'r').read()
    normal = Normalize(text)
    print('List items:  {}'.format(normal))




