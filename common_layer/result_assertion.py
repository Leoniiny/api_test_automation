# @Time : 2023/9/29 10:47
# @Author : 雷洋平
# @File : result_assertion.py
# @Software: PyCharm
# @Function: 对响应结果进行断言
# 引入日志
from util_layer.logger import Logger


# 采用继承的方式进行调用
class ResultAssert(Logger):
    # 数据库断言
    @classmethod
    def data_equal(cls, caseid, rest, expt):
        if rest == expt:
            print("测试成功")
            cls.logger.debug(f"{caseid}号，测试通过")
            return True
        else:
            print("测试失败")
            cls.logger.debug(f"{caseid}号，测试失败")
            return False

    @classmethod
    def data_not_equal(cls, caseid, rest, expt):
        if rest != expt:
            print("测试成功")
            cls.logger.debug(f"{caseid}号，测试通过")
            return True
        else:
            print("测试失败")
            cls.logger.debug(f"{caseid}号，测试通过")
            return False


if __name__ == '__main__':
    pass