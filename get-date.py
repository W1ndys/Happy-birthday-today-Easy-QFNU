from datetime import datetime
import pytz
from lunardate import LunarDate

# 设置时区为东八区
timezone = pytz.timezone('Asia/Shanghai')

# 获取当前日期时间（东八区时间）
current_datetime = datetime.now(timezone)

# 获取公历日期
current_date = current_datetime.strftime("%Y-%m-%d")

# 获取农历日期
current_lunar_date = LunarDate.fromSolarDate(current_datetime.year, current_datetime.month, current_datetime.day)
current_lunar_date_str = current_lunar_date.strftime("%Y-%m-%d (农历 %Y年%m月%d日)")

# 打印今日日期
print("今日公历日期：", current_date)
print("今日农历日期：", current_lunar_date_str)
