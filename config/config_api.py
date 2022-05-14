import requests

driver = requests.session()
class Test():

    def post_cms(self,url,data=None,headers=None):
        return driver.post(url=url,data=data,headers=headers)

    def get_cms(self,url,data,headers):
        return driver.get(url=url,params=data,headers=headers)