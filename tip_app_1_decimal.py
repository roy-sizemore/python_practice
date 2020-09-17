# Tip Program
# Shows 15 and 20 percent tip for an input amount (assumes dollars)

print("Hello! I can calculate your tip")

amount = int(input("$"))
tip15 = amount * .15
tip20 = amount * .2

print("You entered $", amount, "\n15% tip: $", tip15, "\n20% tip: $", tip20)

