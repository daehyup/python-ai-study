my_dict = {}
my_dict["key"] = "value"

person = {"name": "홍길동", "age": 30, "city": "서울"}
person_details = {"job": "개발자"}

person.update(person_details)
print(person)

name = person["name"]
age = person["age"]
city = person["city"]
print(f"이름: {name}, 나이: {age}, 도시: {city}")

person.keys()