# Trust Fund Buddy - Good
# Demonstrates type conversion

print("Please enter monthly costs")

car = int(input("Lamborghini tune-ups: "))
rent = int(input("Manhattan apartment: "))
jet = int(input("Private jet rental: "))
gifts = int(input("Gifts: "))
food = int(input("Dining out: "))
staff = int(input("Staff (butlers, chef, driver, assistant): "))
guru = int(input("Personal guru and coach: "))
games = int(input("Computer games: "))

total = car + rent + jet + gifts + food + staff + guru + games
print("\nGrand Total: ", total)

input("\nPress Enter to exit")

