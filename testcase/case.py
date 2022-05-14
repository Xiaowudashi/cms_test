import unittest
import json
from config.config_api import Test
from ddt import ddt,file_data

@ddt
class Cms(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.p=Test()

    @file_data(r"E:\cms_test\fileyaml\login.yaml")
    def test01(self,**kwargs):
        url = kwargs["path"]
        data = kwargs["data"]
        headers = kwargs["headers"]
        d = self.p.post_cms(url=url,data=data,headers=headers)
        print(d.text)







if __name__ == '__main__':
    unittest.main()

