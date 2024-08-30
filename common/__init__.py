# !/usr/bin/env python3.8
# encoding: utf-8
# Time:2023/8/6 17:28
# Author:xiaobin
# File:__init__.py
# Software:PyCharm

import settings
from common.log_handler import get_logger

logger = get_logger(**settings.LOG_CONFIG)