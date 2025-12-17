from working import convert
import pytest

def main():
    test_bank()

def test_bank():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    with pytest.raises(ValueError):
        assert convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        assert convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        assert convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        assert convert("9:60 AM  5:60 PM")
    with pytest.raises(ValueError):
        assert convert("9:60AM to 5:62PM")
    with pytest.raises(ValueError):
        assert convert("08:20 to 15:40")

if __name__ == "__main__":
    main()