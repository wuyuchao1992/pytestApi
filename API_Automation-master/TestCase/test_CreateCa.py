# -*- coding: utf-8 -*-

import allure
import pytest

from Params.params import CreateCa
from Conf.Config import Config
from Common import Request
from Common import Consts
from Common import Assert


class TestCreateCa:

    @pytest.allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('CreateCa')
    def test_01(self, action):
        """
            用例描述：验证新增企业CA是否成功
        """
        conf = Config()
        data = CreateCa()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'http://' + host
        urls = data.url
        params = data.data

        api_url = req_url + urls[0]
        response = request.post_request(api_url,params[0])

        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'message', u'CA申请信息提交成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('CreateCa')
    def test_02(self, action):
        """
            用例描述：验证是否开启实名
        """
        conf = Config()
        data = CreateCa()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'http://' + host
        urls = data.url
        params = data.data

        api_url = req_url + urls[0]
        response = request.post_request(api_url,params[1])

        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'message', u'实名信息不一致，请检查后重新认证。')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')