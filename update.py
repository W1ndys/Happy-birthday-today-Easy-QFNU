import yaml
from datetime import datetime
import pytz
from lunardate import LunarDate

# 设置时区为东八区
timezone = pytz.timezone('Asia/Shanghai')

def get_current_lunar_month_day(year, month, day):
    current_lunar_date = LunarDate.fromSolarDate(year, month, day)
    return f"{current_lunar_date.month:02d}-{current_lunar_date.day:02d}"

# 加载 YAML 数据
with open('birthdays.yml', 'r') as file:
    data = yaml.safe_load(file)

# 获取当前日期时间（东八区时间）
current_datetime = datetime.now(timezone)

# 获取当前农历日期
current_lunar_month_day = get_current_lunar_month_day(current_datetime.year, current_datetime.month, current_datetime.day)

# 查找生日与当前日期匹配的姓名
matching_names = []
for entry in data:
    birthday_year, birthday_month, birthday_day = map(int, entry['birthday'].split('-'))
    lunar_birthday = LunarDate.fromSolarDate(birthday_year, birthday_month, birthday_day)
    if lunar_birthday == LunarDate.fromSolarDate(current_datetime.year, current_datetime.month, current_datetime.day):
        matching_names.append(entry['name'])

# 将匹配的姓名写入 index.html
with open('index.html', 'w') as file:
    file.write(', '.join(matching_names))

# 将匹配的姓名写入 happy-birthday.html，使用设计好的 HTML 模板
with open('happy-birthday.html', 'w') as file:
    file.write('''
<!DOCTYPE html>
<html lang="en">
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
        <ul class="birthday-names">''')
    for name in matching_names:
        file.write(f'<li>{name}</li>')
    file.write('''
        </ul>
    </div>
</body>
</html>''')

# 打印当前日期时间（东八区时间）
print("当前日期时间：", current_datetime.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
# 打印当前农历日期
print("当前农历日期：", current_lunar_month_day)
