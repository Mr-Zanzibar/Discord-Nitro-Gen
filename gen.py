import requests
import random
import string


print(" Discord Nitro gen (needs a better logo), it will generate some codes, if they work it will show them, if they don't work it will generate a '*'.\n\n\n")
num = int(input('Input How Many Codes to Generate and Check:\n'))


with open("Codes.txt", "w", encoding='utf-8') as file:
    print("I'm checking your codes, wait...")

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"Generated {num} codes\n")

with open("Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f"\n\n Valid | {nitro}\n\n") #If the nitro code will be valid, it will print the nitro code.
        else:
            print(f"*", end = "")   # It will print "*" if the nitro code are not valid.

print("\n\n\nChecked it succesfuly, don't give up, just try and try again")
