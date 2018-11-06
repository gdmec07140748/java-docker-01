#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import os

# dill2 = 'ClassTest1'
# dill = 'Client'
dill = 'cn/lee/demo/Main'
arg = '123 23 33'
# dill = 'Ja'

# print os.system('javac ' + dill2 + '.java')
print os.system('javac ' + dill + '.java')
print os.system('java -cp . ' + dill + '' )