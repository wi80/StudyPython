# 03-2  codition04.py
if False:
    # 입력 받다.
    number  = input("정수 입력> ")
    number  = int(number)

    #짝수 조건
    if number % 2 == 0:
        print("짝수")
    else:
        print("홀수")


# 03-2  codition05.py
if  False:
    # 날짜 / 시간과 관련된 기능을 가져옵니다.
    import  datetime

    # 현재 날짜 / 시간을 구합니다.
    now = datetime.datetime.now()
    month   = now.month
    
    if 3 <= month <= 5:
          print("봄")
    elif 6 <= month <= 8:
       print("여름")
    elif 9 <= month <= 11:
       print("가을")
    else:
       print("겨울")


#03-2   condition07.py
if  False:
    #변수를 선언합니다.
    score   = float( input("학점입력> "))

    #조건문을 적용합니다.
    if score == 4.5:
        print("신")
    elif    4.2 <= score:
        print("교수님의 사랑")
    elif    3.5 <= score:
        print("현 체제의 수호자")
    elif    2.8 <= score:
        print("일반인")
    elif    2.3 <= score:
        print("일탈을 꿈꾸는 소시민")
    elif    1.75 <= score:
        print("오락문화의 선구자")
    elif    1.0 <= score:
        print("불가촉천민")
    elif    0.5 <= score:
        print("자벌레")
    elif    0 <= score:
        print("플랑크톤")
    else:
        print("시대를 앞서가는 혁명의 씨앗")

#03-2 false_valse.py
if  False:
    print("#if 조건문에 0 넣기")

    if 0:
        print("0은 True로 변환됩니다.")
    else:
        print("0은 False로 변환됩니다.")
    print()

    print("#if 조건문에 빈문자열 넣기")

    if "":
        print("빈문자열 True로 변환됩니다.")
    else:
        print("빈문자열 False로 변환됩니다.")

#03-2 pass_keyword.py
if  False:
    # 입력 받다.
    number  = input("정수 입력> ")
    number  = int(number)

    # 조건문 사용
    if  number > 0:
        # 양수 일때: 아직 미 구현 상태 . T.B.D
        raise NotImplementedError
    else:
        # 음수 일때:  TBD
        pass

#03-2 End
if  True:
    # 입력 받다.
    str_input   = input("태어난 해를 입력하세요> ")
    birth_year  = int(str_input) % 12

    if birth_year == 0:
        print("원숭이 띠")
    elif birth_year == 1:
        print("닭 띠")
    elif birth_year == 2:
        print("개 띠")
    elif birth_year == 3:
        print("돼지 띠")
    elif birth_year == 4:
        print("쥐 띠")
    elif birth_year == 5:
        print("소 띠")
    elif birth_year == 6:
        print("범 띠")
    elif birth_year == 7:
        print("토끼 띠")
    elif birth_year == 8:
        print("용 띠")
    elif birth_year == 9:
        print("뱀 띠")
    elif birth_year == 10:
        print("말 띠")
    elif birth_year == 11:
        print("양 띠")


