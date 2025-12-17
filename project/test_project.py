from project import new
from project import current
from project import pickup
from project import stat
from project import produce


def main():
    test_stat()
    test_new()
    test_current()
    test_produce()
    test_pickup()


def test_new():
    assert new("Mark", "S", "3", "pineapples,bell peppers, olives") == ("Order Placed:  \n Order name:Mark \n Size:S\n Number of toppings: 3\n Toppings: pineapples,bell peppers, olives\n Status of Order: Ordered", False)
    assert new("Jacob", "M", "2", "Chicken,Onions") == ("Order Placed:  \n Order name:Jacob \n Size:M\n Number of toppings: 2\n Toppings: Chicken,Onions\n Status of Order: Ordered", False)


def test_current():
   assert current("Mark") == 0



def test_stat():
    assert stat(0) == "Ordered"
    assert stat(1) == "Prepared"
    assert stat(2) == "In the Oven"
    assert stat(3) == "Packing"
    assert stat(4) == "Ready for Pickup"



def test_produce():
    assert produce("Mark","Y") == "Status: old: Ordered --> new: Prepared"
    assert produce("Mark","Y") == "Status: old: Prepared --> new: In the Oven"
    assert produce("Mark","Y") == "Status: old: In the Oven --> new: Packing"
    assert produce("Mark","Y") == "Status: old: Packing --> new: Ready for Pickup"

def test_pickup():
    assert pickup("N","Mark") == "Okay! Come back when you are Ready!"
    assert pickup("Y","Mark") == "Pick up for Mark"



