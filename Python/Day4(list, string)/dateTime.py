# 날짜 , 시간 형식 관련 함수

from datetime import date , datetime , timedelta

today = date.today()
year = today.year
month = today.month
day = today.day
print(f'연도 : {year}, 월 : {month}, 일 : {day}')
print('연도 : {}, 월 : {}, 일 : {}'.format(year,month,day))

# print(datetime.today())
print(datetime.now().time())

current_time = datetime.now().time()
time = current_time.hour
minute = current_time.minute
second = current_time.second
microsec = current_time.microsecond


# timedelta
print(today + timedelta(days=-1)) #24시간 이전(어제 날짜)
print(today + timedelta(days=1)) #24시간 이후 (내일 날짜)
print(today + timedelta(days=7)) # 1주일 후
print(today + timedelta(days=-7)) # 1주일 전

curr_now = datetime.now()
print(curr_now+ timedelta(hours=-1)) #1시간 전
print(curr_now + timedelta(days = 1 , hours=2)) # 내일 2시간 후

# strftime() 함수 : 날짜 형식을 문자열로 반환
# H : 24 시간 , I : 12시간 기준

print(today.strftime('%Y-%m-%d  %H:%M:%S'))
print(today.strftime('%Y-%m-%d  %I:%M:%S %p')) # %p는 pm , am 구분

print(type(today))
print(type(curr_now))

# strptime() 함수 : 문자열을 날짜 형식으로 반환
today = '2020-06-20 17:40:20'
print(type(today))

transToday = datetime.strptime(today, '%Y-%m-%d %H:%M:%S' )
print(transToday)
print(type(transToday))

