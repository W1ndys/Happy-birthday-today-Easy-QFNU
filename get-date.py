from lunardate import LunarDate
from datetime import datetime

def get_current_lunar_month_day(year, month, day):
    current_lunar_date = LunarDate.fromSolarDate(year, month, day)
    return f"{current_lunar_date.month:02d}-{current_lunar_date.day:02d}"

# 获取当前日期
current_datetime = datetime.now()

# 获取当前公历日期
current_solar_date = current_datetime.strftime("%Y-%m-%d")

# 获取当前农历日期
current_lunar_month_day = get_current_lunar_month_day(current_datetime.year, current_datetime.month, current_datetime.day)

# 打印公历和农历日期
print(f"————————————————————农历公历输出工具————————————————————————")
print(f"当前公历日期为：{current_solar_date}")
print(f"当前农历日期为：{current_lunar_month_day}")
