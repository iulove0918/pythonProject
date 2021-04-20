sec = int(input('초를 입력하세요 : '))
min = sec // 60
new_sec = sec % 60
print(min,'분', new_sec, '초')

min = int(input('분을 입력하세요 : '))
new_min = min % 60
hour = (min // 60) % 24
day = (min // 60) // 24
print(day, '일', hour, '시간', new_min, '분')

money = 5000000
year = 5
per = 0.05
result = int(money * (1 + per) ** year)
print(result, '원')

straw = int(input('딸기의 갯수를 입력하세요 : '))
grape = int(input('포도의 갯수를 입력하세요 : '))
total = straw * 113.5 + grape * 75
print(total, 'g입니다.')