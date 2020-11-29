#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/29 16:17 
# @Author  : wangqiang 
# @File    : index.py
# @Project : data_parser
# @Python  : 3.7.1
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial
from data_parser import DataParser
import data_parser_ui


def parse_re(ui):
    input_string = ui.textEdit.toPlainText()
    input_pattern = ui.lineEdit.text()
    if not input_string or not input_pattern:
        output_str = "输入数据和正则表达式"
        ui.textEdit_2.setText(output_str)
        return
    output = DataParser(input_string).parse_re(input_pattern)
    output_str = ""
    if isinstance(output, str):
        output_str = output
    elif isinstance(output, list):
        for i in output:
            output_str = output_str + str(i) + "\n"
    else:
        output_str = "未知错误1"
    ui.textEdit_2.setText(output_str)


def parse_xpath(ui):
    input_string = ui.textEdit.toPlainText()
    input_xpath = ui.lineEdit_2.text()
    if not input_string or not input_xpath:
        output_str = "输入数据和xpath"
        ui.textEdit_2.setText(output_str)
        return
    output = DataParser(input_string).parse_xpath(input_xpath)
    output_str = ""
    if isinstance(output, str):
        output_str = output
    elif isinstance(output, list):
        for i in output:
            output_str = output_str + str(i) + "\n"
    else:
        output_str = "未知错误2"
    ui.textEdit_2.setText(output_str)


def parse_dictpath(ui):
    input_string = ui.textEdit.toPlainText()
    input_dict = ui.lineEdit_4.text()
    if not input_string or not input_dict:
        output_str = "输入数据和字典数据提取path"
        ui.textEdit_2.setText(output_str)
        return
    output = DataParser(input_string).parse_dict(input_dict)
    output_str = ""
    if isinstance(output, str):
        output_str = output
    elif isinstance(output, list):
        for i in output:
            output_str = output_str + str(i) + "\n"
    else:
        output_str = "未知错误3"
    ui.textEdit_2.setText(output_str)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = data_parser_ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.textEdit.setText('[{a:1, b:2, "c":3, "d":"4"},{a:"a", "c":"c"}]')
    ui.lineEdit.setText('a:(.*?),')
    ui.lineEdit_4.setText("c")
    ui.pushButton.clicked.connect(partial(parse_re, ui))
    ui.pushButton_2.clicked.connect(partial(parse_xpath, ui))
    ui.pushButton_4.clicked.connect(partial(parse_dictpath, ui))

    sys.exit(app.exec_())

