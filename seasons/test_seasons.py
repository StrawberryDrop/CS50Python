from datetime import date
from seasons import difference
from seasons import minutes

x = date.fromisoformat("2021-12-29")
y = date.fromisoformat("2020-12-29")

def main():
    test_difference()
    test_minutes()

def test_difference():

    assert str(difference(x)) == "365 days, 0:00:00"
    assert str(difference(y)) == "730 days, 0:00:00"

def test_minutes():
    assert minutes(difference(x)) == "five hundred and twenty-five thousand, six hundred"
    assert minutes(difference(y)) == "one million, fifty-one thousand, two hundred"



