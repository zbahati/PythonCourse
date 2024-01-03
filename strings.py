name = input("What's your name? ").strip().title()

first, last = name.split(" ")
print(f" Hello, {first}")

print(f"First name have {len(first)}")