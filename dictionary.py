my_dict = {}
my_dict["key"] = "value"

print(my_dict)

person = {"name": "홍길도", "age": "30", "city": "서울"}
name = person["name"]
print(name)

print(f"이름은 {person['name']}, 나이는 {person['age']}, 고향은 {person['city']}")

country = person.get("country", "알 수 없음")
print(f"국적은 {country} 입니다.")

person_detail = {"country" : "대한민국", "married": True}
print(person_detail)
print(person_detail.keys())

del person_detail["married"]
print("After ", person_detail.keys())