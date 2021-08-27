import logging
from logging.handlers import RotatingFileHandler
import time
import os

# 当前文件路径
currentPath = os.path.abspath(__file__)
parentPath = os.path.dirname(currentPath)
superiorPath = os.path.dirname(parentPath)
# 日志保存路径
loggerPath = superiorPath+"/loggerData/"

fmt = " %(asctime)s %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
datefmt = '%a, %d %b %Y %H:%M:%S'
curTime = time.strftime("%Y-%m-%d %H%M", time.localtime())
handler_1 = logging.StreamHandler()
handler_2 = RotatingFileHandler(loggerPath + "文件名_{0}.log".format(curTime), backupCount=20, encoding='utf-8')
# 设置日志的输出内容形式，输出渠道
logging.basicConfig(
    format=fmt,
    datefmt=datefmt,
    level=logging.INFO,
    handlers=[handler_1, handler_2]
)
