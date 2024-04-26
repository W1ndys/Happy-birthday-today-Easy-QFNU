import yaml
from datetime import date

# 读取 birthdays.yml 文件
with open('birthdays.yml', 'r') as file:
    birthdays = yaml.safe_load(file)

# 检查是否有人今天过生日
today = date.today()
birthday_people = [person['name'] for person in birthdays if date.fromisoformat(person['birthday']) == today]

# 如果有人过生日,则输出他们的姓名,以逗号分隔
if birthday_people:
    print(','.join(birthday_people))
