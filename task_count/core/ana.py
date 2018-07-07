#/usr/bin/env python3
# -*- coding:utf-8 -*-
#   mail: infaaf@126.com
import yaml
from pyecharts import Bar,Page


class Ana:
    def __init__(self):
        self.__result=Ana.initresult()

    @staticmethod
    def initresult():
        result = {}
        for i in range(1, 8):
            result[i] = [0  for i in range(24)]
        return result

    def calc(self):
        with open('../cfg/joblist.yaml',encoding='utf-8') as f:
            cfg = yaml.load(f)
        for item in cfg.get('type1'):
            for job in item.get('jobs'):
                try:
                    job = [int(i) for i in job.split(',')]
                except TypeError:
                    print('job数字检查')
                except ValueError as e:
                    print('job正整数检查')
                except Exception:
                    print('格式错误')
                weekday, start_time, end_time = job[0], job[1], job[2]
                for hour in range(start_time, end_time):
                    self.__result[weekday][hour] += 1
        return self.__result

    @property
    def result(self):
        return self.__result


    def createhtml(self):
        page = Page('每日任务数')
        weekname=['周一','周二','周三','周四','周五','周六','周日']


        for i in range(7):
            bar = Bar(weekname[i], "每小时任务数统计")
            bar.add("任务数", ["0", "1", "2", "3", "4", "5", "6", "7", "9", "9", "10", "11", "12",
                            "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", '23'],
                    self.result[i+1]
                    )
            bar.show_config()
            bar.render()
            page.add(bar)


        page.render()


if __name__ == '__main__':
    ana=Ana()
    ana.calc()
    # print(ana.result)
    ana.createhtml()