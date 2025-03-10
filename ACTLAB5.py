# function
# classify_age_(age)

age = int(input("Classify age: "))
if age <0:
    print("AYOKO AYOKO AYOKO.")
elif age <= 12:
    print("You are a Child.")
elif age <= 19:
    print("You are a Teen.")
elif age <= 64:
    print("You are an Adult.")
else:
    print("You are a Senior.")