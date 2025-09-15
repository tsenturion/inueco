zero_dict = {}

translation = {
    "ананас": "pineapple",
    "яблоко": "apple",
}

dict1 = { "1": 123, "2": 234, }

print(translation)
print(zero_dict)
print(dict1)

print(translation["ананас"])
print(translation["яблоко"])

print(translation.get("яблоко2", "яблоко2 нет в словаре"))