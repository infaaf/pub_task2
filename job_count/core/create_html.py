#/usr/bin/env python3
# -*- coding:utf-8 -*-
#   mail: infaaf@126.com
from pyecharts import Bar,Page


page=Page()

bar = Bar("周一", "每小时任务数统计")
bar.add("任务数", ["0", "1", "2", "3", "4", "5","6","7","9", "9", "10", "11","12",
                       "13","2点", "3", "4", "5","6","7","9", "9", "10",'23'],
        [5, 20, 36, 10, 75, 90,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
bar.show_config()
bar.render()

data=[5,20,1,1,1,1]

bar1 = Bar("周二", "这里是副标题")
bar1.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], data)
bar1.show_config()
bar1.render()

bar2 = Bar("周二", "这里是副标题")
bar2.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
bar2.show_config()
bar2.render()


page.add(bar)
page.add(bar1)
page.add(bar2)
page.render()
