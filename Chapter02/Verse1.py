#define     ON             1
#define     OFF            0

#define     VERSE_1         ON


print("Hello world")
#if     VERSE_1
print("""\
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산 대한사람
대한으로 길이 보전하세\
""")


print("""\
"저는" + "1" + "입니다."
""")

print("안녕!! * 3 = " + "안녕!!" * 3)
print("")
print("Zero Index??")
print("굿모닝_1, Index 0: " + "굿모닝_1"[0])
print("굿모닝_1, Index 1: " + "굿모닝_1"[1])
print("굿모닝_1, Index 2: " + "굿모닝_1"[2])
print("굿모닝_1, Index 3: " + "굿모닝_1"[3])
print("굿모닝_1, Index 4: " + "굿모닝_1"[4])
print("")
print("굿모닝_1, Index -1: " + "굿모닝_1"[0])
print("굿모닝_1, Index -2: " + "굿모닝_1"[1])
print("굿모닝_1, Index -3: " + "굿모닝_1"[2])
print("굿모닝_1, Index -4: " + "굿모닝_1"[3])
print("굿모닝_1, Index -5: " + "굿모닝_1"[4])
print()
print("굿모닝_1, [1:4] = " + "굿모닝_1"[1:4])
print("굿모닝_1, [2:3] = " + "굿모닝_1"[2:3])
print("굿모닝_1, [:3] = " + "굿모닝_1"[:3])
print("굿모닝_1, [2:] = " + "굿모닝_1"[2:])
print()
print("len(\"굿모닝_1\") = " )
print( len("굿모닝_1") )
print( type("굿모닝_1") )
print()
#else
#endif