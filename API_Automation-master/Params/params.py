# -*- coding: utf-8 -*-

"""
定义所有测试数据

"""
import os
from Params import tools
from Common import Log
log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


def get_parameter(name):
    data = tools.GetPages().get_page_list()
    param = data[name]
    return param

class OrderIndex:
    log.info('解析yaml, Path:' + path_dir + '/Params/Param/OrderIndex.yaml')
    params = get_parameter('OrderIndex')
    url = []
    data = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])

class CreateCa:
    log.info('解析yaml, Path:' + path_dir + '/Params/Param/CreateCa.yaml')
    params = get_parameter('CreateCa')
    url = []
    data = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])

class IndependentContract:
    log.info('解析yaml, Path:' + path_dir + '/Params/Param/IndependentContract.yaml')
    params = get_parameter('IndependentContract')
    url = []
    data = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])

class Index:
    log.info('解析yaml, Path:' + path_dir + '/Params/Param/Index.yaml')
    params = get_parameter('Index')
    url = []
    data = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])

class GetContractList:
    log.info('解析yaml, Path:' + path_dir + '/Params/Param/GetContractList.yaml')
    params = get_parameter('GetContractList')
    url = []
    data = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])

class OrganizationCreate:
    log.info('解析yaml, Path:' + path_dir + '/Params/Param/OrganizationCreate.yaml')
    params = get_parameter('OrganizationCreate')
    url = []
    data = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])