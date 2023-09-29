# @Time : 2023/9/29 9:57
# @Author : 雷洋平
# @File : api_common.py
# @Software: PyCharm
# @Function: 接口公共调用层
import requests, json, os,jsonpath
from util_layer.logger import Logger
from util_layer.Dynamic_path import *
from util_layer.DoYmal import DoYaml

# 获取项目配置文件
file = os.path.join(CONFIG_PATH, "woniusales_config.yaml")


class ApiCommon(Logger):
    # 声明一个全局的session对象。
    session = requests.session()
    # 获取项目被测系统的host
    host = DoYaml(file).get_data_yaml(node_name="WN", data_name="host")
    url = None
    method = None
    headers = None
    params = None
    data = None
    json = None
    files = None
    resp = None

    # 发送请求
    @classmethod
    def send_requst(cls, **kwargs):
        if kwargs.get('url') is None:
            kwargs['url'] = cls.url
        if kwargs.get('method') is None:
            kwargs['method'] = cls.method
        if kwargs.get('headers') is None:
            kwargs['headers'] = cls.headers
        if kwargs.get('params') is None:
            kwargs['params'] = cls.params
        if kwargs.get('data') is None:
            kwargs['data'] = cls.data
        if kwargs.get('json') is None:
            kwargs['json'] = cls.json
        if kwargs.get('files') is None:
            kwargs['files'] = cls.files

        cls.logger.info('#######################################################################')
        cls.resp = cls.session.request(**kwargs)
        cls.logger.info(f'接口请求的url是: {cls.resp.url}')
        cls.logger.info('响应状态码是: {}'.format(cls.resp.status_code))
        cls.logger.info('响应结果是: {}'.format(cls.resp.text))
        cls.logger.info('#######################################################################' + "\n\n")
        return cls.resp

    # 处理返回结果
    @classmethod
    def processing_result(cls,rest,jsonpath_express,index=0):
        if rest != '':
            try:
                cls.logger.info('#######################################################################')
                resp_dict = json.loads(rest)  # 将json格式的字符串转换成字典
                print(f"rest 的type 类型为：{type(rest)}")
                if index < 0:
                    res = jsonpath.jsonpath(resp_dict, jsonpath_express)
                    cls.logger.info('通过【{}】提取到的结果是:{}'.format(jsonpath_express, res))
                    cls.logger.info('#######################################################################' + "\n\n")
                    return res
                else:
                    res = jsonpath.jsonpath(resp_dict, jsonpath_express)[index]
                    cls.logger.info('通过【{}】提取到的结果是:{}'.format(jsonpath_express, res))
                    cls.logger.info('#######################################################################' + "\n\n")
                    return res
            except Exception as e:
                cls.logger.debug('从响应中通过【{}】提取是出现了异常:{}'.format(jsonpath_express, e))
                cls.logger.info('#######################################################################' + "\n\n")


if __name__ == '__main__':
    pass
    obj = ApiCommon()
    print(f"host >>>：{obj.host}")
    data = {
        "username": "admin",
        "password": "admin",
        "verifycode": "0000",
    }
    resp = obj.send_requst(method="post",url = obj.host + "/user/login",data=data)
    rest = resp.text
    # obj.processing_result(jsonpath_express="login-fail")
