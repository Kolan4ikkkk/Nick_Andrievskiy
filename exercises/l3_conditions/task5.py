# Write the body of the function to make the script work without errors
def is_vowel(c: str) -> bool:
     return c.lower() in ['a', 'e', 'i', 'o', 'u']

if __name__ == "__main__":
    # Do not change the below asserts
    assert is_vowel("a") is True
    assert is_vowel("e") is True
    assert is_vowel("z") is False
    assert is_vowel("B") is False
    print(is_vowel("a"))  # True
    print(is_vowel("e"))  # True
    print(is_vowel("z"))  # False
    print(is_vowel("B"))  # False