import random

from high_color_text import highlight_text
from clear_console import clear_console

a_year_list = [0]*52
energy = 20
inspiration = 20


for week in range(0,len(a_year_list)-1):

    def fight_log():
        text = ""
        for i in range(0, len(a_year_list) - 1):
            if i == week:
                text += highlight_text(f"\t[{a_year_list[i]}]", "yellow_font")
            else:
                text += f"\t{a_year_list[i]}"
        return text


    clear_console()
    print(f"Your fight record so far:{fight_log()}\tYellow = current week\n"
    f"Energy: {highlight_text(energy, 'blue_font')}/20  "
    f"Inspiration: {highlight_text(inspiration, 'blue_font')}/20  "
    f"Week {highlight_text(week + 1, 'blue_font')}/52")

    # End the game if energy or inspiration drops to 0
    if energy <= 0 or inspiration <= 0:
        break
    if energy >= 20:
        energy = 20
    if inspiration >= 20:
        inspiration = 20
    # Loop until the player enters a valid command
    while True:
        answer = input("Enter 'r' to rest, or 'f' to fight: ")
        if answer == "r":
            energy += 5
            inspiration += 3
            break
        elif answer == "f":
            energy -= 5
            inspiration -= 3
            add = 7 + random.randint(0,inspiration)
            a_year_list[week] += add
            break
        else:
            print("Invalid input, please try again.")
total = 0
for i in a_year_list:
    total += i
print("Game over!")
print(f"Over {week+1} weeks, you achieved a total score of {total}")
