
"""
str_a   = input("Input A:\\")
int_a   = int(str_a)

str_b   = input("Input B:\\12")
int_b   = int(str_b)

print("int: a + b = ", int_a + int_b)
print("str: a + b = ", str_a + str_b)
"""

output_f    = "{:+d}".format(52)    #양수
output_g    = "{:-d}".format(-52)   #음수
output_h    = "{: d}".format(52)    #양수: 기호부분 공백
output_i    = "{: d}".format(-52)   #음수: 기호부분 공백
output_w    = "{:=05d}".format(52)    #음수
output_1    = "{}".format(52, type(273))    #음수

print(output_f)
print(output_g)
print(output_h)
print(output_i)
print(output_w)

