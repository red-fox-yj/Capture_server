import redis
import pymysql


def _register(response):
    """用户注册"""
    result = "注册成功"
    r = redis.Redis(
        host="localhost", port=6379, decode_responses=True
    )  # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
    if r.get(response["email"]) is None:
        result = "邮箱验证超时"
    elif r.get(response["email"]) == response["validation"]:
        result = _save_db(response)
        if result == 1:
            result = "注册成功"
        else:
            result = "数据库插入失败"
    elif r.get(response["email"]) != response["validation"]:
        result = "验证码错误"
    return result


def _save_db(response):
    """将注册用户信息保存到数据库"""
    param = {
        "host": "cdb-g76irqy0.cd.tencentcdb.com",
        "port": 10186,
        "db": "mysql",
        "user": "root",
        "password": "red-fox-yj2020",
        "charset": "utf8",
    }
    conn = pymysql.connect(**param)  # 连接对象
    cur = conn.cursor()  # 游标对象，采用默认的数据格式
    # SQL 插入语句
    sql = "insert into Caputure_user values(%s,%s,%s)"
    params = (response["username"], response["password"], response["email"])
    # sql语句参数化，防止攻击！
    result = cur.execute(sql, params)
    # pymysql连接数据库默认开启事物，提交之前的操作，使生效！
    conn.commit()
    # 要及时关闭连接！
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接
    return result
