# @Time : 2023/9/29 21:07
# @Author : 雷洋平
# @File : driven.py
# @Software: PyCharm
# @Function:用例运行层
import os
import time

import pytest


if __name__ == '__main__':
    pytest.main()
    time.sleep(2)
    # 这里日志的输出路径要和 pytest.ini 中的配置文件一致
    os.system('allure generate ../reporter_layer -o ../reporter_layer/allure_report --clean')
