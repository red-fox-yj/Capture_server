from email.header import Header
from email.mime.text import MIMEText
import smtplib
import random
import redis


def _send_mail(from_addr, to_addr):
    """发送邮箱验证码"""
    password = "kwrwnikjztexiefa"
    smtp_server = "smtp.qq.com"
    # 生成验证码
    validation = _num()
    response = "验证码发送成功"
    # 生成邮件
    msg = _mail_content(from_addr, to_addr, validation)
    server = smtplib.SMTP_SSL(smtp_server)  # 云服务器需要
    server.set_debuglevel(1)
    server.ehlo(smtp_server)  # 云服务器需要
    server.login(from_addr, password)
    try:
        server.sendmail(from_addr, [to_addr], msg.as_string())
    except smtplib.SMTPRecipientsRefused:
        response = "邮箱不存在"
    server.quit()
    return validation, response


def _save_redis(email: str, validation: str):
    """将验证码保存到redis里面"""
    r = redis.Redis(
        host="127.0.0.1", port=6379, decode_responses=True
    )  # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
    r.set(email, validation, ex=120)
    print(r.get(email))


def _mail_content(from_addr, to_addr, validation):
    """生成邮件内容"""
    msg = MIMEText("您的验证码为：" + validation, "plain", "utf-8")
    msg["From"] = Header("redfox")
    msg["To"] = Header(to_addr)
    msg["Subject"] = Header("redfox感谢您的注册", "utf-8").encode()
    return msg


# 随机生成四位数字验证码
def _num():
    """随机生成四位数字验证码"""
    veri = ""
    for i in range(4):
        veri_num = random.randint(48, 57)
        veri_str = chr(veri_num)
        veri = veri + veri_str
    return veri
