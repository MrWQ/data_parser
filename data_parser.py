#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/29 14:55 
# @Author  : wangqiang 
# @File    : data_parser.py
# @Project : data_parser
# @Python  : 3.7.1
import re
import demjson
from lxml import etree


class DataParser:
    def __init__(self, input_string):
        self.input_string = input_string

    def init_input(self):
        """
        预处理输入的数据
        :return:
        """
        pass

    def parse_re(self, pat):
        """
        解析正则
        :param pattren:
        :return:
        """
        pattern = re.compile(pat, re.S)
        try:
            results = []
            results_re = re.findall(pattern, self.input_string)
            for i in results_re:
                if isinstance(i, str):
                    results.append(i.strip().replace("'", '').replace('"', ''))
        except Exception as e:
            results = e
        return results

    def parse_xpath(self, xpath):
        """
        解析xpath
        :param xpath:
        :return:
        """
        try:
            results = []
            html = etree.HTML(self.input_string)
            html_data = html.xpath(xpath)
            for i in html_data:
                results.append(i.text.strip())
        except Exception as e:
            results = e
        return results

    def parse_dict(self, dict_path):
        results = []
        try:
            input_dict = demjson.decode(self.input_string)
        except Exception as e:
            e = str(e) + "\n可以试试使用正则"
            return e
        if isinstance(input_dict, dict):
            try:
                get_data = input_dict[dict_path]
                results.append(get_data)
                # exec_str = "get_data = input_dict[dict_path]"
            except:
                pass
        elif isinstance(input_dict, list):
            for data_dic in input_dict:
                try:
                    get_data = data_dic[dict_path]
                    results.append(get_data)
                except:
                    pass
        else:
            results = "不能识别"
        return results


if __name__ == '__main__':
    a = '{a:1, b:2, "c":3, "d":"4"},{a:"a", "c":"c"}'
    obj = DataParser(a)
    c = obj.parse_re("a:(.*?),")
    print(c)
