# Do not change the line below
Number = int | float


# Write the function body to make the script work without errors
def is_positive(n: Number) -> bool:
    return n >= 0 


# Do not change the below's code
if __name__ == "__main__":
    assert is_positive(3) is True
    assert is_positive(0) is True
    assert is_positive(3.1) is True
    assert is_positive(-1) is False
    assert is_positive(-0.1) is False
# Add output of results
    print(is_positive(3))    # True
    print(is_positive(0))    # True
    print(is_positive(3.1))  # True
    print(is_positive(-1))   # False
    print(is_positive(-0.1)) # False