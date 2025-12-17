from numb3rs import validate

def main():
    test_bank()

def test_bank():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("75.456.76.65")== False
    assert validate("cat") == False

if __name__ == "__main__":
    main()