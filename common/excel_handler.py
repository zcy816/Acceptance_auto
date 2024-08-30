# !/usr/bin/env python3.8
# encoding: utf-8
# Time:2023/8/25 14:58
# Author:xiaobin
# File:excel_handler.py
# Software:PyCharm

import openpyxl


class ExcelHandle:

    def read_data(self, filepath, sheet):
        """
        读取Excel数据方法
        :param filepath: 读取的文件路径
        :param sheet: 读取的表单名
        :return:
        """
        # 加载文件
        wb = openpyxl.load_workbook(filepath)
        # 选择表单
        sh = wb[sheet]
        # 遍历表单
        rows_list = list(sh.rows)
        # 提取表头
        title = [i.value for i in rows_list[0]]
        cases = []
        for item in rows_list[1:]:
            li = [c.value for c in item]
            res = dict(zip(title, li))
            cases.append(res)
        return cases

if __name__ == '__main__':
    import settings
    F1_cases = ExcelHandle().read_data(settings.TEST_DATA_FILE, 'user_fail_cases1')
    print(F1_cases)