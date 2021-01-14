import ast
from register import _register
from validation import _send_mail, _save_redis


def _distribute(response: str):
    """分发消息"""
    # 去除字符串里面的换行符
    response = list(response)
    while "\n" in response:
        response.remove("\n")
    response = "".join(response)
    # 字符串转json
    response = ast.literal_eval(response)
    if response["type"] == "validation":
        # 验证邮箱
        validation, temp = _send_mail("1461852030@qq.com", response["email"])
        _save_redis(response["email"], validation)
        result = {"type": "validation", "response": temp}
    elif response["type"] == "register":
        # 注册账户
        result = {"type": "register", "response": _register(response)}
    else:
        # 无意义
        result = {"type": "meaningless", "response": "null"}
    return result
