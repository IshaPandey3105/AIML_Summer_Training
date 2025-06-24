# ============================================
#                QUESTIONS
# ============================================

# Q1: Count vowels, consonants, and spaces in a string

str1 = "my name is isha"
vowels_set = "aeiou"
vowels = 0
consonants = 0
spaces = 0

for ch in str1:
    if ch in vowels_set:
        vowels += 1
    elif ch == " ":
        spaces += 1
    else:
        consonants += 1

print("Count of vowels     :", vowels)
print("Count of consonants :", consonants)
print("Count of spaces     :", spaces)

# ============================================

# Q2: Count the number of words in a string

str2 = input("Enter a string: ")
words = str2.split()
print("Number of words in the string:", len(words))

# ============================================

# Q3: Check if a string is a palindrome

s = input("Enter a string: ")
if s == s[::-1]:
    print("String is a Palindrome")
else:
    print("String is NOT a Palindrome")

# ============================================

# Q4: Count frequency of each character and store in dictionary

mystr = "life is beautiful"
freq = {}

for ch in mystr:
    freq[ch] = freq.get(ch, 0) + 1

print("Frequency of each character:")
for key, value in freq.items():
    print(f"{key} : {value}")
