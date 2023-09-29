# @Time : 2023/9/29 8:05
# @Author : 雷洋平
# @File : logger.py
# @Software: PyCharm
# @Function: 配置日志文件
import logging.config
import os.path
from util_layer.Dynamic_path import LOGGING_PATH


class Logger:
    loger_path =os.path.join(LOGGING_PATH,"logger.ini")
    # 读取配置文件
    logging.config.fileConfig(loger_path)

    # 获取配置文件中的记录器
    logger =logging.getLogger("woniusales")


if __name__ == '__main__':
    pass
    obj = Logger()
    obj.logger.debug("测试debug 是否成功！！！！")

