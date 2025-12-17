from datetime import date
import sys
import inflect

p = inflect.engine()

def main():


    birth = input("Date of Birth: ")
    try:
        birthday = date.fromisoformat(birth)
        s  = difference(birthday)
        words = minutes(s)
        words = words.capitalize()
        words = words.replace(" and "," ")
        print(words+" minutes")
    except:
        sys.exit("Invalid date")


def difference(bday):

     x = date.today()
     s = x - bday

     return s

def minutes(number):
        k = int(number.days) *1440
        words = p.number_to_words(k)
        return words


if __name__ == "__main__":
    main()