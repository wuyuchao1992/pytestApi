# -*- coding: utf-8 -*-

import allure
import pytest

from Params.params import Index
from Conf.Config import Config
from Common import Request
from Common import Consts
from Common import Assert


class TestIndex:

    @pytest.allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Index')
    def test_01(self, action):
        """
            用例描述：验证首页统计
        """
        conf = Config()
        data = Index()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'http://' + host
        urls = data.url
        params = data.data
        api_url = req_url + urls[0]

        response = request.get_request(api_url,params[0])
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'message', u'请求成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Index')
    def test_02(self, action):
        """
            用例描述：验证首页按年统计门店数据
        """
        conf = Config()
        data = Index()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'http://' + host
        urls = data.url
        params = data.data
        api_url = req_url + urls[1]

        response = request.get_request(api_url,params[1])
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'message', u'请求成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Index')
    def test_03(self, action):
        """
            用例描述：验证首页按指定统计门店数据
        """
        conf = Config()
        data = Index()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'http://' + host
        urls = data.url
        params = data.data
        api_url = req_url + urls[2]

        response = request.get_request(api_url,params[2])
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body'], 'message', u'请求成功')
        assert test.assert_time(response['time_consuming'], 1000)
        Consts.RESULT_LIST.append('True')