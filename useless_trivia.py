# Useless Trivia
# Gets information from the user and then prints dumb trivia based on the information provided

name = input("Hi, what's your name? ")
age = int(input("How old are you? "))
weight = int(input("Last question, how many pounds do you weigh? "))

print("\nIf ee cummings were to email you, he'd address you as", name.lower())
print("But if ee were mad, he'd call you", name.upper())

called = name * 5

print("\nIf a small child were trying ot get your attention",)
print("your name would become:")
print(called)

seconds = age * 365 * 24 * 60 * 60

print("\nYou're over ", seconds, "seconds old.")

moon_weight = weight / 6
print("\nDid you know that on the moon you would weigh only", moon_weight, "pounds?")

sun_weight = weight * 27.1
print("\nOn the sun, you'd weigh", sun_weight, "(but, ah... not for long).")

input("\nPress Enter to exit")

