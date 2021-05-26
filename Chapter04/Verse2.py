# Exercise 04-4
if  False:
    max_value   = 0
    a = 0
    b = 0

    for i in range(1, 99 +1):
        j = 100 -i

        if max_value < (i*j):
            max_value = i*j
            a = i
            b = j

    print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))

# Exercise 04-2
if  False:
    key_list = ["name", "hp", "mp", "level"]
    valuse_list = ["기사", 200, 30, 5]
    character = {}

    for i in range(len(key_list)):
        character[key_list[i]] = valuse_list[i]
    
    print(character)

# list_range01.py
if False:
    # 리스트 선언
    array = [273, 32, 103, 57, 52]

    # 리스트에 반복문 적용
    for i in range( len(array) ):
        #출력
        print("{}번째 반복: {}".format(i, array[i]))

# 역반복문
if False:
    # 역반복문
    for i in reversed( range(5) ):
        # 출력
        print("현재 반복 변수: {}".format(i))

# while_with_time.py
if False:
    # 시간과 관련된 기능을 취득
    import time

    # 변수 선언
    number = 0

    # 5초 동안 반복
    target_tick = time.time() + 5
    while time.time() < target_tick:
        number += 1

    # 출력
    print("5초 동안 {}번 반복했습니다.".format(number))

# reversed.py
if  True:
    # 리스트를 선언하고 뒤집다.
    list_a  = [10, 1, 2, 3, 4, 5]
    list_reversed = reversed(list_a)

    # 출력
    print("# reversed() functions")
    print("reversed( [1, 2, 3, 4, 5] ) = ", list_reversed)
    print( "list( reversed([1, 2, 3, 4, 5]) ) = ", list(list_reversed))

    for i in reversed(list_a):
        print(i)

    




