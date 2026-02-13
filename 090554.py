str1 = input("Enter String1: ")
str2 = input("Enter String2: ")
if len(str1) != len(str2):
    print("Strigs Are Not Of The Same Length")
    exit()
else:
    print("Yes,Both Strings Are Of Same Length")
result = ""
for i in range(len(str1)):
    result += str1[i] + str2[i]
print("The Result String Is",result)
