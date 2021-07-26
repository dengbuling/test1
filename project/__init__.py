import pymysql

#指定mysql版本
pymysql.version_info = (1, 4, 13, "final")

pymysql.install_as_MySQLdb()