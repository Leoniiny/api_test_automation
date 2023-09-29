# @Time : 2023/9/29 20:20
# @Author : 雷洋平
# @File : test_user_login.py
# @Software: PyCharm
# @Function: 用户登录的测试用例
import pytest, allure, os
from business_layer.user_login import UserLogin
from common_layer.result_assertion import ResultAssert


@allure.feature("客服登录")
class Test_UserLogin:
    test_data = [
        ["1、客服登录成功", "admin", "admin", "0000", "login-pass"],
        ["2、客服不输入账号", "", "admin", "0000", "login-fail"],
        ["3、客服不输入密码", "admin", "", "0000", "login-fail"],
        ["4、客服不输入验证码", "admin", "admin", "000", "vcode-error"],
    ]

    @allure.story("客服登录")
    @allure.title("{casename}")
    @pytest.mark.parametrize("casename,username, password, verifycode,expect_retMsg", test_data)
    def test_userlogin(self, casename, username, password, verifycode, expect_retMsg):
        obj = UserLogin()
        obj.user_login(username, password, verifycode)
        self.resp = obj.send_requst()
        rest = self.resp.text
        print(f"rest >>>：{rest}")
        ResultAssert().data_equal(casename, rest, expect_retMsg)


if __name__ == '__main__':
    pytest.main([__file__, "--alluredir=./reporter_layer"])
    os.system('allure generate ./reporter_layer -o ./reporter_layer/report --clean')
