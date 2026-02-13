word = input ("Enter word")
vowels = {'a','e','i','o','u'}
if any (char.lower()in vowels for char in word):
    print("Word contains vowels")
else:
    print("Word does not conain vowels")
