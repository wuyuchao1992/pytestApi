# -*- coding: utf-8 -*-

import allure
import pytest

from Params.params import OrderList
from Conf.Config import Config
from Common import Request
from Common import Consts
from Common import Assert


class TestOrderList:

    @pytest.allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('OrderList')
    def test_01(self, action):
        """
            用例描述：验证保理1订单列表搜索筛选功能
        """
        conf = Config()
        data = OrderList()
        test = Assert.Assertions()
        request = Request.Request(action)

        host = conf.host_debug
        req_url = 'http://' + host
        urls = data.url
        params = data.data

        api_url = req_url + urls[0]
        response = request.get_request(api_url,params[0])
        assert test.assert_code(response['code'], 200)
        assert test.assert_body(response['body']['data']['list'][0], 'id',735)
        assert test.assert_time(response['time_consuming'], 300)
        Consts.RESULT_LIST.append('True')

