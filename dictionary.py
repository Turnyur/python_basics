user_dictionary = {
    "name":"Turnyur",
    "age":21,
    "color":"cyan",
    "is_verified":True
}

print(user_dictionary["age"])
print(user_dictionary.get("birthdate"))
print(user_dictionary.get("birthdate", "Jan 1 1980"))