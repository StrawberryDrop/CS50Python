from fuel import convert, gauge
import pytest

def main():
    test_pl()

def test_pl():
    with pytest.raises(ValueError):
        assert convert("cat/dog")

    with pytest.raises(ValueError):
        assert convert("7/4")

    with pytest.raises(ZeroDivisionError):
        assert convert("9/0")

    assert convert("1/2") == 50
    assert gauge(75) == "75%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"




if __name__ == "__main__":
    main()