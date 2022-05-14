# # import  sys
# #
# # print(sys.getsizeof(24))
# # print(sys.getsizeof(2400))
# # print(sys.getsizeof(False))
# #
# # import time
# #
# # print(time.time())
# # print(time.localtime(time.time()))
# #
# #
# # import urllib.request
# #
# #
# # print(urllib.request.urlopen('http://www.baidu.com').read())
# #
# #
#
# import requests
#
# s = requests.get('https://www.baidu.com')
# print(s.content)
# print(s.status_code)


lis = [1,2,3,4,5,6,7,8]

ll=lis[-3:-1]
print(ll)