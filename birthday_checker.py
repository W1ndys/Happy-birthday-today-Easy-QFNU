import yaml
from datetime import datetime

# 加载 birthdays.yml 文件
with open("birthdays.yml", "r") as file:
    birthdays_data = yaml.safe_load(file)

# 获取今天的日期
today = datetime.now().strftime("%Y-%m-%d")

# 保存今日过生日的人的名字
today_birthdays = []

# 检查每个人的生日是否是今天
for person in birthdays_data:
    if person["birthday"] == today:
        today_birthdays.append(person["name"])

# 输出今日过生日的人的名字到 birthdays.md
with open("birthdays.md", "w") as file:
    if today_birthdays:
        file.write("今日过生日的人:\n")
        for name in today_birthdays:
            file.write("- " + name + "\n")
    else:
        file.write("今天没有人过生日。\n")
