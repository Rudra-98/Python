def is_anagram(str1, str2):
    #ignoring case
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    if len(str1) != len(str2):
        return False
    elif not all(True if s in str2 else False  for s in str1):
        return False
    return True


print(is_anagram("listen", "silent"))
print(is_anagram("Hello", "hello"))
print(is_anagram("Astronomer", "Moon starer"))
print(is_anagram("hello", "world"))
print(is_anagram("abc", "ab"))




