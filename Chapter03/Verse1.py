#03-1 condition.py
if False:
    # 입력 받다.
    number  = input("정수 입력> ")
    number  = int(number)

    #양수 조건
    if number > 0:
        print("양수")

    #음수 조건
    if number < 0:
        print("음수")

    #0 조건
    if number == 0:
        print("0")

#03-1 date.py
if  False:
    # 날짜 / 시간과 관련된 기능을 가져옵니다.
    import  datetime

    # 현재 날짜 / 시간을 구합니다.
    now = datetime.datetime.now()

    # Output
    print(now.year,     "년")
    print(now.month,    "월")
    print(now.day,      "일")
    print(now.hour,     "시")
    print(now.minute,   "분")
    print(now.second,   "초")

    # Output
    print("{}년. {}월. {}일. {}시. {}분. {}초".format(
         now.year, 
         now.month, 
         now.day, 
         now.hour, 
         now.minute, 
         now.second
         )
                  )

#03-1   date02.py
if  False:
    # 날짜 / 시간과 관련된 기능을 가죠오다.
    import datetime

    # 현재 날짜 / 시간을 구하다.
    now = datetime.datetime.now()

    # 오전구분
    if now.hour < 12:
        print("현재 시각은 {}시로 오전입니다.".format(
            now.hour
        ))

    # 오후구분
    if now.hour >= 12:
        print("현재 시각은 {}시로 오후입니다.".format(
            now.hour
        ))

    # 봄 구분
    if 3 <= now.month < 6:
        print("이번달은 {}월로 봄입니다.".format(
            now.month
        ))

    # 여름 구분
    if 5 < now.month < 9:
        print("이번달은 {}월로 여름입니다.".format(
            now.month
        ))

    # 가을 구분
    if 8 < now.month < 12:
        print("이번달은 {}월로 가을입니다.".format(
            now.month
        ))

    # 겨울 구분
    if 11 < now.month or now.month < 3:
        print("이번달은 {}월로 여름입니다.".format(
            now.month
        ))


# 03-1  codition01.py
if  True:
    # 입력을 받다.
    number  = input("정수 입력>")

    # 마지막 자리 숫자 추출
    last_character  = number[-1]

    # 숫자로 변환
    last_number = int(last_character)

    # 짝수 확인
    if  last_number == 0 or \
        last_number == 2 or \
        last_number == 4 or \
        last_number == 8:
        print("짝수 입니다.")

    if  last_character in "02468":
        print("'02468' 짝수입니다.")

    # 홀수 확인
    if  last_number == 1 or \
        last_number == 3 or \
        last_number == 7 or \
        last_number == 9:
        print("홀수 입니다.")

    if  last_character in "13579":
        print("'13579' 홀수입니다.")

    a   = float(input("1번째 숫자> "))
    b   = float(input("2번째 숫자> "))
    print()

    if  a > b:
        print("처음 입력했던 {}가 {}보다 더 큽니다.".format(a, b))

    if  a < b:
        print("2번째 입력했던 {}가 {}보다 더 큽니다.".format(b, a))


