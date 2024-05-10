import yaml
from datetime import datetime

# 加载 YAML 数据
with open('birthdays.yml', 'r') as file:
    data = yaml.safe_load(file)

# 获取当前日期
current_date = datetime.now().strftime("%m-%d")

# 查找生日与当前日期匹配的姓名
matching_names = [entry['name'] for entry in data if entry['birthday'][5:] == current_date]

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

current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("当前日期时间：", current_datetime)
