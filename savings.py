amount_saved = 0
while amount_saved <= 100:
    money_made = int(input("How much will you save: "))
    amount_to_save = money_made * 0.4
    if money_made < 20:
        print(f"Your earnings for today is not sufficient, we were able to save {amount_saved} for now. However, let us pause on savings for today")
        break
    amount_saved += amount_to_save
print(f"We have managed to save up to {amount_saved}")