import random

print("WELCOME TO MobileNumbersGenerator\n\t| CREATED By MOHIT |")
print("-"*40)
CountryCode = input("Enter CountryCode (eg. india(+91) Press ENTER For Skip): ")
print("-"*40)
Quantity = int(input("Enter Quantity OF Numbers: "))
print("-"*40)
StaringCode = input("Enter Starting Code (eg. 9149------): ")
print("-"*40)
Length = int(input("Enter Rmaining Digits: "))
print("-"*40)
RandomNumber = str("9"*Length)

def script():
    NewNumber = str(random.randint(0, int(RandomNumber))).zfill(Length)
    return NewNumber

try:
    with open(f"New{Quantity}.txt", "a+") as file:
        for i in range(Quantity):
            number = CountryCode + StaringCode + script() + "\n"
            file.write(number)

except Exception as e:
    print(e)

print(f"{Quantity} Numbers successfully Saved in New{Quantity}.txt file")
print("="*50)
print("Enter Any Key For Exit...")

