import configparser

# 读取配置文件
conf = configparser.ConfigParser()
conf.read("config.ini", encoding="utf-8")

# 读取服务器host
server_host = conf.get("serverInfo", "host")

# 读取测试数据
defaultTestDataFile = conf.get("testData", "defaultDataFilePath")
testDataFile = conf.get("testData", "testDataFilePath")

# 读取请求头
header = dict(conf.items("header"))

# 读取mysql信息
host = conf.get("mysql", "host")
port = conf.getint("mysql", "port")
user = conf.get("mysql", "user")
password = conf.get("mysql", "password")
