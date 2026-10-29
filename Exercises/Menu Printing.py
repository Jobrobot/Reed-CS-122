name = input("Restaurant name? ")

firstEntree = input("First entree? ").strip()
fePrice = input("First entree price? ").strip()

secondEntree = input("Second entree? ").strip()
sePrice = input("Second entree price? ").strip()

thirdEntree = input("Third entree? ").strip()
tePrice = input("Third entree price? ").strip()

title = name + " Entrees"

longest = max(len(firstEntree), len(secondEntree), len(thirdEntree))

def dotMaker(entree):
    return longest - len(entree) + 2

print()
print(title)
print("-" * len(title))
print(firstEntree + "." * dotMaker(firstEntree) + "$" + fePrice.rjust(3))
print(secondEntree + "." * dotMaker(secondEntree) + "$" + sePrice.rjust(3))
print(thirdEntree + "." * dotMaker(thirdEntree) + "$" + tePrice.rjust(3))