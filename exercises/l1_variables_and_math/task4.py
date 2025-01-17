if __name__ == "__main__":
    # Do not change the line below
    a = b = c = d = None

    # Assign the values of correct types to variables a, b, c, d 
    # to make the script work without errors
    a = 20
    b = 10.5
    c =4+12j
    d = "Hi!"
    print(a + b * c)
    # Do not change the lines below
    assert isinstance(a, int)
    assert isinstance(b, float)
    assert isinstance(c, complex)
    assert isinstance(d, str)