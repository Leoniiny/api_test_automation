# @Time : 2023/9/28 20:37
# @Author : 雷洋平
# @File : DoYmal.py
# @Software: PyCharm
# @Function:处理Yaml 文件
import yaml, os


class DoYaml:

    # 获取的是一个yaml文件对象：<__main__.DoYaml object at 0x00000242B214FF48>
    def __init__(self, file_name):
        with open(file_name, encoding="utf8") as f:
            self.content = yaml.load(f, Loader=yaml.FullLoader)

    # 获取yaml返回值中指定的数据【字典类型】:node_name 是节点名。{'account': 'admin', 'pwd': 'admin', 'ver_code': 0}
    def get_node_yaml(self, node_name):
        node_content = self.content.get(node_name)
        return node_content

    # 获取yaml节点下的内容:data_name 是节点下的值。admin
    def get_data_yaml(self, node_name, data_name):
        appoint_content = self.content.get(node_name).get(data_name)
        return appoint_content


if __name__ == '__main__':
    pass
    from util_layer.Dynamic_path import CONFIG_PATH

    woniu_config = os.path.join(CONFIG_PATH, "woniusales_config.yaml")
    obj = DoYaml(woniu_config)
    print(obj)
    print(obj.get_node_yaml(node_name="WN"))
    print(obj.get_data_yaml(node_name="WN", data_name="pwd"))
