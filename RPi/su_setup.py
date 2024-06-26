#!/usr/bin/python3
# File name   : setup.py for WAVEGO
# Date        : 2022/1/5

import os
import time
import re

curpath = os.path.realpath(__file__)
thisPath = os.path.dirname(curpath)

CMDLINE_FILE = open('/boot/cmdline.txt', 'r')
OLD_LINES = CMDLINE_FILE.readlines()
CMDLINE_FILE.close()

CMDLINE_FILE = open('/boot/cmdline.txt', 'w+')
for EACH_LINE in OLD_LINES:
	NEW_LINES = re.sub('console=serial0,115200', '', EACH_LINE)
	CMDLINE_FILE.writelines(NEW_LINES)

CMDLINE_FILE.close()
