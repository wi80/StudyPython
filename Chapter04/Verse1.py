# list01.py
if  False:
    # list를 선언합니다.
    list_a  = [1, 2, 3]
    list_b  = [4, 5, 6]

    # 출력합니다.
    print("출력합니다.")
    print("list_a = ", list_a)
    print("list_b = ", list_b)

    print()

    # 기본 연산자
    print("# 리스트 기본 연산자")
    print("list_a + llist_b = ", list_a + list_b)
    print("list_a *3 = ", list_a *3)

    print()

    # 함수
    print("길이 구하자")
    print("len( list_a ) = ", len( list_a ))

# list02.py
if  False:
    # 리스트 선언합니다.
    list_a  = [1, 2, 3]

    # 리스트 뒤에 요소 추가하기
    print("# 리스트 뒤에 요소 추가하기")
    list_a.append(4)
    list_a.append(5)
    
    print( list_a )

    print( )

    # 리스트 중간에 요소 추가하기
    print("# 리슽 중간에 요소 추가하기")
    list_a.insert(3, 0)

    print(list_a)


# list03.py
if  False:
    list_a  = [0, 1, 2, 3, 4, 5]
    print("# 리스트의 요소 하나 제거하기")

    # 제거 방법[1] - del
    del list_a[1]
    print("del list_a[1] = ", list_a)

    # 제거 방법[2] - pop
    list_a.pop(2)
    print("pop(2) = ", list_a)

# for_list.py
if  False:
    # 리스트를 선언합니다.
    array  = [273, 32, 103, 57, 52]


    # 리스트에 반복문을 적용합니다.
    for aaa in array:
        #출력
        print(aaa)


# 연습문제 4번
if  True:
    list_of_list = [
        [1, 2, 3],
        [4, 5, 6, 7],
        [8, 9],
        ]

    for list in list_of_list:
        print("", list)

