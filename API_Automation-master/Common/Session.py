# -*- coding: utf-8 -*-

"""
封装获取cookie方法

"""

import requests,json

from Common import Log,Hash
from Conf import Config

class Session:
    def __init__(self):
        self.config = Config.Config()
        self.log = Log.MyLog()
        self.encrypt = Hash.base()
    def get_session(self, env):
        """
        获取session
        :param env: 环境变量
        :return:
        """
        if env == "debug":
            login_url = 'http://' + self.config.loginHost_debug
            parm = json.loads(self.config.loginInfo_debug)
            sign = self.encrypt.my_md5_encrypt(parm)
            parm["sign"] = sign
            session_debug = requests.session()
            response = session_debug.post(login_url, parm)
            if response.status_code == 200:
                if response.json()["resultCode"] == 200:
                    cookies = response.cookies.get_dict()
                    token = response.json()["data"]["token"]
                    userId = response.json()["data"]["userId"]
                    self.log.debug('【cookies】:%s【token】:%s【userId】:%s'%(cookies,token,userId))
                    return cookies,token,userId
                else:
                    self.log.error('get cookies error, please checkout!!!')
                    return None

        elif env == "release":
            login_url = 'http://' + self.config.loginHost_release
            parm = json.loads(self.config.loginInfo_release)
            sign = self.encrypt.my_md5_encrypt(parm)
            parm["sign"] = sign
            session_debug = requests.session()
            response = session_debug.post(login_url, parm)
            if response.status_code == 200:
                if response.json()["resultCode"] == 200:
                    cookies = response.cookies.get_dict()
                    token = response.json()["data"]["token"]
                    userId = response.json()["data"]["userId"]
                    self.log.debug('【cookies】:%s【token】:%s【userId】:%s'%(cookies,token,userId))
                    return cookies,token,userId

        else:
            print("get cookies error")
            self.log.error('get cookies error, please checkout!!!')
            return None


if __name__ == '__main__':
    ss = Session()
    ss.get_session('debug')