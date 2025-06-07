import random
import time

print("WELCOME TO MobileNumbersGenerator\n\t| CREATED By MOHIT |")
print("-" * 40)

CountryCode = input("Enter CountryCode (eg. +91 for India, press ENTER to skip): ").strip()
print("-" * 40)

while True:
    try:
        Quantity = int(input("Enter Quantity of Numbers: "))
        if Quantity > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("-" * 40)

StaringCode = input("Enter Starting Code (e.g., 9149------): ").strip()
print("-" * 40)

while True:
    try:
        Length = int(input("Enter Remaining Digits: "))
        if Length > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("-" * 40)
RandomNumber = "9" * Length

def generate_number():
    """Generate a new random mobile number."""
    return str(random.randint(0, int(RandomNumber))).zfill(Length)

# Generate numbers and store in a list
generated_numbers = [CountryCode + StaringCode + generate_number() for _ in range(Quantity)]

# Show a preview
print("\n📞 Generated Numbers:")
for num in generated_numbers[:5]:  # Show only first 5 for preview
    print(num)

# File saving with timestamp
filename = f"MobileNumbers_{time.strftime('%Y%m%d_%H%M%S')}.txt"

try:
    with open(filename, "w") as file:
        file.write("\n".join(generated_numbers))
    print(f"\n✅ {Quantity} numbers successfully saved in {filename}!")
except Exception as e:
    print(f"❌ Error: {e}")

print("=" * 50)
input("Press Enter to exit...")