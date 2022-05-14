import unittest
import os
import time
from units.HTMLTestRunner3_New import HTMLTestRunner
from units.mail3 import SendMail

#报告生成与邮件发送


#拿到项目路径
p = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())))
print(p)
#拿到用例路径
testcase_path=os.path.join(os.path.abspath(os.path.dirname(os.getcwd())),'testcase')
print(testcase_path)

#项目存放报告路径
report_path = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())),'report')
print(report_path)

new = time.strftime('%y-%m-%d %H-%M-%S')
file_name = report_path + '/' + str(new) + 'report.html'

def bg(file):
    d = unittest.defaultTestLoader.discover(start_dir=testcase_path,pattern=file)
    f = open(file_name,'wb')
    r = HTMLTestRunner(stream=f,description='用例执行情况',title='cms接口自动化测试',tester='吴旭晨')
    r.run(d)


def yj():
    ff = SendMail(send_msg=file_name,attachment=file_name)
    ff.send_mail()


if __name__ == '__main__':
    bg('case.py')