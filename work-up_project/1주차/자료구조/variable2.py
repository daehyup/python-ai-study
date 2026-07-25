# 문자열 변수 선언
str_var = "This is my python code"
multi_line = """This is a multi-line string.
It can span multiple lines.
You can use triple quotes for this purpose."""

print(str_var)
print(multi_line)

# 문자열의 더하기
str1 = "Hello, "
str2 = "World!"
result = str1 + str2
print(result)

# 인덱싱
print(str_var[11])
print(str_var[-1])

# 슬라이싱
print(str_var[0:4])
print(str_var[5:])

print(str_var.isalpha())

# 포맷스트링
weahter = "sunny"
temperature = 30.1
# % code
result = "오늘 날씨는 %s이고, 온도는 %.1f도입니다." % (weahter, temperature)
print(result)

# format() code
result = "오늘 날씨는 {}이고, 온도는 {}도입니다.".format(weahter, temperature)
print(result)

#f""
result = f"오늘 날씨는 {weahter}이고, 온도는 {temperature}도입니다."
print(result)

# 사용자로부터 입력받기
name = input("당신의 이름은 무엇입니까? ")
print(f"안녕하세요, {name}님!")