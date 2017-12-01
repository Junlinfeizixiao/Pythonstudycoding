from datetime import datetime,timedelta,timezone
#获取当前时间
# now = datetime.now()
# print(now)
# print(type(now))

#获取指定时间
# dt = datetime(2017,12,1,17,4)
# print(dt)

#datetime转换为timestamp
#在计算机中，时间是用浮点数字表示的
# dt = datetime(2017,12,1,17,6)
# st = dt.timestamp()
# print(st)  #1512119160.0

#timestamp转换为datetime
# st = 1512119960.0
# print(datetime.fromtimestamp(st))
# print(datetime.utcfromtimestamp(st))

#str转换为datetime
# str = "2017-12-1 17:19:0"
# ex = "%Y-%m-%d %H:%M:%S"
# cday = datetime.strptime(str,ex)
# print(cday)

#datetime加减
# dt = datetime.now()
# print(dt)
# print(dt + timedelta(hours = 10))

#用户输入 2017-12-1 18:50:30 时区信息UTC+5:00
#先把时区信息的时间区分出来，如把+5:00利用正则表达式求得，再依此将时间转化

import re
def  to_timestamp(dt_str,tz_str):
	tz_re =re.compile(r'^UTC([+-]\d{1,2}):([0-5]\d)')
	num=int(re.match(tz_re,tz_str).group(1))
	dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
	dt = dt.replace(tzinfo = timezone(timedelta(hours = num)))
	return dt.timestamp()
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')