#/usr/bin/env python3
# -*- coding:utf-8 -*-
#   mail: infaaf@126.com
import sys
import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,BASE_DIR)


from core import ana

ana=ana.Ana()
print(ana.result)