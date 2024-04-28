import yaml
from datetime import datetime

# 读取 birthdays.yml 文件
with open("birthdays.yml", "r") as file:
    birthdays = yaml.safe_load(file)

# 获取今天的月份和日期
today = datetime.today().strftime("%m-%d")

# 查找当日过生日的姓名
birthday_names = [
    person["name"]
    for person in birthdays
    if datetime.strptime(person["birthday"], "%Y-%m-%d").strftime("%m-%d") == today
]

# 将姓名列表转换为逗号分隔的字符串
names_str = ", ".join(birthday_names)

# 将结果写入 index.html 文件
with open("index.html", "w") as file:
    file.write(f"<p>今天过生日的人：{names_str}</p>")
