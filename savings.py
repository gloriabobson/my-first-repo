amount_saved = 0
while amount_saved <= 100:
    amount_to_save = int(input("How much will you save: "))
    amount_saved += amount_to_save
print(f"We have managed to save up {amount_saved}")