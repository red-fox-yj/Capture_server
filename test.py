import csv

temp_list = []


def _WriteToCsv(names: list):
    """将名单写入CSV"""
    with open(
        "names.csv",
        "w",
        newline="",
        encoding="UTF8",
    ) as csvfile:
        writer = csv.writer(csvfile)
        for row in names:
            writer.writerow([row])


def _ReadNames():
    """将名单写入CSV"""
    with open(
        "names.csv",
        "r",
        newline="",
        encoding="UTF8",
    ) as csvfile:
        temp = []
        reader = csv.reader(csvfile)
        for row in reader:
            temp.append(row[0])
    return temp


def _modify(names_str: str):
    """"""
    _WriteToCsv(names_str.split(","))


user_list = ["用户名为空", "用户名已存在", "用户名有效"]
email_list = ["邮箱为空", "邮箱已存在", "邮箱无效", "邮箱有效"]
validation_list = ["验证码为空", "验证码错误", "验证码正确"]
password_list = ["密码为空", "密码错误", "密码正确"]

for item_1 in user_list:
    temp_1 = item_1 + "+"
    for item_2 in email_list:
        temp_2 = temp_1
        temp_2 += item_2 + "+"
        for item_3 in validation_list:
            temp_3 = temp_2
            temp_3 += item_3 + "+"
            for item_4 in password_list:
                temp_list.append(temp_3 + item_4)


print(temp_list)
_WriteToCsv(temp_list)