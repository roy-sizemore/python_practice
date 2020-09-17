# Trust Fund Buddy - Bad
# Demonstrates a logical error

print("Please enter monthly costs")

car = input("Lamborghini tune-ups: ")
rent = input("Manhattan apartment: ")
jet = input("Private jet rental: ")
gifts = input("Gifts: ")
food = input("Dining out: ")
staff = input("Staff (butlers, chef, driver, assistant): ")
guru = input("Personal guru and coach: ")
games = input("Computer games: ")

total = car + rent + jet + gifts + food + staff + guru + games
print("\nGrand Total: ", total)

input("\nPress Enter to exit")

