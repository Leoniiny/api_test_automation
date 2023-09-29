# @Time : 2023/9/29 19:41
# @Author : 雷洋平
# @File : user_login.py
# @Software: PyCharm
# @Function: 用户登陆
from common_layer.api_common import ApiCommon


class UserLogin(ApiCommon):
    # 用户登录
    @classmethod
    def user_login(cls, username, password, verifycode):
        cls.url = cls.host + "/user/login"
        cls.method = "post"
        cls.data = {
            "username": username,
            "password": password,
            "verifycode": verifycode,
        }


if __name__ == '__main__':
    obj = UserLogin()
    obj.user_login("admin", "admin", "0000")
    resp = obj.send_requst()
    rest = resp.text
    print(f"rest 的值为：{rest}")
