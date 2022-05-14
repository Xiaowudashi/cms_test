import openpyxl



#打开excel

excel = openpyxl.load_workbook(r'E:\cms_test\fileexcel\cms_login.xlsx')

#打开对应sheet页
sheet = excel['Sheet1']

print(sheet)


#读取excel内容来实现文件驱动自动化的执行，逐行的循环读取excel数据

n = 0
for value in sheet.values:
    n=n+1
    print(n)

    #判断当前行的第一列的值，是否是数字编号
    if type(value[0]) is int:
        #准备需要的测试数据
        #请求参数
        data = value[5]
        #校验字段
        assert_value = value[7]
        #预期结果字段
        expect_value = value[8]
        #如果存在请求头
        if value[4]:
            #存在请求参数
            if value[5]:
                print('存在请求参数')
                dict_data = {
                    'url':value[1]+value[2],
                    #不能直接取字符串需要字典，eval函数将字符串当做有效表达式来求值并返回计算结果
                    #这里直接给headers一个字典值
                    'headers': eval(value[4]),
                    value[6]:eval(value[5])
                }
                print(dict_data)
                print()
            #不存在请求参数
            else:
                print('不存在请求参数')

            #不存在请求参数

        #不存在请求头
        else:
            #存在请求参数
            if value[5]:
                print('存在请求参数')
            #不存在请求参数
            else:
                print('不存在请求参数')

        res = getattr()


    # else:
    #     # 准备需要的测试数据
    #     # 请求参数
    #     data = value[5]
    #     # 校验字段
    #     assert_value = value[7]
    #     # 预期结果字段
    #     expect_value = value[8]
    #     # 如果存在请求头
    #     if value[4]:
    #         # 存在请求参数
    #         if value[5]:
    #             print('存在请求参数')
    #         # 不存在请求参数
    #         else:
    #             print('不存在请求参数')
    #
    #         # 不存在请求参数
    #
    #     # 不存在请求头
    #     else:
    #         # 存在请求参数
    #         if value[5]:
    #             print('存在请求参数')
    #         # 不存在请求参数
    #         else:
    #             print('不存在请求参数')

