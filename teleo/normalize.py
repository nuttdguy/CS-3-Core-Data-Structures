

# class Normalize(dict):

    # def __init__(self, text):
        # self.normalize_phone(text)
        # self.normalize_cost(text)



    # def normalize_phone(self, text):
    #     # format
    #     ## “[+][country code][area code][local code][smaller locales]”
    #     temp = str(text).split()
    #     for phone in temp:
    #         self.append(('prefix', phone[0],
    #                      'countryCode', phone[1],
    #                      'areaCode', phone[2:5],
    #                      'localCode', phone[5:8],
    #                      'smallCode', phone[8::]))

    # def normalize_cost(self, text):
    #     temp = str(text).rsplit('\n')
    #
    #     for cost in temp:
    #         if cost is not '':
    #             cost_list = cost.split(',')
    #             phone = cost_list[0]
    #             price = cost_list[1]
    #             text = [['prefix', phone[0]],
    #                     ['countryCode', phone[1]],
    #                     ['areaCode', phone[2:5]],
    #                     ['localCode', phone[5:8]],
    #                     ['smallCode', phone[8::]]]
    #             self[price] = text


# if __name__ == '__main__':
#     # text = open('./teleo/phone-numbers-1000.txt', 'r').read()
#     # normal = Normalize(text)
#     # print('List items:  {}'.format(normal))
#
#     text = open('./route-costs-10.txt', 'r').read()
#     normalCost = Normalize(text)
#     print('Cost items:  {}'.format(normalCost))




