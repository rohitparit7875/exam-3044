def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for ch in s if ch in vowels)
    return count

print(count_vowels("Hello World"))
