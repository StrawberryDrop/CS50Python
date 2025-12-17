from um import count
#import pytest

def main():
    test_bank()

def test_bank():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album") == 1
    assert count("Um, thanks, um...") == 2

if __name__ == "__main__":
    main()