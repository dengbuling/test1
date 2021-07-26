import pymysql

#指定mysql版本
pymysql.version_info = (1, 4, 13, "final", 0)

pymysql.install_as_MySQLdb()