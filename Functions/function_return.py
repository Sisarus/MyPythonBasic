def is_adult(age):
    return age >= 16

def convert_gender(gender="unknown"):
    if gender.upper() == "M":
        return "Male"
    elif gender.upper() == "F":
        return "Female"
    else:
        return f"Gender {gender} is unknown"

result = is_adult(45)
print(result)

print(convert_gender("M"))
print(convert_gender("f"))
print(convert_gender("F"))
print(convert_gender("Keuni"))
