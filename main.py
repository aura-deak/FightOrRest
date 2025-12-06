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
    print(f"直到上一周，你的所有奋斗记录：{fight_log()}\t其中黄色高亮数字为这一周\n"
    f"精力值为{highlight_text(energy, 'blue_font')}/20"
    f"灵感值为{highlight_text(inspiration, 'blue_font')}/20。"
    f"现在是第{highlight_text(week + 1, "blue_font")}/52周")

    # 维持energy和inspiration20内，并在其中一个小于等于0时强制结束游戏
    if energy <= 0 or inspiration <= 0:
        break
    if energy >= 20:
        energy = 20
    if inspiration >= 20:
        inspiration = 20
    #死循环，直到玩家输入正确指令
    while True:
        answer = input("你可以输入r休息，或者输入f奋斗")
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
            print("输入错误，请重新输入")
total = 0
for i in a_year_list:
    total += i
print("游戏结束！")
print(f"在今年的{week+1}周内，你所获得的成就为{total}")