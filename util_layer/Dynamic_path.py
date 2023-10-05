# @Time : 2023/9/28 20:06
# @Author : 雷洋平
# @File : Dynamic_path.py
# @Software: PyCharm
# @Function:获取项目的动态路径
import os

# 获取框架的跟目录
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 获取每一层的路径
# 1、工具层绝对路径
UTIL_PATH = os.path.join(PROJECT_PATH, "util_layer")
# 2、公共层绝对路径
COMMON_PATH = os.path.join(PROJECT_PATH, "common_layer")
# 3、业务层绝对路径
BUSINESS_PATH = os.path.join(PROJECT_PATH, "business_layer")
# 4、文件配置层绝对路径
CONFIG_PATH = os.path.join(PROJECT_PATH, "config_layer")
# 5、数据层绝对路径
DATA_PATH = os.path.join(PROJECT_PATH, "data_layer")
# 6、测试用例层绝对路径
CASE_PATH = os.path.join(PROJECT_PATH, "case_layer")
# 7、用例运行层绝对路径
OPRATION_PATH = os.path.join(PROJECT_PATH, "operational_layer")
# 8、测试报告层绝对路径
REPORT_PATH = os.path.join(PROJECT_PATH, "reporter_layer")
# 9、测试报告层绝对路径
LOGGING_PATH = os.path.join(PROJECT_PATH, "logging_layer")

if __name__ == '__main__':
    pass
    print(PROJECT_PATH)
    print(UTIL_PATH)
    print(COMMON_PATH)
    print(BUSINESS_PATH)
    print(f"CONFIG_PATH >>>{CONFIG_PATH}")
    print(DATA_PATH)
    print(CASE_PATH)
    print(OPRATION_PATH)
    print(REPORT_PATH)
    print(LOGGING_PATH)
