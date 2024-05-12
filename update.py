from lunardate import LunarDate
import datetime
import yaml
import pytz

# 读取生日信息
with open("birthdays.yml", "r", encoding="utf-8") as file:
    birthdays = yaml.safe_load(file)

print("读取生日信息成功！\n")


# 设置时区为东八区
tz = pytz.timezone("Asia/Shanghai")
today = datetime.datetime.now(tz)

print("当前时间为：" + str(today) + "\n")

# 转换今日日期为农历
lunar_today = LunarDate.fromSolarDate(today.year, today.month, today.day)

print("农历日期为：" + str(lunar_today) + "\n")

# 找出今天过生日的人
matching_names = []
for person in birthdays:
    birthday = datetime.datetime.strptime(person["birthday"], "%Y-%m-%d")
    # 转换生日为农历
    lunar_birthday = LunarDate.fromSolarDate(
        birthday.year, birthday.month, birthday.day
    )
    # 检查是否与今天农历日期匹配
    if (
        lunar_birthday.month == lunar_today.month
        and lunar_birthday.day == lunar_today.day
    ):
        matching_names.append(person["name"])
        print(f"{person['name']} 生日匹配！\n")

# 将匹配的姓名写入 happy-birthdays.html
with open("happy-birthdays.html", "w", encoding="utf-8") as file:
    if matching_names:
        file.write(f"今天是{'，'.join(matching_names)}的生日，祝他们生日快乐！")
    else:
        file.write("今天没有人过生日")

print("写入 happy-birthdays.html 成功！\n")

# 将匹配的姓名写入 index.html，使用设计好的 HTML 模板
with open("index.html", "w", encoding="utf-8") as file:
    if matching_names:
        file.write(
            """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>生日快乐！</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f0f0f0;
            padding: 20px;
            margin: 0;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            background-color: #fff;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #333;
        }
        .birthday-message {
            font-size: 18px;
            margin-top: 20px;
        }
        .birthday-names {
            font-size: 24px;
            margin-top: 20px;
            padding: 0;
            list-style: none;
        }
        .birthday-names li {
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>生日快乐！</h1>
        <p class="birthday-message">今天是特别的一天，祝以下同学生日快乐：</p>
        <ul class="birthday-names">"""
        )
        for name in matching_names:
            file.write(f"<li>{name}</li>")
        file.write(
            """
        </ul>
    </div>
</body>
</html>"""
        )
    else:
        file.write("今天没有人过生日")

print("写入 index.html 成功！\n")

print("程序执行完毕！\n")
