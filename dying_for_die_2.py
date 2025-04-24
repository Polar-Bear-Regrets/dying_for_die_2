import random
from collections import Counter

def die_pack():
    global contents_of_box
    global die_added
    global eyes
    dies_2 = []
    if 3 in eyes:
        dies_2.append(random.randint(2, 5))
        dies_2.append(random.randint(2, 5))
        dies_2.append(random.randint(2, 5))
    else:
        dies_2.append(random.randint(1, 5))
        dies_2.append(random.randint(1, 5))
        dies_2.append(random.randint(1, 5))
    for i in dies_2:
        if random.randint(1, 5) == 1:
            print("stone")
            dies_2.pop(-1)
            dies_2.append(15)
        elif i == 1:
            print("norm die")
        elif i == 2:
            print("d1")
        elif i == 3:
            print("d4")
        elif i == 4:
            print("coin")
        elif i == 11:
            print("lucky die")
        elif i == 12:
            print("lucky d1")
        elif i == 13:
            print("lucky d4")
        elif i == 14:
            print("lucky coin")
        elif i == 21:
            print("mult die")
        elif i == 22:
            print("mult d1")
        elif i == 23:
            print("mult d4")
        elif i == 24:
            print("mult coin")
        elif i == 31:
            print("pinned die")
        elif i == 32:
            print("pinned d1")
        elif i == 33:
            print("pinned d4")
        elif i == 34:
            print("pinned coin")
        elif i == 41:
            print("badge die")
        elif i == 42:
            print("badge d1")
        elif i == 43:
            print("badge d4")
        elif i == 44:
            print("badge coin")
        elif i == 51:
            print("bonus die")
        elif i == 52:
            print("bonus d1")
        elif i == 53:
            print("bonus d4")
        elif i == 54:
            print("bonus coin")
    decision = int(input(" 1 for option one etc."))
    contents_of_box.append(dies_2[decision - 1])
    print("die has been added to deck.")
    die_added += 1

def emerald_eye():
    global high_die_level
    global pair_level
    global two_pair_level
    global three_pair_level
    global full_house_level
    global three_of_a_kind_level
    global four_of_a_kind_level
    global five_of_a_kind_level
    global six_of_a_kind_level
    global two_trio_level
    global overflow_house_level
    global high_die
    global pair
    global two_pair
    global three_pair
    global three_of_a_kind
    global full_house
    global four_of_a_kind
    global five_of_a_kind
    global six_of_a_kind
    global overflow_house
    hand_plays = {1: high_die_played, 2: pair_played, 3: three_pair_played, 4: full_house_played, 5: two_trio_played, 6: two_trio_played, 7: three_of_a_kind_played, 8: four_of_a_kind_played, 9: five_of_a_kind_played, 10: six_of_a_kind_played, 11: overflow_house_played}
    most_played = max(hand_plays, key=hand_plays.get)
    if most_played == 1:
        high_die_level += 1
        high_die[0] += 120
        high_die[1] += 12
        print("high die has been upgraded.")
    elif most_played == 2:
        pair_level += 1
        pair[0] += 20
        pair[1] += 2
        print("pair has been upgraded.")
    elif most_played == 3:
        two_pair_level += 1
        two_pair[0] += 40
        two_pair[1] += 2
        print("two pair has been upgraded.")
    elif most_played == 4:
        three_pair_level += 1
        three_pair[0] += 60
        three_pair[1] += 2
        print("three pair has been upgraded")
    elif most_played == 5:
        full_house_level += 1
        full_house[0] += 90
        full_house[1] += 4
        print("full house has been upgraded")
    elif most_played == 6:
        two_trio_level += 1
        two_trio[0] += 60
        two_trio[1] += 3
        print("two trio has been upgraded.")
    elif most_played == 7:
        three_of_a_kind_level += 1
        three_of_a_kind[0] += 30
        three_of_a_kind[1] += 3
        print("three of a kind has been upgraded.")
    elif most_played == 8:
        four_of_a_kind_level += 1
        four_of_a_kind[0] += 40
        four_of_a_kind[1] += 4
        print("four of a kind has been upgraded.")
    elif most_played == 9:
        five_of_a_kind_level += 1
        five_of_a_kind[0] += 50
        five_of_a_kind[1] += 5
        print("five of a kind has been upgraded.")
    elif most_played == 10:
        six_of_a_kind_level += 1
        six_of_a_kind[0] += 60
        six_of_a_kind[1] += 6
        print("six of a kind has been upgraded.")
    else:
        overflow_house_level += 1
        overflow_house[0] += 50
        overflow_house[1] += 5
        print("overflow house has been upgraded.")

def gem_pack():
    global cash
    global high_die_level
    global pair_level
    global two_pair_level
    global three_pair_level
    global full_house_level
    global three_of_a_kind_level
    global four_of_a_kind_level
    global five_of_a_kind_level
    global six_of_a_kind_level
    global two_trio_level
    global overflow_house_level
    global eyes
    global high_die
    global pair
    global two_pair
    global three_pair
    global three_of_a_kind
    global full_house
    global four_of_a_kind
    global five_of_a_kind
    global six_of_a_kind
    global overflow_house
    gem_1 = random.randint(1, 11)
    gem_2 = random.randint(1, 11)
    gem_3 = random.randint(1, 11)
    gems = []
    gems.append(gem_1)
    gems.append(gem_2)
    gems.append(gem_3)
    for i in gems:
        if i == 1:
            print("lapis lazuli - upgrades high die, 120 pupils, 12 mult")
        elif i == 2:
            print("garnet - upgrades pair, 20 pupils, 2 mult")
        elif i == 3:
            print("opal - upgrades two pair, 40 pupils, 2 mult")
        elif i == 4:
            print("pearl - upgrades three pair, 60 pupils, 2 mult")
        elif i == 5:
            print("emerald - upgrades full house, 90 pupils, 4 mult")
        elif i == 6:
            print("ruby - upgrades two trio, 60 pupils, 3 mult")
        elif i == 7:
            print("obsidian - upgrades three of a kind, 30 pupils, 3 mult")
        elif i == 8:
            print("diamond - upgrades four of a kind, 40 pupils, 4 mult")
        elif i == 9:
            print("amethyst - upgrades five of a kind, 50 pupils, 5 mult")
        elif i == 10:
            print("peridot - upgrades six of a kind, 60 pupils, 6 mult")
        elif i == 11:
            print("topaz - upgrades overflow house, 50 pupils, 5 mult")
    decision = int(input("1 for option one etc"))
    if gems[decision - 1] == 1:
        high_die_level += 1
        high_die[0] += 120
        high_die[1] += 12
        print("high die has been upgraded.")
    elif gems[decision - 1] == 2:
        pair_level += 1
        high_die[0] += 20
        high_die[1] += 2
        print("pair has been upgraded.")
    elif gems[decision - 1] == 3:
        two_pair_level += 1
        two_pair[0] += 40
        two_pair[1] += 2
        print("two pair has been upgraded.")
    elif gems[decision - 1] == 4:
        three_pair_level += 1
        three_pair[0] += 60
        three_pair[1] += 2
        print("three pair has been upgraded")
    elif gems[decision - 1] == 5:
        full_house_level += 1
        full_house[0] += 90
        full_house[1] += 4
        print("full house has been upgraded")
    elif gems[decision - 1] == 6:
        two_trio_level += 1
        two_trio[0] += 60
        two_trio[1] += 3
        print("two trio has been upgraded.")
    elif gems[decision - 1] == 7:
        three_of_a_kind_level += 1
        three_of_a_kind[0] += 30
        three_of_a_kind[1] += 3
        print("three of a kind has been upgraded.")
    elif gems[decision - 1] == 8:
        four_of_a_kind_level += 1
        four_of_a_kind[0] += 40
        four_of_a_kind[1] += 4
        print("four of a kind has been upgraded.")
    elif gems[decision - 1] == 9:
        five_of_a_kind_level += 1
        five_of_a_kind[0] += 50
        five_of_a_kind[1] += 5
        print("five of a kind has been upgraded.")
    elif gems[decision - 1] == 10:
        six_of_a_kind_level += 1
        six_of_a_kind[0] += 60
        six_of_a_kind[1] += 6
        print("six of a kind has been upgraded.")
    else:
        overflow_house_level += 1
        overflow_house[0] += 50
        overflow_house[1] += 5
        print("overflow house has been upgraded.")

def soul_pack():
    global cash
    global high_die_level
    global pair_level
    global two_pair_level
    global three_pair_level
    global full_house_level
    global three_of_a_kind_level
    global four_of_a_kind_level
    global five_of_a_kind_level
    global six_of_a_kind_level
    global two_trio_level
    global overflow_house_level
    global contents_of_box
    global souls_played
    souls_played += 1
    soul_1 = random.randint(1, 15)
    soul_2 = random.randint(1, 15)
    soul_3 = random.randint(1, 15)
    souls = []
    souls.append(soul_1)
    souls.append(soul_2)
    souls.append(soul_3)
    draw_1 = random.randint(0, len(contents_of_box) - 1)
    draw_2 = random.randint(0, len(contents_of_box) - 1)
    draw_3 = random.randint(0, len(contents_of_box) - 1)
    draw_4 = random.randint(0, len(contents_of_box) - 1)
    draw_5 = random.randint(0, len(contents_of_box) - 1)
    draw_6 = random.randint(0, len(contents_of_box) - 1)
    draws = []
    draw_1 = contents_of_box[draw_1]
    draw_2 = contents_of_box[draw_2]
    draw_3 = contents_of_box[draw_3]
    draw_4 = contents_of_box[draw_4]
    draw_5 = contents_of_box[draw_5]
    draw_6 = contents_of_box[draw_6]
    draws.append(draw_1)
    draws.append(draw_2)
    draws.append(draw_3)
    draws.append(draw_4)
    draws.append(draw_5)
    draws.append(draw_6)
    for i in draws:
        if i == 1:
            print("norm die")
        elif i == 2:
            print("d1")
        elif i == 3:
            print("d4")
        elif i == 4:
            print("coin")
        elif i == 11:
            print("lucky die")
        elif i == 12:
            print("lucky d1")
        elif i == 13:
            print("lucky d4")
        elif i == 14:
            print("lucky coin")
        elif i == 21:
            print("mult die")
        elif i == 22:
            print("mult d1")
        elif i == 23:
            print("mult d4")
        elif i == 24:
            print("mult coin")
        elif i == 31:
            print("pinned die")
        elif i == 32:
            print("pinned d1")
        elif i == 33:
            print("pinned d4")
        elif i == 34:
            print("pinned coin")
        elif i == 41:
            print("badge die")
        elif i == 42:
            print("badge d1")
        elif i == 43:
            print("badge d4")
        elif i == 44:
            print("badge coin")
        elif i == 51:
            print("bonus die")
        elif i == 52:
            print("bonus d1")
        elif i == 53:
            print("bonus d4")
        elif i == 54:
            print("bonus coin")
        else:
            print("stone")
    for i in souls:
        if i == 1:
            print("soul of the magician - turns hands stickers to lucky stickers (lucky stickers: 1 in 5 chance for 5 mult, 1 in 20 chance for 10 cash)")
        elif i == 2:
            print("soul of the priestess - upgrades 2 random hands by one")
        elif i == 3:
            print("soul of the empress - turns hands stickers into mult stickers (mult stickers: 1 mult)")
        elif i == 4:
            print("soul of the hierophant - turns hands stickers into bonus stickers (bonus stickers: 10 pupils")
        elif i == 5:
            print("soul of the chariot - turns hands stickers into pins (pins: 1.1x mult)")
        elif i == 6:
            print("soul of justice - turns hands stickers into badges (badges: 1.2x mult, 1 in 4 chance die dies)")
        elif i == 7:
            print("soul of the hermit - doubles cash, max of 20")
        elif i == 8:
            print("souls of power - turns spheres into coins, coins into d4's, d4's into d6's, and d6's into spheres.")
        elif i == 9:
            print("vengeful soul - destroys hand.")
        elif i == 10:
            print("soul of the fallen - turns die into rocks, always rolls 15's but cant contrabute to hand.")
        elif i == 11:
            print("soul of the star - turns hand into d4's")
        elif i == 12:
            print("soul of the moon - turns hand into spheres")
        elif i == 13:
            print("soul of god - turns hand into d6's")
        elif i == 14:
            print("soul of the sun - turns hand into coins")
        else:
            print("soul of the judge - creates a random celestial body")
    decision = int(input("1 for option one etc."))
    if souls[decision - 1] == 1:
        for i in range(0, 6, 1):
            if draws[i] == 1 or draws[i] == 11 or draws[i] == 21 or draws[i] == 31 or draws[i] == 41 or draws[i] == 51:
                contents_of_box.append(11)
            if draws[i] == 2 or draws[i] == 12 or draws[i] == 22 or draws[i] == 32 or draws[i] == 42 or draws[i] == 52:
                contents_of_box.append(12)
            if draws[i] == 3 or draws[i] == 13 or draws[i] == 23 or draws[i] == 33 or draws[i] == 43 or draws[i] == 51:
                contents_of_box.append(13)
            if draws[i] == 4 or draws[i] == 14 or draws[i] == 24 or draws[i] == 34 or draws[i] == 44 or draws[i] == 54:
                contents_of_box.append(14)
            contents_of_box.remove(draws[i])

    elif souls[decision - 1] == 2:
        while True:
            hand_1 = random.randint(1, 11)
            hand_2 = random.randint(1, 11)
            if hand_1 != hand_2:
                break
        if hand_1 == 1 or hand_2 == 1:
            high_die_level += 1
            high_die[0] += 120
            high_die[1] += 12
            print("high die has been upgraded.")
        if hand_1 == 2 or hand_2 == 2:
            pair_level += 1
            high_die[0] += 20
            high_die[1] += 2
            print("pair has been upgraded.")
        if hand_1 == 3 or hand_2 == 3:
            two_pair_level += 1
            two_pair[0] += 40
            two_pair[1] += 2
            print("two pair has been upgraded.")
        if hand_1 == 4 or hand_2 == 4:
            three_pair_level += 1
            three_pair[0] += 60
            three_pair[1] += 2
            print("three pair has been upgraded")
        if hand_1 == 5 or hand_2 == 5:
            full_house_level += 1
            full_house[0] += 90
            full_house[1] += 4
            print("full house has been upgraded")
        if hand_1 == 6 or hand_2 == 6:
            two_trio_level += 1
            two_trio[0] += 60
            two_trio[1] += 3
            print("two trio has been upgraded.")
        if hand_1 == 7 or hand_2 == 7:
            three_of_a_kind_level += 1
            three_of_a_kind[0] += 30
            three_of_a_kind[1] += 3
            print("three of a kind has been upgraded.")
        if hand_1 == 8 or hand_2 == 8:
            four_of_a_kind_level += 1
            four_of_a_kind[0] += 40
            four_of_a_kind[1] += 4
            print("four of a kind has been upgraded.")
        if hand_1 == 9 or hand_2 == 9:
            five_of_a_kind_level += 1
            five_of_a_kind[0] += 50
            five_of_a_kind[1] += 5
            print("five of a kind has been upgraded.")
        if hand_1 == 10 or hand_2 == 10:
            six_of_a_kind_level += 1
            six_of_a_kind[0] += 60
            six_of_a_kind[1] += 6
            print("six of a kind has been upgraded.")
        else:
            overflow_house_level += 1
            overflow_house[0] += 50
            overflow_house[1] += 5
            print("overflow house has been upgraded.")
    elif souls[decision - 1] == 3:
        for i in range(0, 6, 1):
            if draws[i] == 1 or draws[i] == 11 or draws[i] == 21 or draws[i] == 31 or draws[i] == 41 or draws[i] == 51:
                contents_of_box.append(21)
            elif draws[i] == 2 or draws[i] == 12 or draws[i] == 22 or draws[i] == 32 or draws[i] == 42 or draws[i] == 52:
                contents_of_box.append(22)
            elif draws[i] == 3 or draws[i] == 13 or draws[i] == 23 or draws[i] == 33 or draws[i] == 43 or draws[i] == 51:
                contents_of_box.append(23)
            elif draws[i] == 4 or draws[i] == 14 or draws[i] == 24 or draws[i] == 34 or draws[i] == 44 or draws[i] == 54:
                contents_of_box.append(24)
            contents_of_box.remove(draws[i])
    elif souls[decision - 1] == 4:
        for i in range(0, 6, 1):
            if draws[i] == 1 or draws[i] == 11 or draws[i] == 21 or draws[i] == 31 or draws[i] == 41 or draws[i] == 51:
                contents_of_box.append(51)
            elif draws[i] == 2 or draws[i] == 12 or draws[i] == 22 or draws[i] == 32 or draws[i] == 42 or draws[i] == 52:
                contents_of_box.append(52)
            elif draws[i] == 3 or draws[i] == 13 or draws[i] == 23 or draws[i] == 33 or draws[i] == 43 or draws[i] == 51:
                contents_of_box.append(53)
            elif draws[i] == 4 or draws[i] == 14 or draws[i] == 24 or draws[i] == 34 or draws[i] == 44 or draws[i] == 54:
                contents_of_box.append(54)
            contents_of_box.remove(draws[i])
    elif souls[decision - 1] == 5:
        for i in range(0, 6, 1):
            if draws[i] == 1 or draws[i] == 11 or draws[i] == 21 or draws[i] == 31 or draws[i] == 41 or draws[i] == 51:
                contents_of_box.append(31)
            elif draws[i] == 2 or draws[i] == 12 or draws[i] == 22 or draws[i] == 32 or draws[i] == 42 or draws[i] == 52:
                contents_of_box.append(32)
            elif draws[i] == 3 or draws[i] == 13 or draws[i] == 23 or draws[i] == 33 or draws[i] == 43 or draws[i] == 51:
                contents_of_box.append(33)
            elif draws[i] == 4 or draws[i] == 14 or draws[i] == 24 or draws[i] == 34 or draws[i] == 44 or draws[i] == 54:
                contents_of_box.append(34)
            contents_of_box.remove(draws[i])
    elif souls[decision - 1] == 6:
        for i in range(0, 6, 1):
            if draws[i] == 1 or draws[i] == 11 or draws[i] == 21 or draws[i] == 31 or draws[i] == 41 or draws[i] == 51:
                contents_of_box.append(41)
            elif draws[i] == 2 or draws[i] == 12 or draws[i] == 22 or draws[i] == 32 or draws[i] == 42 or draws[i] == 52:
                contents_of_box.append(42)
            elif draws[i] == 3 or draws[i] == 13 or draws[i] == 23 or draws[i] == 33 or draws[i] == 43 or draws[i] == 51:
                contents_of_box.append(43)
            elif draws[i] == 4 or draws[i] == 14 or draws[i] == 24 or draws[i] == 34 or draws[i] == 44 or draws[i] == 54:
                contents_of_box.append(44)
            contents_of_box.remove(draws[i])
    elif souls[decision - 1] == 7:
        if 0 <= cash <= 20:
            cash *= 2
        elif cash > 20:
            cash += 20
        print("you now have", cash, "cash.")
    elif souls[decision - 1] == 8:
        for i in range(0, 6, 1):
            if draws[i] == 1:
                contents_of_box.append(2)
            elif draws[i] == 2:
                contents_of_box.append(4)
            elif draws[i] == 3:
                contents_of_box.append(1)
            elif draws[i] == 4:
                contents_of_box.append(3)

            elif draws[i] == 11:
                contents_of_box.append(12)
            elif draws[i] == 12:
                contents_of_box.append(14)
            elif draws[i] == 13:
                contents_of_box.append(11)
            elif draws[i] == 14:
                contents_of_box.append(13)

            elif draws[i] == 21:
                contents_of_box.append(22)
            elif draws[i] == 22:
                contents_of_box.append(24)
            elif draws[i] == 23:
                contents_of_box.append(21)
            elif draws[i] == 24:
                contents_of_box.append(23)

            elif draws[i] == 31:
                contents_of_box.append(32)
            elif draws[i] == 32:
                contents_of_box.append(34)
            elif draws[i] == 33:
                contents_of_box.append(31)
            elif draws[i] == 34:
                contents_of_box.append(33)

            elif draws[i] == 41:
                contents_of_box.append(42)
            elif draws[i] == 42:
                contents_of_box.append(44)
            elif draws[i] == 43:
                contents_of_box.append(41)
            elif draws[i] == 44:
                contents_of_box.append(43)

            elif draws[i] == 51:
                contents_of_box.append(52)
            elif draws[i] == 52:
                contents_of_box.append(54)
            elif draws[i] == 53:
                contents_of_box.append(51)
            elif draws[i] == 54:
                contents_of_box.append(53)
            contents_of_box.remove(draws[i])

    elif souls[decision - 1] == 9:
        for i in range(0, 6, 1):
            contents_of_box.remove(draws[i])
    for i in range(0, 6, 1):
        if souls[decision - 1] == 10:
            contents_of_box.append(15)
            contents_of_box.remove(draws[i])
        elif souls[decision - 1] == 11:
            if draws[i] == 1 or draws[i] == 2 or draws[i] == 3 or draws[i] == 4:
                contents_of_box.append(3)
            elif draws[i] == 11 or draws[i] == 12 or draws[i] == 13 or draws[i] == 14:
                contents_of_box.append(13)
            elif draws[i] == 21 or draws[i] == 22 or draws[i] == 23 or draws[i] == 24:
                contents_of_box.append(23)
            elif draws[i] == 31 or draws[i] == 32 or draws[i] == 33 or draws[i] == 34:
                contents_of_box.append(33)
            elif draws[i] == 41 or draws[i] == 42 or draws[i] == 43 or draws[i] == 44:
                contents_of_box.append(43)
            else:
                contents_of_box.append(53)
            contents_of_box.remove(draws[i])
        elif souls[decision - 1] == 12:
            if draws[i] == 1 or draws[i] == 2 or draws[i] == 3 or draws[i] == 4:
                contents_of_box.append(2)
            elif draws[i] == 11 or draws[i] == 12 or draws[i] == 13 or draws[i] == 14:
                contents_of_box.append(12)
            elif draws[i] == 21 or draws[i] == 22 or draws[i] == 23 or draws[i] == 24:
                contents_of_box.append(22)
            elif draws[i] == 31 or draws[i] == 32 or draws[i] == 33 or draws[i] == 34:
                contents_of_box.append(32)
            elif draws[i] == 41 or draws[i] == 42 or draws[i] == 43 or draws[i] == 44:
                contents_of_box.append(42)
            else:
                contents_of_box.append(52)
            contents_of_box.remove(draws[i])
        elif souls[decision - 1] == 13:
            if draws[i] == 1 or draws[i] == 2 or draws[i] == 3 or draws[i] == 4:
                contents_of_box.append(1)
            elif draws[i] == 11 or draws[i] == 12 or draws[i] == 13 or draws[i] == 14:
                contents_of_box.append(11)
            elif draws[i] == 21 or draws[i] == 22 or draws[i] == 23 or draws[i] == 24:
                contents_of_box.append(21)
            elif draws[i] == 31 or draws[i] == 32 or draws[i] == 33 or draws[i] == 34:
                contents_of_box.append(31)
            elif draws[i] == 41 or draws[i] == 42 or draws[i] == 43 or draws[i] == 44:
                contents_of_box.append(41)
            else:
                contents_of_box.append(51)
            contents_of_box.remove(draws[i])
        elif souls[decision - 1] == 14:
            if draws[i] == 1 or draws[i] == 2 or draws[i] == 3 or draws[i] == 4:
                contents_of_box.append(4)
            elif draws[i] == 11 or draws[i] == 12 or draws[i] == 13 or draws[i] == 14:
                contents_of_box.append(14)
            elif draws[i] == 21 or draws[i] == 22 or draws[i] == 23 or draws[i] == 24:
                contents_of_box.append(24)
            elif draws[i] == 31 or draws[i] == 32 or draws[i] == 33 or draws[i] == 34:
                contents_of_box.append(34)
            elif draws[i] == 41 or draws[i] == 42 or draws[i] == 43 or draws[i] == 44:
                contents_of_box.append(44)
            else:
                contents_of_box.append(54)
            contents_of_box.remove(draws[i])
        else:
            pass

def celestial_killer():
    global celestials
    print("here are your celestials; select one to replace.")
    for i in celestials:
        print(i)
    #once you finish with all celestial bodies, copy paste them all here from worm_hole_pack
    decision = int(input("1 for option 1 etc"))
    decision -= 1
    if celestials[decision] == 34:
        print("earth egg has provided cash!")
        cash += 15
    celestials[decision] = 0
    celestials.sort()

def worm_hole_pack():
    global celestials
    global max_celestials
    global popcorn
    global ice_cream
    rarity = random.randint(1, 13)
    if 1 <= rarity <= 7:
        celestial_body_1 = random.randint(1, 61)
    elif 8 <= rarity <= 11:
        celestial_body_1 = random.randint(62, 125)
    else:
        celestial_body_1 = random.randint(126, 145)
    rarity_2 = random.randint(1, 13)
    if 1 <= rarity_2 <= 7:
        celestial_body_2 = random.randint(1, 61)
    elif 8 <= rarity_2 <= 11:
        celestial_body_2 = random.randint(62, 125)
    else:
        celestial_body_2 = random.randint(126, 145)
    celestial_s = [celestial_body_1, celestial_body_2]
    for celestial_body in celestial_s:
        if celestial_body == 1:
            print("meteor - +4 mult")
        elif celestial_body == 2:
            print("greed ring - 3 mult for every d4 played")
        elif celestial_body == 3:
            print("lust ring - 2 mult for every coin played")
        elif celestial_body == 4:
            print("wrath ring - 4 mult for every d6 played")
        elif celestial_body == 5:
            print("gluttony ring - 1 mult for every sphere played")
        elif celestial_body == 6:
            print("twin star - +8 mult if played hand is not a high die")
        elif celestial_body == 7:
            print("triplet star - +12 mult if played hand contains a three of a kind")
        elif celestial_body == 8:
            print("two sun two moon - +10 mult if played hand contains a two pair")
        elif celestial_body == 9:
            print("stardust - +12 mult if played hand is a high die")
        elif celestial_body == 10:
            print("square star - +16 mult played if hand contains a four of a kind")
        elif celestial_body == 11:
            print("twin moon - +50 pupils if played hand is not a high die")
        elif celestial_body == 12:
            print("triplet moon - +100 pupils if played hand contains a three of a kind")
        elif celestial_body == 13:
            print("two moon two sun - +80 pupils if played hand contains two pair")
        elif celestial_body == 14:
            print("moondust - +100 pupils if played hand is a high die")
        elif celestial_body == 15:
            print("square moon - +200 pupils if hand contains four of a kind")
        elif celestial_body == 16:
            print("meteor field - 8 - 180 pupils")
        elif celestial_body == 17:
            print("wishing star - +30 pupils")
        elif celestial_body == 18:
            print("cold star - +30 chips for each remaining discard")
        elif celestial_body == 19:
            print("gravity-less planet - 15 mult when no discards remaining.")
        elif celestial_body == 20:
            print("sunlight - 2$ for every hand played, 0.1% chance of self destruction")
        elif celestial_body == 21:
            print("glitch in space and time - >32£½#25%^'+½5#<")
        elif celestial_body == 22:
            print("USA flag - +4 mult for every remaining discard")
        elif celestial_body == 23:
            print("NASA - +220 pupils, 0.1% chance of self destruction")
        elif celestial_body == 24:
            print("saturn - 23 pupils for each celestial body.")
        elif celestial_body == 25:
            print("jupiter - 3 mult for each celestial body.")
        elif celestial_body == 26:
            print("delay in gravity - if you did not discard any die this sun, gain cash double your maximum discards.")
        elif celestial_body == 27:
            print("pluto - +15 mult. 0.1% chance of self destruction")
        elif celestial_body == 28:
            print("even stars - +4 mult for each even roll")
        elif celestial_body == 29:
            print("odd stars out of the galaxy - +31 pupils for every odd roll")
        elif celestial_body == 30:
            print("colletzes law - each rolled 4, 2 or 1 gives 4 mult")
        elif celestial_body == 31:
            print("oops! all 1's - 1's give 3 mult.")
        elif celestial_body == 32:
            print("supernova - adds the number of times hand has been played this run to mult.")
        elif celestial_body == 33:
            print("galaxy o bill - 3 mult for every 3 rolled")
        elif celestial_body == 34:
            print("earth egg - provides 15$ when destroyed")
        elif celestial_body == 35:
            print("spaceship - provides 15 pupils for everytime high die has been played this run")
        elif celestial_body == 36:
            print("none can hear you scream - +100 pupils. slowly loses value.")
        elif celestial_body == 37:
            print("hybrid planet - +8 pupils for every gem used this run.")
        elif celestial_body == 38:
            print("neptune - gives more pupils depending on how big your deck is.")
        elif celestial_body == 39:
            print("brainstorm - 1 in 2 chance of 15 mult.")
        elif celestial_body == 40:
            print("acid rain - more mult for the hands you play, less for the hands you discard.")
        elif celestial_body == 41:
            print("addiction - if roll is 6, gain 1 in $.")
        elif celestial_body == 42:
            print("space route - 1 in 11 chance to earn 4$ after playing hand.")
        elif celestial_body == 43:
            print("radioactive moon - 3x mult, 1 in 5 chance of self destruction")
        elif celestial_body == 44:
            print("place_holder_does_nothing")
        elif celestial_body == 45:
            print("place_holder_does_nothing")
        elif celestial_body == 46:
            print("place_holder_does_nothing")
        elif celestial_body == 47:
            print("place_holder_does_nothing")
        elif celestial_body == 48:
            print("place_holder_does_nothing")
        elif celestial_body == 49:
            print("place_holder_does_nothing")
        elif celestial_body == 50:
            print("all the stars - provides 1 mult for each soul card played.")
        elif celestial_body == 51:
            print("place_holder_does_nothing")
        elif celestial_body == 52:
            print("golden planet - gives 4 cash at the end of round.")
        elif celestial_body == 53:
            print("in space - +20 mult. slowly loses value.")
        elif celestial_body == 54:
            print("place_holder_does_nothing")
        elif celestial_body == 55:
            print("hosyk - ")
        elif celestial_body == 56:
            print("place_holder_does_nothing")
        elif celestial_body == 57:
            print("discardiun planet - +1 discard")
        elif celestial_body == 58:
            print("rollium planet - +1 roll")
        elif celestial_body == 59:
            print("place_holder_does_nothing")
        elif celestial_body == 60:
            print("place_holder_does_nothing")
        elif celestial_body == 61:
            print("place_holder_does_nothing")
        elif celestial_body == 62:
            print("the pipe strip - in third hand of sun, x3 mult.")
        elif celestial_body == 63:
            print("fourth dimension - pairs and three of a kinds are now a high die.")
        elif celestial_body == 64:
            print("reverse mitosis - +5 mult for every gravity pack opened.")
        elif celestial_body == 65:
            print("oops! all sixes - sixes give 60 pupils.")
        elif celestial_body == 66:
            print("space reptile - 75 chips for every eye that you have.")
        elif celestial_body == 67:
            print("stone planet - adds a stone die to box at the start of round.")
        elif celestial_body == 68:
            print("royal planet - x4 mult every 6 hands played.")
        elif celestial_body == 69:
            print("steel moon - turns hand into pins if they dont have stickers.")
        elif celestial_body == 70:
            print("Space vending machine - +10 mult for every eye that you have.")
        elif celestial_body == 71:
            print("steel planet - +x0.1 mult for every pinned die you have in your full box.")
        elif celestial_body == 72:
            print("chemical x - x1.5 mult")
        elif celestial_body == 73:
            print("place_holder_does_nothing")
        elif celestial_body == 74:
            print("astronaut - 1 in 4 chance of upgrading hand played.")
        elif celestial_body == 75:
            print("space burglar - multiply discards by zero, and add 3 to hands.")
        elif celestial_body == 76:
            print("dark matter - if hand contains only d6 and d1's, x3 mult.")
        elif celestial_body == 77:
            print("place_holder_does_nothing")
        elif celestial_body == 78:
            print("constelletion - +x0.1 mult for every level up on all hands.")
        elif celestial_body == 79:
            print("place_holder_does_nothing")
        elif celestial_body == 80:
            print("sharp sun - x3 mult if hand type has already been played this sun.")
        elif celestial_body == 81:
            print("place_holder_does_nothing")
        elif celestial_body == 82:
            print("place_holder_does_nothing")
        elif celestial_body == 83:
            print("blood moon - +x0.1 permanent mult for every stickered die. removes stickers.")
        elif celestial_body == 84:
            print("place_holder_does_nothing")
        elif celestial_body == 85:
            print("illusion of light - +x0.25 mult for everytime a die has been added to your deck.")
        elif celestial_body == 86:
            print("place_holder_does_nothing")
        elif celestial_body == 87:
            print("rocket - gives money depending on ante.")
        elif celestial_body == 88:
            print("place_holder_does_nothing")
        elif celestial_body == 89:
            print("place_holder_does_nothing")
        elif celestial_body == 90:
            print("place_holder_does_nothing")
        elif celestial_body == 91:
            print("rusty planet - gives mult depending on how small your deck is.")
        elif celestial_body == 92:
            print("to the moon - doubles interest")
        elif celestial_body == 93:
            print("stone moon - gives 25 chips per stone in your deck.")
        elif celestial_body == 94:
            print("lucky star - gives +x0.25 mult for every time a lucky die has been triggered.")
        elif celestial_body == 95:
            print("bull - gives pupils double your money")
        elif celestial_body == 96:
            print("place_holder_does_nothing")
        elif celestial_body == 97:
            print("place_holder_does_nothing")
        elif celestial_body == 98:
            print("place_holder_does_nothing")
        elif celestial_body == 99:
            print("meteor-U - gives double the amount of times a hand with two pair has been played to mult.")
        elif celestial_body == 100:
            print("space food - +x2 mult. loses 0.06 value after discard.")
        elif celestial_body == 101:
            print("place_holder_does_nothing")
        elif celestial_body == 102:
            print("place_holder_does_nothing")
        elif celestial_body == 103:
            print("death star - saves you from death once")
        elif celestial_body == 104:
            print("space gun - x3 times mult on final hand of sun.")
        elif celestial_body == 105:
            print("place_holder_does_nothing")
        elif celestial_body == 106:
            print("place_holder_does_nothing")
        elif celestial_body == 107:
            print("rocket science certificate - adds a random stickered die to your deck every sun")
        elif celestial_body == 108:
            print("place_holder_does_nothing")
        elif celestial_body == 109:
            print("place_holder_does_nothing")
        elif celestial_body == 110:
            print("diamond meteor - +1 in cash for every d4 played.")
        elif celestial_body == 111:
            print("scenario: iron lung - 50% chance coins give +x1.5 mult.")
        elif celestial_body == 112:
            print("space directions - +50 chips for each played d6")
        elif celestial_body == 113:
            print("dimension zero - 7 mult for every played sphere.")
        elif celestial_body == 114:
            print("glass planet - x0.75 mult for everytime a badge die dies")
        elif celestial_body == 115:
            print("place_holder_does_nothing")
        elif celestial_body == 116:
            print("place_holder_does_nothing")
        elif celestial_body == 117:
            print("place_holder_does_nothing")
        elif celestial_body == 118:
            print("place_holder_does_nothing")
        elif celestial_body == 119:
            print("place_holder_does_nothing")
        elif celestial_body == 120:
            print("rift - if hand has a sphere but not all spheres, x2 mult.")
        elif celestial_body == 121:
            print("space cowboy - who knows?")
        elif celestial_body == 122:
            print("satalite - gain 1$ at the end of round for every hand level above 1.")
        elif celestial_body == 123:
            print("place_holder_does_nothing")
        elif celestial_body == 124:
            print("space rock - gem packs are free.")
        elif celestial_body == 125:
            print("space boot - for every 5$, every hand gets 2 mult.")
        elif celestial_body == 126:
            print("paraoh planet - if cash is over 40, +x3 mult.")
        elif celestial_body == 127:
            print("the golden sun - +x4 mult if deck has exactly 52 die")
        elif celestial_body == 128:
            print("place_holder_does_nothing")
        elif celestial_body == 129:
            print("place_holder_does_nothing")
        elif celestial_body == 130:
            print("place_holder_does_nothing")
        elif celestial_body == 131:
            print("place_holder_does_nothing")
        elif celestial_body == 132:
            print("place_holder_does_nothing")
        elif celestial_body == 133:
            print("duo - x2 mult if hand is not a high die.")
        elif celestial_body == 134:
            print("trio - x3 mult if hand contains three of a kind.")
        elif celestial_body == 135:
            print("quadro - x4 mult if hand contains four of a kind.")
        elif celestial_body == 136:
            print("cinq - x5 mult if hand contains five of a kind.")
        elif celestial_body == 137:
            print("law of space - x3 mult if hand is a high die.")
        elif celestial_body == 138:
            print("place_holder_does_nothing")
        elif celestial_body == 139:
            print("place_holder_does_nothing")
        elif celestial_body == 140:
            print("place_holder_does_nothing")
        elif celestial_body == 141:
            print("license of something - x3 mult if at least 16 die in deck has stickers")
        elif celestial_body == 142:
            print("place_holder_does_nothing")
        elif celestial_body == 143:
            print("place_holder_does_nothing")
        elif celestial_body == 144:
            print("place_holder_does_nothing")
        else:
            print("place_holder_does_nothing")
    try:
        decision = int(input("1 for option 1, 2 for option 2, 0 to skip."))
    except:
        print("skipped.")
        return 0
    if decision == 0:
        return 0
    elif decision == 1:
        celestials.append(celestial_body_1)
        celestial_body_chosen = celestial_body_1
    else:
        celestials.append(celestial_body_2)
        celestial_body_chosen = celestial_body_2
    if celestial_body_chosen == 36:
        ice_cream = 100
    elif celestial_body_chosen == 53:
        popcorn = 20

def gravity_pack():
    global contents_of_box
    global cash
    global high_die_level
    global pair_level
    global two_pair_level
    global three_pair_level
    global full_house_level
    global three_of_a_kind_level
    global four_of_a_kind_level
    global five_of_a_kind_level
    global six_of_a_kind_level
    global two_trio_level
    global overflow_house_level
    global gravity_played
    gravity_played += 5
    gravity_1 = random.randint(1,5)
    gravity_2 = random.randint(1, 5)
    gravities = [gravity_1, gravity_2]
    draw_1 = random.randint(0, len(contents_of_box) - 1)
    draw_2 = random.randint(0, len(contents_of_box) - 1)
    draw_3 = random.randint(0, len(contents_of_box) - 1)
    draw_4 = random.randint(0, len(contents_of_box) - 1)
    draw_5 = random.randint(0, len(contents_of_box) - 1)
    draw_6 = random.randint(0, len(contents_of_box) - 1)
    draws = []
    draw_1 = contents_of_box[draw_1]
    draw_2 = contents_of_box[draw_2]
    draw_3 = contents_of_box[draw_3]
    draw_4 = contents_of_box[draw_4]
    draw_5 = contents_of_box[draw_5]
    draw_6 = contents_of_box[draw_6]
    draws.append(draw_1)
    draws.append(draw_2)
    draws.append(draw_3)
    draws.append(draw_4)
    draws.append(draw_5)
    draws.append(draw_6)

    for i in draws:
        if i == 1:
            print("norm die")
        elif i == 2:
            print("d1")
        elif i == 3:
            print("d4")
        elif i == 4:
            print("coin")
        elif i == 11:
            print("lucky die")
        elif i == 12:
            print("lucky d1")
        elif i == 13:
            print("lucky d4")
        elif i == 14:
            print("lucky coin")
        elif i == 21:
            print("mult die")
        elif i == 22:
            print("mult d1")
        elif i == 23:
            print("mult d4")
        elif i == 24:
            print("mult coin")
        elif i == 31:
            print("pinned die")
        elif i == 32:
            print("pinned d1")
        elif i == 33:
            print("pinned d4")
        elif i == 34:
            print("pinned coin")
        elif i == 41:
            print("badge die")
        elif i == 42:
            print("badge d1")
        elif i == 43:
            print("badge d4")
        elif i == 44:
            print("badge coin")
        elif i == 51:
            print("bonus die")
        elif i == 52:
            print("bonus d1")
        elif i == 53:
            print("bonus d4")
        elif i == 54:
            print("bonus coin")
        elif i == 15:
            print("stone")
    for i in gravities:
        if i == 1:
            print("black holish - creates a random rare celestial body, but sets money to zero.")
        elif i == 2:
            print("magical forces - turns all die in hand to a random die.")
        elif i == 3:
            print("supernova - destroys hand. gain 20 in cash.")
        elif i == 4:
            print("pull of death - select a celestial body. copy it and destroy all others.")
        elif i == 5:
            print("pull of curiosity - copies all cards in hand.")
        elif i == 6:
            print("pull of cash - upgrades every hand by one")
        else:
            print("pull of life - creates a random legendary celestial body")
    decision = int(input("1 for option one etc. 0 to skip"))
    if gravities[decision - 1] == 1:
        pass
    elif gravities[decision - 1] == 2:
        random_die = random.randint(1, 4)
        if random_die == 1:
            print("d6")
        elif random_die == 2:
            print("d1")
        elif random_die == 3:
            print("d4")
        else:
            print("coin")
        for seven in range(0, 6, 1):
            if draws[i] == 1 or draws[i] == 2 or draws[i] == 3 or draws[i] == 4:
                contents_of_box.append(random_die)
            elif draws[i] == 11 or draws[i] == 12 or draws[i] == 13 or draws[i] == 14:
                contents_of_box.append(random_die + 10)
            elif draws[i] == 21 or draws[i] == 22 or draws[i] == 23 or draws[i] == 24:
                contents_of_box.append(random_die + 20)
            elif draws[i] == 31 or draws[i] == 32 or draws[i] == 33 or draws[i] == 34:
                contents_of_box.append(random_die + 30)
            elif draws[i] == 41 or draws[i] == 42 or draws[i] == 43 or draws[i] == 44:
                contents_of_box.append(random_die + 40)
            else:
                contents_of_box.append(random_die + 50)
        contents_of_box.remove(draws[0])
        contents_of_box.remove(draws[1])
        contents_of_box.remove(draws[2])
        contents_of_box.remove(draws[3])
        contents_of_box.remove(draws[4])
        contents_of_box.remove(draws[5])

    elif gravities[decision - 1] == 3:
        for i in range(0, 6, 1):
            contents_of_box.remove(draws[i])
        cash += 5
        print("you now have", cash, "cash.")
    elif gravities[decision - 1] == 4:
        pass
    elif gravities[decision - 1] == 5:
        for i in draws:
            contents_of_box.append(i)
        die_added += 6
    elif gravities[decision - 1] == 6:
        high_die_level += 1
        high_die[0] += 120
        high_die[1] += 12
        pair_level += 1
        high_die[0] += 20
        high_die[1] += 2
        two_pair_level += 1
        two_pair[0] += 40
        two_pair[1] += 2
        three_pair_level += 1
        three_pair[0] += 60
        three_pair[1] += 2
        full_house_level += 1
        full_house[0] += 90
        full_house[1] += 4
        two_trio_level += 1
        two_trio[0] += 60
        two_trio[1] += 3
        three_of_a_kind_level += 1
        three_of_a_kind[0] += 30
        three_of_a_kind[1] += 3
        four_of_a_kind_level += 1
        four_of_a_kind[0] += 40
        four_of_a_kind[1] += 4
        five_of_a_kind_level += 1
        five_of_a_kind[0] += 50
        five_of_a_kind[1] += 5
        six_of_a_kind_level += 1
        six_of_a_kind[0] += 60
        six_of_a_kind[1] += 6
        overflow_house_level += 1
        overflow_house[0] += 50
        overflow_house[1] += 5
        print("every hand has been upgraded by one.")
    elif gravities[decision - 1] == 7:
        if len(celestials) != max_celestials:
            celestial_killer()
        celestial_body = random.randint(146, 150)
        if celestial_body == 146:
            print("ceres - +250 pupils for every 3 times you roll.")
        elif celestial_body == 147:
            print("Remina - +x1 mult for every eye that you have")
        elif celestial_body == 148:
            print("planet x - +x1 mult for every 4 times you discard.")
        elif celestial_body == 149:
            print("eris - disables effect of every boss sun")
        else:
            print("")
        celestials.append(celestial_body)
    elif decision == 0:
        return 0







def shop_eye():
    global a
    global eye
    global eyes
    global cash
    global max_celestials
    global discard_max
    global roll_max
    global ante
    print("cash is", cash)
    if len(eyes) == 11:
        return 0
    print("you have entered the shop!")
    try:
        if eye == 0:
            return 0
    except NameError:
        pass
    if a == 1:
        z = random.randint(1, 11)
        if z == 1:
            print("third eye - shop will have an additional pack waiting for you.")
        elif z == 2:
            print("cheapskates eye - all products are 25% off!")
        elif z == 3:
            print("lucky eye - die from packs will always have stickers!")
        elif z == 4:
            print("eye of the beholder - does nothing.")
        elif z == 5:
            print("emerald eye - gem packs always contain the gem for your most played hand, but will also automatically select it.")
        elif z == 6:
            print("hen die - +1 roll")
        elif z == 7:
            print("bat eye - +1 discard")
        elif z == 8:
            print("golden eye - increases interest cap. ")
        elif z == 9:
            print("blind eye - +1 celestial body slot")
        elif z == 10:
            print("baby eye - ante -= 1, rolls -= 1")
        else:
            print("elder eye - ante -= 1, discards -= 1")
        if z in eyes:
            print("error. recalculating shop...")
            shop_eye()
            return 0
        eye = z
    if cash >= 10:
        d = int(input("press 1 to purchase the eye."))
        if d == 1:
            eyes.append(eye)
            eye = 0
            if 2 in eyes:
                cash -= 7
            else:
                cash -= 10
            print("you now have", cash, "cash.")
            if eye == 6:
                roll_max += 1
            elif eye == 7:
                discad_max += 1
            elif eye == 9:
                max_celestials += 1
            elif eye == 10:
                ante -= 1
                roll_max -= 1
            elif eye == 11:
                ante -= 1
                discard_max -= 1


def shop_packs():
    global cash
    global eyes
    print("you are in the pack aisle.")
    pack_1 = random.randint(1,5)
    pack_2 = random.randint(1, 5)
    if pack_1 == 1:
        print("the first pack you may purchase is... a die pack! guess whats in it.")
    elif pack_1 == 2:
        print("the first pack you may purchase is... a gem pack! it upgrades your hands.")
    elif pack_1 == 3:
        print("the first pack you may purchase is... a soul pack! souls can do all sorts of things!")
    elif pack_1 == 4:
        print("the first pack you may purchase is... a wormhole pack! i wonder where it leads to?")
    else:
        print("the first pack you may purchase is... a gravity pack! itll do 7 wonders, but at a cost. and money.")
    decision = int(input("press 1 to purchase this pack."))
    if decision == 1 and cash >= 4:
        if pack_1 == 1:
            die_pack()
            cash -= 4
            if 2 in eyes:
                cash += 1
        elif pack_1 == 2:
            if 124 not in celestials:
                cash -= 4
                if 2 in eyes:
                    cash += 1
            if 5 in eyes:
                emerald_eye()
            else:
                gem_pack()
        elif pack_1 == 3:
            soul_pack()
            cash -= 4
            if 2 in eyes:
                cash += 1
        elif pack_1 == 4:
            worm_hole_pack()
            cash -= 4
            if 2 in eyes:
                cash += 1
        else:
            gravity_pack()
            cash -= 4
            if 2 in eyes:
                cash += 1
    if pack_2 == 1:
        print("the second pack you may purchase is... a die pack! guess whats in it.")
    elif pack_2 == 2:
        print("the second pack you may purchase is... a gem pack! it upgrades your hands.")
    elif pack_2 == 3:
        print("the second pack you may purchase is... a soul pack! souls can do all sorts of things!")
    elif pack_2 == 4:
        print("the second pack you may purchase is... a wormhole pack! i wonder where it leads to?")
    else:
        print("the second pack you may purchase is... a gravity pack! itll do 7 wonders, but at a cost. and money.")
    decision = int(input("press 1 to purchase this pack."))
    if decision == 1 and cash >= 4:
        if pack_2 == 1:
            die_pack()
            cash -= 4
            if 2 in eyes:
                cash += 1
        elif pack_2 == 2:
            if 124 not in celestials:
                cash -= 4
                if 2 in eyes:
                    cash += 1
            if 5 in eyes:
                emerald_eye()
            else:
                gem_pack()
        elif pack_2 == 3:
            soul_pack()
            cash -= 4
            if 2 in eyes:
                cash += 1
        elif pack_2 == 4:
            worm_hole_pack()
            cash -= 4
            if 2 in eyes:
                cash += 1
        else:
            gravity_pack()
            cash -= 4
            if 2 in eyes:
                cash += 1
    if 1 in eyes:
        pack_3 = random.randint(1, 5)
        if pack_3 == 1:
            print("the third pack you may purchase is... a die pack! guess whats in it.")
        elif pack_3 == 2:
            print("the third pack you may purchase is... a gem pack! it upgrades your hands.")
        elif pack_3 == 3:
            print("the third pack you may purchase is... a soul pack! souls can do all sorts of things!")
        elif pack_3 == 4:
            print("the third pack you may purchase is... a wormhole pack! i wonder where it leads to?")
        else:
            print("the third pack you may purchase is... a gravity pack! itll do 7 wonders, but at a cost. and money.")
        decision = int(input("press 1 to purchase this pack."))
        if decision == 1 and cash >= 4:
            if pack_3 == 1:
                die_pack()
                cash -= 4
                if 2 in eyes:
                    cash += 1
            elif pack_3 == 2:
                if 124 not in celestials:
                    cash -= 4
                    if 2 in eyes:
                        cash += 1
                if 5 in eyes:
                    emerald_eye()
                else:
                    gem_pack()
            elif pack_3 == 3:
                soul_pack()
                cash -= 4
                if 2 in eyes:
                    cash += 1
            elif pack_3 == 4:
                worm_hole_pack()
                cash -= 4
                if 2 in eyes:
                    cash += 1
            else:
                gravity_pack()
                cash -= 4
                if 2 in eyes:
                    cash += 1


def poker_hand_inator(f):
    global celestials
    y = Counter(f)
    y = y.values()
    y = sorted(y, reverse=True)
    if y == [1, 1, 1, 1, 1, 1] or y == [1, 1, 1, 1, 1] or y == [1, 1, 1, 1] or y == [1, 1, 1] or y == [1, 1] or y == [1] or y == []:
        return 1
    if y == [2, 1, 1, 1, 1] or y == [2, 1, 1, 1] or y == [2, 1, 1] or y == [2, 1, 1] or y == [2, 1] or y == [2]:
        if 63 in celestials:
            return 1
        else:
            return 2
    if y == [2, 2, 1, 1] or y == [2, 2, 1] or y == [2, 2]:
        return 3
    if y == [2, 2, 2]:
        return 4
    if y == [3, 2, 1] or y == [3, 2]:
        return 5
    if y == [3, 3]:
        return 6
    if y == [3, 1, 1, 1] or y == [3, 1, 1] or y == [3, 1] or y == [3]:
        if 63 in celestials:
            return 1
        else:
            return 7
    if y == [4, 1, 1] or y == [4, 1] or y == [4]:
        return 8
    if y == [5, 1] or y == [5]:
        return 9
    if y == [6]:
        return 10
    else: #overflow house
        return 11

def blinds(b):
    if b == 3:
        a = random.randint(1, 28)
        if a == 1:
            print("the hook - minus 2 mult on every hand you play")
        elif a == 2:
            print("the ox - playing your most played hand this run sets money to zero")
        elif a == 3:
            print("the house - first hand is discarded")
        elif a == 4:
            print("the wall - extra large blind")
        elif a == 5:
            print("the wheel - 1 in 6 chance hand dosent score")
        elif a == 6:
            print("the arm - decrease level of played hand")
        elif a == 7:
            print("the pyramid - all d4's are debuffed")
        elif a == 8:
            print("the fish - discard the next hand after rolling")
        elif a == 9:
            print("the psychic - first die will roll a 1")
        elif a == 10:
            print("the sphere - all d1's are debuffed")
        elif a == 11:
            print("the water - start with 0 discards")
        elif a == 12:
            print("the dice - all d6's are debuffed")
        elif a == 13:
            print("the manacle - last die will roll a 1")
        elif a == 14:
            print("the eye - hand dosent score if its already been played this round")
        elif a == 15:
            print("the mouth - hand dosent score if it dosent match the last hand played this round (first hand is fine)")
        elif a == 16:
            print("the plant - all die with a sticker are debuffed")
        elif a == 17:
            print("the serpent - if hand has a trio or higher, it does not score")
        elif a == 18:
            print("the pillar - ERROR: no effects because i do not want to code whats supposed to be here")
        elif a == 19:
            print("the needle - play only one hand")
        elif a == 20:
            print("the head - all coins are debuffed")
        elif a == 21:
            print("the tooth - lose 6$ per hand played")
        elif a == 22:
            print("the flint - base score is halved")
        elif a == 23:
            print("the mark - if hand is six sixes, lose. ")
        elif a == 24:
            print("amber acorn - hand level is assumed to be 1")
        elif a == 25:
            print("verdant leaf - destroy 1 celestial body.")
        elif a == 26:
            print("violet vessel - very large blind")
        elif a == 27:
            print("crimson heart - one random joker disabled every round")
        else:
            print("cerulean bell - nothing. yet.")
        return a
    else:
        if b == 1:

            print("small sun")
        else:
            print("medium sun")

if __name__ == "__main__":
    print("red box gives an additional discard")
    print("blue box gives and additional roll")
    print("yellow box starts with an additional 10$")
    print("green box makes it so at the end of each round: 2$ per remaining hand, 1$ per remaining discard, but no intrest.")
    print("black deck provides an additional celestial slot.")
    print("nebula box starts with an emerald eye")
    print("checkered deck starts with 26 d4's and 26 d1's")
    while True:
        try:
            box = int(input("0 = red box, 1 = blue box, 2 = yellow box, 3 = green box, 4 = black box, 5 = nebula deck, 6 = checkered deck"))
        except ValueError:
            continue
        finally:
            break
    decision_balance = 0
    luck = 1
    orbs = [2, 12, 22, 32, 42, 52]
    gravity_played = 0
    blood = 1
    die_added = 0
    space_food = 200
    glass = 1
    planet_x = 1
    onefoureight = 0
    ceres = 0
    ceres_rolls = 0
    if box == 0:
        discard_max = 4
    else:
        discard_max = 3
    royal = 0
    if box == 1:
        roll_max = 4
    else:
        roll_max = 3
    souls_played = 0
    eyes = []
    if box == 5:
        eyes.append(5)
    cash = 4
    if box == 2:
        cash += 10
    # 1 equals norm die,
    # 2 equals norm d1,
    # 3 equals norm d4,
    # 4 equals norm coin.
    contents_of_box = []
    if box != 6:
        contents_of_box.append(1)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(4)
        contents_of_box.append(1)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(4)
        contents_of_box.append(1)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(4)
        contents_of_box.append(1)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(4)
        contents_of_box.append(1)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(4)
        contents_of_box.append(1)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(4)
        contents_of_box.append(1)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(4)
        contents_of_box.append(1)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(4)
        contents_of_box.append(1)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(4)
        contents_of_box.append(1)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(4)
        contents_of_box.append(1)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(4)
        contents_of_box.append(1)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(4)
        contents_of_box.append(1)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(4)
    else:
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(2)
        contents_of_box.append(3)
        contents_of_box.append(2)
        contents_of_box.append(3)
    random.shuffle(contents_of_box)

    high_die_level = 1
    pair_level = 1
    two_pair_level = 1
    three_pair_level = 1
    full_house_level = 1
    two_trio_level = 1
    three_of_a_kind_level = 1
    four_of_a_kind_level = 1
    five_of_a_kind_level = 1
    six_of_a_kind_level = 1
    overflow_house_level = 1

    #pupils, mult
    high_die = [120, 12]
    pair =  [20, 2]
    two_pair = [40, 2]
    three_pair = [60, 2]
    full_house = [90, 4]
    two_trio = [60, 3]
    three_of_a_kind = [30, 3]
    four_of_a_kind = [40, 4]
    five_of_a_kind = [50, 5]
    six_of_a_kind = [60, 6]
    overflow_house = [50, 5]

    high_die_played = 1
    pair_played = 1
    two_pair_played = 1
    three_pair_played = 1
    full_house_played = 1
    two_trio_played = 1
    three_of_a_kind_played = 1
    four_of_a_kind_played = 1
    five_of_a_kind_played = 1
    six_of_a_kind_played = 1
    overflow_house_played = 1

    celestials = []
    max_celestials = 5
    if box == 4:
        max_celestials = 6

    ante_minus = 37.5
    ante_0 = 75
    ante_1 = 150
    ante_2 = 300
    ante_3 = 600
    ante_4 = 1200
    ante_5 = 2400
    ante_6 = 4800
    ante_7 = 9600
    ante_8 = 19200
    ante_10 = 38400
    ante_11 = 76800
    ante_12 = 152000

    ante = 1

    while True:
        #ante loop
        for a in range(1,4,1):
            if 67 in celestials:
                contents_of_box.append(15)
                die_added += 1
                print("stone planet has done its thing.")
            if 107 in celestials:
                z = random.randint(1, 6)
                if z == 1:
                    z = random.randint(1, 4)
                    if z == 1:
                        print("lucky d6")
                        contents_of_box.append(11)
                    elif z == 2:
                        print("lucky d1")
                        contents_of_box.append(12)
                    elif z == 3:
                        print("lucky d4")
                        contents_of_box.append(13)
                    else:
                        print("lucky coin")
                        contents_of_box.append(14)
                elif z == 2:
                    z = random.randint(1, 4)
                    if z == 1:
                        print("mult d6")
                        contents_of_box.append(21)
                    elif z == 2:
                        print("mult d1")
                        contents_of_box.append(22)
                    elif z == 3:
                        print("mult d4")
                        contents_of_box.append(23)
                    else:
                        print("mult coin")
                        contents_of_box.append(24)
                elif z == 3:
                    z = random.randint(1, 4)
                    if z == 1:
                        print("pinned d6")
                        contents_of_box.append(31)
                    elif z == 2:
                        print("pinned d1")
                        contents_of_box.append(32)
                    elif z == 3:
                        print("pinned d4")
                        contents_of_box.append(33)
                    else:
                        print("pinned coin")
                        contents_of_box.append(34)
                elif z == 4:
                    z = random.randint(1, 4)
                    if z == 1:
                        print("badged d6")
                        contents_of_box.append(41)
                    elif z == 2:
                        print("badged d1")
                        contents_of_box.append(42)
                    elif z == 3:
                        print("badged d4")
                        contents_of_box.append(43)
                    else:
                        print("badged coin")
                        contents_of_box.append(44)
                elif z == 5:
                    z = random.randint(1, 4)
                    if z == 1:
                        print("bonus d6")
                        contents_of_box.append(51)
                    elif z == 2:
                        print("bonus d1")
                        contents_of_box.append(52)
                    elif z == 3:
                        print("bonus d4")
                        contents_of_box.append(53)
                    else:
                        print("bonus coin")
                        contents_of_box.append(54)
                else:
                    print("stone")
                    contents_of_box.append(15)
            score = 0
            current_box = contents_of_box.copy()
            random.shuffle(current_box)
            sharp = []
            stone_pupils = 0
            if a != 3:
                blinds(a)
                #deciding pupils needed
                if ante == -1:
                    b = ante_minus
                elif ante == 0:
                    b = ante_0
                elif ante == 1:
                    b = ante_1
                elif ante == 2:
                    b = ante_2
                elif ante == 3:
                    b = ante_3
                elif ante == 4:
                    b = ante_4
                elif ante == 5:
                    b = ante_5
                elif ante == 6:
                    b = ante_6
                elif ante == 7:
                    b = ante_7
                elif ante == 8:
                    b = ante_8
                elif ante == 9:
                    b = ante_9
                elif ante == 10:
                    b = ante_10
                elif ante == 11:
                    b = ante_11
                else:
                    b = ante_12
                if a == 2:
                    b *= 1.5
                print("No special effects, pupils needed is", b)
                mult = 0
                pupils = 0
                #combat
                while True:
                    roll = []
                    hand_of_round = 0
                    rolls = roll_max
                    discards = discard_max
                    if 57 in celestials:
                        discards += 1
                    if 58 in celestials:
                        rolls += 1
                    if 75 in celestials:
                        discards = 0
                        rolls += 3
                        print("space burglar has done its thing.")
                    print("you have", discards, "discards.")
                    print("you have", rolls, "rolls.")
                    try:
                        for i in range(0,6,1):
                            roll.append(current_box[0])
                            current_box.pop(0)
                    except IndexError:
                        print("your deck ran out. you know what they say, the house always wins!")
                        if 103 in celestials:
                            print("mr. death star has jumped in front of the bullet.")
                            celestials.remove(103)
                            break
                        else:
                            exit()
                    print("Hand is:")
                    for i in roll:
                        if i == 1:
                            print("normal die")
                        if i == 2:
                            print("normal sphere")
                        if i == 3:
                            print("normal d4")
                        if i == 4:
                            print("normal coin")
                        elif i == 11:
                            print("lucky die")
                        elif i == 12:
                            print("lucky d1")
                        elif i == 13:
                            print("lucky d4")
                        elif i == 14:
                            print("lucky coin")
                        elif i == 21:
                            print("mult die")
                        elif i == 22:
                            print("mult d1")
                        elif i == 23:
                            print("mult d4")
                        elif i == 24:
                            print("mult coin")
                        elif i == 31:
                            print("pinned die")
                        elif i == 32:
                            print("pinned d1")
                        elif i == 33:
                            print("pinned d4")
                        elif i == 34:
                            print("pinned coin")
                        elif i == 41:
                            print("badge die")
                        elif i == 42:
                            print("badge d1")
                        elif i == 43:
                            print("badge d4")
                        elif i == 44:
                            print("badge coin")
                        elif i == 51:
                            print("bonus die")
                        elif i == 52:
                            print("bonus d1")
                        elif i == 53:
                            print("bonus d4")
                        elif i == 54:
                            print("bonus coin")
                        elif i == 15:
                            print("stone")
                    if rolls == 0:
                        print("im literally a fool, whats your excuse?")
                        if 103 in celestials:
                            print("mr. death star has jumped in front of the bullet.")
                            celestials.remove(103)
                            break
                        else:
                            exit()
                    if discards == 0:
                        print("no discards. hand rolling automatically...")
                        decision = 1
                        decision_balance += 1
                    else:
                        decision = int(input("1 to roll, 2 to discard."))
                    if decision == 2:
                        print("discarding...")
                        discards -= 1
                        decision_balance -= 1
                        if onefoureight == 4:
                            planet_x += 1
                            onefoureight = 0
                        else:
                            onefoureight += 1
                        if 100 in celestials:
                            space_food -= 6
                            if space_food < 100:
                                celestials.remove(100)
                                print("space food has ran out.")
                        continue
                    else:
                        print("hand playing protocol starting...")
                        if ceres_rolls == 3:
                            ceres = 0
                            ceres += 250
                        else:
                            ceres += 1
                        if royal != 6:
                            royal += 1
                        else:
                            royal = 0
                        dies = []
                        decision_balance += 1
                        for z in range(0, 6, 1):
                            if roll[0] == 1 or roll[0] == 11 or roll[0] == 21 or roll[0] == 31 or roll[0] == 41 or roll[0] == 51:
                                e = random.randint(1,6)
                            elif roll[0] == 2 or roll[0] == 12 or roll[0] == 22 or roll[0] == 32 or roll[0] == 42 or roll[0] == 52:
                                e = 3
                            elif roll[0] == 3 or roll[0] == 13 or roll[0] == 23 or roll[0] == 33 or roll[0] == 43 or roll[0] == 53:
                                c = random.randint(1,2)
                                if c == 1:
                                    e = random.randint(1, 2)
                                else:
                                    e = random.randint(5, 6)
                            elif roll[0] == 4 or roll[0] == 14 or roll[0] == 24 or roll[0] == 34 or roll[0] == 44 or roll[0] == 54:
                                c = random.randint(1,2)
                                if c == 1:
                                    e = 1
                                else:
                                    e = 6
                            else:
                                e = 15
                                stone_pupils += 15
                            try:
                                if roll[0] != 15:
                                    dies.append(e)
                            except IndexError:
                                pass
                            roll.pop(0)
                        print("you have rolled these:", dies)
                        print("which is a...")
                        hand_of_round += 1
                        hand_type = poker_hand_inator(dies)
                        if hand_type == 1:
                            print("high die!")
                            pupils += high_die[0]
                            mult += high_die[1]
                            high_die_played += 1
                            print("that is", high_die[0], "pupils and", high_die[1], "mult.")
                            if 9 in celestials:
                                print("stardust has provided mult!")
                                mult += 12
                            if 14 in celestials:
                                print("moondust has provided pıpils!")
                                pupils += 100
                            sharp.append(1)
                        elif hand_type == 2:
                            print("pair!")
                            pupils += pair[0]
                            mult += pair[1]
                            pair_played += 1
                            print("that is",pair[1], "pupils and",pair[1] , "mult.")
                            if 6 in celestials:
                                print("twin star has provided mult!")
                                mult += 8
                            if 11 in celestials:
                                print("twin moon has provided pupils!")
                                pupils += 50
                            sharp.append(2)
                        elif hand_type == 3:
                            print("two pair!")
                            pupils += two_pair[0]
                            mult += two_pair[1]
                            two_pair_played += 1
                            print("that is", two_pair[0], "pupils and",two_pair[1], "mult.")
                            if 6 in celestials:
                                print("twin star has provided mult!")
                                mult += 8
                            if 8 in celestials:
                                print("two sun two moon has provided mult!")
                                mult += 10
                            if 11 in celestials:
                                print("twin moon has provided pupils!")
                                pupils += 50
                            if 13 in celestials:
                                print("two moon two sun has provided pupils!")
                                pupils += 80
                            sharp.append(3)
                        elif hand_type == 4:
                            print("three pair!")
                            pupils += three_pair[0]
                            mult += three_pair[1]
                            three_pair_played += 1
                            print("that is", three_pair[0], "pupils and",three_pair[1], "mult.")
                            if 6 in celestials:
                                print("twin star has provided mult!")
                                mult += 8
                            if 8 in celestials:
                                print("two sun two moon has provided mult!")
                                mult += 10
                            if 11 in celestials:
                                print("twin moon has provided pupils!")
                                pupils += 50
                            if 13 in celestials:
                                print("two moon two sun has provided pupils!")
                                pupils += 80
                            sharp.append(4)
                        elif hand_type == 5:
                            print("full house!")
                            pupils += full_house[0]
                            mult += full_house[1]
                            full_house_played += 1
                            print("that is",full_house[0], "pupils and", full_house[1], "mult.")
                            if 6 in celestials:
                                print("twin star has provided mult!")
                                mult += 8
                            if 7 in celestials:
                                print("triplet star has providded mult!")
                                mult += 12
                            if 8 in celestials:
                                print("two sun two moon has provided mult!")
                                mult += 10
                            if 11 in celestials:
                                print("twin moon has provided pupils!")
                                pupils += 50
                            if 12 in celestials:
                                print("triplet moon has provided some pupils!")
                                pupils += 100
                            if 13 in celestials:
                                print("two moon two sun has provided pupils!")
                                pupils += 80
                            sharp.append(5)
                        elif hand_type == 6:
                            print("two trio!")
                            pupils += two_trio[0]
                            mult += two_trio[1]
                            two_trio_played += 1
                            print("that is",two_trio[0], "pupils and",two_trio[1], "mult.")
                            if 6 in celestials:
                                print("twin star has provided mult!")
                                mult += 8
                            if 7 in celestials:
                                print("triplet star has providded mult!")
                                mult += 12
                            if 8 in celestials:
                                print("two sun two moon has provided mult!")
                                mult += 10
                            if 11 in celestials:
                                print("twin moon has provided pupils!")
                                pupils += 50
                            if 12 in celestials:
                                print("triplet moon has provided some pupils!")
                                pupils += 100
                            if 13 in celestials:
                                print("two moon two sun has provided pupils!")
                                pupils += 80
                            sharp.append(6)
                        elif hand_type == 7:
                            print("three of a kind!")
                            pupils += three_of_a_kind[0]
                            mult += three_of_a_kind[1]
                            three_of_a_kind_played += 1
                            print("that is", three_of_a_kind[0], "pupils and",three_of_a_kind[1], "mult.")
                            if 6 in celestials:
                                print("twin star has provided mult!")
                                mult += 8
                            if 7 in celestials:
                                print("triplet star has providded mult!")
                                mult += 12
                            if 11 in celestials:
                                print("twin moon has provided pupils!")
                                pupils += 50
                            if 12 in celestials:
                                print("triplet moon has provided some pupils!")
                                pupils += 100
                            sharp.append(7)
                        elif hand_type == 8:
                            print("four of a kind!")
                            pupils += four_of_a_kind[0]
                            mult += four_of_a_kind[1]
                            four_of_a_kind_played += 1
                            print("that is",four_of_a_kind[0], "pupils and",four_of_a_kind[1], "mult.")
                            if 6 in celestials:
                                print("twin star has provided mult!")
                                mult += 8
                            if 7 in celestials:
                                print("triplet star has providded mult!")
                                mult += 12
                            if 10 in celestials:
                                print("square star has provided mult!")
                                mult += 16
                            if 11 in celestials:
                                print("twin moon has provided pupils!")
                                pupils += 50
                            if 12 in celestials:
                                print("triplet moon has provided pupils!")
                                pupils += 100
                            if 13 in celestials:
                                print("two moon two sun has provided pupils!")
                                pupils += 80
                            if 15 in celestials:
                                print("square moon has provided pupils!")
                                pupils += 200
                            sharp.append(8)
                        elif hand_type == 9:
                            print("five of a kind!")
                            pupils += five_of_a_kind[0]
                            mult += five_of_a_kind[1]
                            five_of_a_kind_played += 1
                            print("that is",five_of_a_kind[0], "pupils and", five_of_a_kind[1], "mult.")
                            if 6 in celestials:
                                print("twin star has provided mult!")
                                mult += 8
                            if 7 in celestials:
                                print("triplet star has providded mult!")
                                mult += 12
                            if 11 in celestials:
                                print("twin moon has provided pupils!")
                                pupils += 50
                            if 12 in celestials:
                                print("triplet moon has provided some pupils!")
                                pupils += 100
                            if 13 in celestials:
                                print("two moon two sun has provided pupils!")
                                pupils += 80
                            if 15 in celestials:
                                print("square moon has provided pupils!")
                                pupils += 200
                            sharp.append(9)
                        elif hand_type == 10:
                            print("six of a kind!")
                            pupils += six_of_a_kind[0]
                            mult += six_of_a_kind[1]
                            six_of_a_kind_played += 1
                            print("that is",six_of_a_kind[0], "pupils and", six_of_a_kind[1], "mult.")
                            if 6 in celestials:
                                print("twin star has provided mult!")
                                mult += 8
                            if 7 in celestials:
                                print("triplet star has providded mult!")
                                mult += 12
                            if 11 in celestials:
                                print("twin moon has provided pupils!")
                                pupils += 50
                            if 12 in celestials:
                                print("triplet moon has provided some pupils!")
                                pupils += 100
                            if 13 in celestials:
                                print("two moon two sun has provided pupils!")
                                pupils += 80
                            if 15 in celestials:
                                print("square moon has provided pupils!")
                                pupils += 200
                            sharp.append(10)
                        else:
                            print("overflow house!")
                            pupils += overflow_house[0]
                            mult += overflow_house[1]
                            overflow_house_played += 1
                            print("that is",overflow_house[0], "pupils and", overflow_house[1], "mult.")
                            if 6 in celestials:
                                print("twin star has provided mult!")
                                mult += 8
                            if 7 in celestials:
                                print("triplet star has providded mult!")
                                mult += 12
                            if 8 in celestials:
                                print("two sun two moon has provided mult!")
                                mult += 10
                            if 10 in celestials:
                                print("square star has provided mult!")
                                mult += 16
                            if 11 in celestials:
                                print("twin moon has provided pupils!")
                                pupils += 50
                            if 12 in celestials:
                                print("triplet moon has provided pupils!")
                                pupils += 100
                            if 13 in celestials:
                                print("two moon two sun has provided pupils!")
                                pupils += 80
                            if 15 in celestials:
                                print("square moon has provided pupils!")
                                pupils += 200
                            sharp.append(11)
#--------------------------------------------------------------------------------------------------
                        if 74 in celestials and random.randint(1, 4) == 1:
                            if hand_type == 1:
                                high_die_level += 1
                                high_die[0] += 120
                                high_die[1] += 12
                                print("high die has been upgraded.")
                            if hand_type == 2:
                                pair_level += 1
                                high_die[0] += 20
                                high_die[1] += 2
                                print("pair has been upgraded.")
                            if hand_type == 3:
                                two_pair_level += 1
                                two_pair[0] += 40
                                two_pair[1] += 2
                                print("two pair has been upgraded.")
                            if hand_type == 4:
                                three_pair_level += 1
                                three_pair[0] += 60
                                three_pair[1] += 2
                                print("three pair has been upgraded")
                            if hand_type == 5:
                                full_house_level += 1
                                full_house[0] += 90
                                full_house[1] += 4
                                print("full house has been upgraded")
                            if hand_type == 6:
                                two_trio_level += 1
                                two_trio[0] += 60
                                two_trio[1] += 3
                                print("two trio has been upgraded.")
                            if hand_type == 7:
                                three_of_a_kind_level += 1
                                three_of_a_kind[0] += 30
                                three_of_a_kind[1] += 3
                                print("three of a kind has been upgraded.")
                            if hand_type == 8:
                                four_of_a_kind_level += 1
                                four_of_a_kind[0] += 40
                                four_of_a_kind[1] += 4
                                print("four of a kind has been upgraded.")
                            if hand_type == 9:
                                five_of_a_kind_level += 1
                                five_of_a_kind[0] += 50
                                five_of_a_kind[1] += 5
                                print("five of a kind has been upgraded.")
                            if hand_type == 10:
                                six_of_a_kind_level += 1
                                six_of_a_kind[0] += 60
                                six_of_a_kind[1] += 6
                                print("six of a kind has been upgraded.")
                            else:
                                overflow_house_level += 1
                                overflow_house[0] += 50
                                overflow_house[1] += 5
                                print("overflow house has been upgraded.")
                        if 1 in celestials:
                            print("meteor has provided mult!")
                            mult += 4
                        if 18 in celestials and discards > 0:
                            for i in range(1, discards, 1):
                                print("cold star has provided pupils!")
                                pupils += 30
                        if 22 in celestials and discards > 0:
                            for i in range(1, discards, 1):
                                print("USA flag has provided mult!")
                                mult += 4
                        if discards == 0 and 19 in celestials:
                            print("gravity-less planet has provided mult!")
                            mult += 15
                        for z in dies:
                            if z is not None:
                                pupils += z
                                if 28 in celestials:
                                    if z == 2 or z == 4 or z == 6:
                                        print("even starts has provided mult!")
                                        mult += 4
                                if 29 in celestials:
                                    if z == 1 or z == 3 or z == 5:
                                        print("odd stars out of the galaxy has provided some pupils!")
                                        pupils += 31
                                if 30 in celestials:
                                    if z == 1 or z == 2 or z == 4:
                                        mult += 4
                                        print("collatzes law has provided mult!")
                                if i == 1 and 31 in celestials:
                                    print("oops! all 1's provided mult!")
                                    mult += 3
                                if 41 in celestials and i == 6:
                                    print("addiction has provided cash!")
                                    cash += 1
                                if 65 in celestials and i == 6:
                                    print("oops! all sixes has provided some pupils!")
                                    pupils += 60
                            pupils += stone_pupils
#---------------------------------die type---------------------------------------------------------------------
                        for i in roll:
                            if i == 11 or i == 12 or i == 13 or i == 14:
                                d = random.randint(1, 5)
                                if d == 1:
                                    mult += 5
                                    print("lucky die has gave some mult!")
                                    luck += 0.25
                                d = random.randint(1, 20)
                                if d == 1:
                                    cash += 10
                                    print("lucky die has game some sweet sweet cash!")
                                    luck += 0.25
                            if i == 21 or i == 22 or i == 23 or i == 24:
                                mult += 1
                                print("mult die has provided mult!")
                            if i == 31 or i == 32 or i == 33 or i == 34:
                                mult *= 1.1
                                print("pin die has multed your mult!")
                            if i == 41 or i == 42 or i == 43 or i == 44:
                                mult *= 1.2
                                d = random.randint(1, 4)
                                if d == 1:
                                    contents_of_box.remove(i)
                                    glass += 0.75
                                    if i == 41:
                                        print("badge die has perished.")
                                    elif i == 42:
                                        print("badge sphere has perished.")
                                    elif i == 43:
                                        print("badge d4 has perished.")
                                    else:
                                        print("badge coin has perished.")
                            if 33 in celestials and i == 3:
                                print("galaxy o bill has provided some mult!")
                                mult += 3
                            if i == 51 or i == 52 or i == 53 or i == 54:
                                pupils += 10
                                print("bonus die has provided pupils!")
                            if i == 2 or i == 12 or i == 22 or i == 32 or i == 42 or i == 52:
                                if 5 in celestials:
                                    mult += 1
                                    print("gluttony ring has provided mult!")
                            if i == 3 or i == 13 or i == 23 or i == 33 or i == 43 or i == 53:
                                if 2 in celestials:
                                    mult += 3
                                    print("greed ring has provided mult!")
                            if i == 4 or i == 14 or i == 24 or i == 34 or i == 44 or i == 54:
                                if 3 in celestials:
                                    mult += 2
                                    print("lust ring has provided mult!")
                            if i == 1 or i == 11 or i == 21 or i == 31 or i == 41 or i == 51:
                                if 4 in celestials:
                                    mult += 4
                                    print("wrath ring has provided mult!")
                            if 69 in celestials:
                                if i == 1:
                                    current_box.remove(i)
                                    current_box.append(31)
                                    print("steel moon has done its thing.")
                                elif i == 2:
                                    current_box.remove(i)
                                    current_box.append(32)
                                    print("steel moon has done its thing.")
                                elif i == 3:
                                    current_box.remove(i)
                                    current_box.append(33)
                                    print("steel moon has done its thing.")
                                elif i == 4:
                                    current_box.remove(i)
                                    current_box.append(34)
                                    print("steel moon has done its thing.")
                            if 110 in celestials:
                                if i == 3 or i == 13 or i == 23 or i == 33 or i == 43 or i == 53:
                                    print("diamond meteor has provided cash!")
                                    cash += 1
                            if 111 in celestials and random.randint(1, 2) == 1:
                                if i == 4 or i == 14 or i == 24 or i == 34 or i == 44 or i == 54:
                                    print("scenario: iron lung has multiplied mult!")
                                    mult *= 1.5
                            if 112 in celestials:
                                if i == 1 or i == 11 or i == 21 or i == 31 or i == 41 or i == 51:
                                    print("space directions have provided pupils!")
                                    pupils += 50
                            if 113 in celestials:
                                if i == 2 or i == 12 or i == 22 or i == 32 or i == 42 or i == 52:
                                    print("dimension zero has provided mult!")
                                    mult += 7
                        if 21 in celestials:
                            v = random.randint(1, 23)
                            print("glitch in space and time has provided", v, "mult!")
                            mult += v
                        if 24 in celestials:
                            w =[]
                            for d in celestials:
                                if i != 0:
                                        w.append(i)
                            print("saturn has provided", len(w) * 23, "pupils!")
                            pupils += len(w) * 23
                            if 25 in celestials:
                                w =[]
                                for d in celestials:
                                    if i != 0:
                                        w.append(i)
                                print("jupiter has provided", len(w) * 3, "mult!")
                                mult += len(w) * 3
                            if 27 in celestials:
                                mult += 15
                                print("pluto has granted mult!")
                                if random.randint(1, 1000) == 1:
                                    celestials.remove(27)
                                    print("pluto is no longer a planet.")
                            if 32 in celestials:
                                if hand_type == 1:
                                    print("supernova has provided", high_die_played, "mult!")
                                    mult += high_die_played
                                elif hand_type == 2:
                                    print("supernova has provided", pair_played, "mult!")
                                    mult += pair_played
                                elif hand_type == 3:
                                    print("supernova has provided", two_pair_played, "mult!")
                                    mult += two_pair_played
                                elif hand_type == 4:
                                    print("supernova has provided", three_pair_played, "mult!")
                                    mult += three_pair_played
                                elif hand_type == 5:
                                    print("supernova has provided", full_house_played, "mult!")
                                    mult += full_house_played
                                elif hand_type == 6:
                                    print("supernova has provided", two_trio_played, "mult!")
                                    mult += two_trio_played
                                elif hand_type == 7:
                                    print("supernova has provided", three_of_a_kind_played, "mult!")
                                    mult += three_of_a_kind_played
                                elif hand_type == 8:
                                    print("supernova has provided", four_of_a_kind_played, "mult!")
                                    mult += four_of_a_kind_played
                                elif hand_type == 9:
                                    print("supernova has provided", five_of_a_kind_played, "mult!")
                                    mult += five_of_a_kind_played
                                elif hand_type == 10:
                                    print("supernova has provided", six_of_a_kind_played, "mult!")
                                    mult += six_of_a_kind_played
                                else:
                                    print("supernova has provided", overflow_house_played, "mult!")
                                    mult += overflow_house_played
                        if 34 in celestials:
                            print("space ship has provided", high_die_played * 15, "pupils!")
                            pupils += high_die_played * 15
                        if 36 in celestials:
                            print("none can hear you scream has provided", ice_cream, "pupils!")
                            pupils += ice_cream
                            ice_cream -= 5
                            if ice_cream == 0:
                                celestials.remove(36)
                                print("none can hear you scream has melted away.")
                        if 53 in celestials:
                            print("in space has provided", popcorn, "mult!")
                            mult += popcorn
                            popcorn -= 4
                            if popcorn == 0:
                                celestials.remove(53)
                                print("in space has rotten away.")
                        if 38 in celestials:
                            print("neptune has provided", len(contents_of_box) * 2, "pupils.")
                            pupils += len(contents_of_box) * 2
                        if 40 in celestials:
                            print("acid rain has provided", decision_balance, "mult!")
                            mult += decision_balance
                        if 42 in celestials and random.randint(1, 11) == 1:
                            print("space route has provided cash")
                            cash += 4
                        if 50 in celestials and souls_played > 0:
                            print("all the stars has provided", souls_played, "mult!")
                            mult += souls_played
                        if 16 in celestials:
                            k = random.randint(8, 180)
                            print("meteor field has provided", k, "pupils!")
                            pupils += k
                        if 17 in celestials:
                            print("wishing star has provided pupils!")
                            pupils += 30
                        if 20 in celestials:
                            print("sunlight has provided cash!")
                            cash += 2
                            if random.randint(1, 1000) == 1:
                                celestials.remove(20)
                                print("sunlight has faded away.")
                        if 23 in celestials:
                            print("NASA has provided pupils!")
                            pupils += 220
                            if random.randint(1, 1000) == 1:
                                celestials.remove(23)
                                print("NASA has went bankrupt.")
                        if 37 in celestials and high_die_level + pair_level + three_pair_level + full_house_level + three_of_a_kind_level + two_trio_level + four_of_a_kind_level + five_of_a_kind_level + six_of_a_kind_level + overflow_house_level != 11:
                            print("hybrid planet has provided", (high_die_level + pair_level + three_pair_level + full_house_level + three_of_a_kind_level + two_trio_level + four_of_a_kind_level + five_of_a_kind_level + six_of_a_kind_level + overflow_house_level) * 8, "pupils!" )
                            pupils += (high_die_level + pair_level + three_pair_level + full_house_level + three_of_a_kind_level + two_trio_level + four_of_a_kind_level + five_of_a_kind_level + six_of_a_kind_level + overflow_house_level) * 8
                        if 39 in celestials and random.randint(1, 2) == 1:
                            print("brainstorm has provided mult!")
                            mult += 15
                        if 64 in celestials and gravity_played != 0:
                            print("reverse mitosis has provided", gravity_played, "mult!")
                            mult += gravity_played
                        if 66 in celestials and eyes != []:
                            print("space reptile has provided", len(eyes) * 75, "pupils")
                            pupils += len(eyes) * 75
                        if 70 in celestials and eyes != []:
                            print("space vending machine has provided", len(eyes) * 10, "mult!")
                            mult += len(eyes) * 10
                        if 91 in celestials and len(contents_of_box) < 53:
                            print("rusty planet has provided", (52 - len(contents_of_box)) * 4, "mult!")
                            mult += (52 - len(contents_of_box)) * 4
                        if 93 in celestials and contents_of_box.count(15) != 0:
                            print("stone moon has provided", contents_of_box.count(15) * 25, "pupils!")
                            pupils += contents_of_box.count(15) * 25
                        if 95 in celestials and cash > 0:
                            print("bull has provided", cash * 2, "pupils!")
                            pupils += cash * 2
                        if 99 in celestials and (two_pair_played + full_house_played + two_trio_played + three_pair_played + overflow_house_played) * 2 != 0:
                            print("meteor-U has provided", (two_pair_played + full_house_played + two_trio_played + three_pair_played + overflow_house_played) * 2, "mult!")
                            mult += (two_pair_played + full_house_played + two_trio_played + three_pair_played + overflow_house_played) * 2
                        if 125 in celestials:
                            for l in range(0, cash, 5):
                                mult += 2
                            print("space boot has provided about", cash / 5, "mult")
                        if 146 in celestials and ceres != 0:
                            print("ceres has provided", ceres, "pupils!")
                            pupils += ceres
#------------------------------------------------------------X---------------------------------------------------
                        if 43 in celestials:
                            print("radioactive moon has multiplied mult!")
                            mult *= 3
                            if random.randint(1, 5) == 1:
                                celestials.remove(43)
                                print("radioactive moon has been destroyed.")
                        if 62 in celestials and hand_of_round == 3:
                            print("the pipe strip has multiplied mult!")
                            mult *= 3
                        if 68 in celestials and royal == 6:
                            print("royal planet has multiplied mult!")
                            mult *= 4
                        if 71 in celestials:
                            pins = 10
                            for i in current_box:
                                if i == 31 or i == 32 or i == 33 or i == 34:
                                    pins += 1
                            if pins != 10:
                                print("steel planet has multiplied mult by x", pins / 10)
                                mult *= pins / 10
                        if 72 in celestials:
                            print("chemical x has multiplied mult!")
                            mult *= 1.5
                        if 76 in celestials:
                            if 3 not in dies and 4 not in dies and 13 not in dies and 14 not in dies and 23 not in dies and 24 not in dies and 33 not in dies and 34 not in dies and 43 not in dies and 44 not in dies and 53 not in dies and 54 not in dies:
                                print("dark matter has multiplied mult!")
                                mult *= 3
                        if 78 in celestials and high_die_level + pair_level + three_pair_level + full_house_level + three_of_a_kind_level + two_trio_level + four_of_a_kind_level + five_of_a_kind_level + six_of_a_kind_level + overflow_house_level == 11:
                            print("constelation has multiplied mult by: x", (high_die_level + pair_level + three_pair_level + full_house_level + three_of_a_kind_level + two_trio_level + four_of_a_kind_level + five_of_a_kind_level + six_of_a_kind_level + overflow_house_level) / 10 + 1)
                            mult *= (high_die_level + pair_level + three_pair_level + full_house_level + three_of_a_kind_level + two_trio_level + four_of_a_kind_level + five_of_a_kind_level + six_of_a_kind_level + overflow_house_level) / 10 + 1
                        if 80 in celestials and hand_type in sharp:
                            print("sharp sun has multiplied mult!")
                            mult *= 3
                        if 83 in celestials:
                            if i == 11 or i == 21 or i == 31 or i == 41 or i == 51:
                                blood += 0.1
                                contents_of_box.remove(i)
                                contents_of_box.append(1)
                            if i == 12 or i == 22 or i == 32 or i == 42 or i == 52:
                                blood += 0.1
                                contents_of_box.remove(i)
                                contents_of_box.append(2)
                            if i == 13 or i == 23 or i == 33 or i == 43 or i == 53:
                                blood += 0.1
                                contents_of_box.remove(i)
                                contents_of_box.append(3)
                            if i == 14 or i == 24 or i == 34 or i == 44 or i == 54:
                                blood += 0.1
                                contents_of_box.remove(i)
                                contents_of_box.append(4)
                            print("blood moon has multiplied mult by: x", blood)
                            mult *= blood
                        if 85 in celestials and die_added != 0:
                            print("illusion of light has multiplied mult by: x", (die_added + 4) * 25 / 100)
                            mult *= (die_addded + 4) * 25 / 100
                        if 94 in celestials and luck != 1:
                            print("lucky star has multiplied mult by: x", luck)
                            mult *= luck
                        if 100 in celestials:
                            print("space food has multiplied mult by: x", space_food / 100)
                            mult *= space_food / 100
                        if 104 in celestials and rolls == 0:
                            print("space gun has multiplied mult!")
                            mult *= 3
                        if 114 in celestials and glass != 1:
                            print("glass planet has multiplied mult by: x", glass)
                            mult *= glass
                        if 120 in celestials:
                            if 2 in roll:
                                if not all(item in orbs for item in roll):
                                    print("rift has multiplied mult!")
                                    mult *= 2
                            elif 12 in roll:
                                if not all(item in orbs for item in roll):
                                    print("rift has multiplied mult!")
                                    mult *= 2
                            elif 22 in roll:
                                if not all(item in orbs for item in roll):
                                    print("rift has multiplied mult!")
                                    mult *= 2
                            elif 32 in roll:
                                if not all(item in orbs for item in roll):
                                    print("rift has multiplied mult!")
                                    mult *= 2
                            elif 42 in roll:
                                if not all(item in orbs for item in roll):
                                    print("rift has multiplied mult!")
                                    mult *= 2
                            elif 52 in roll:
                                if not all(item in orbs for item in roll):
                                    print("rift has multiplied mult!")
                                    mult *= 2
                        if 126 in celestials and cash > 40:
                            print("paraoh planet has multiplied mult")
                            mult *= 3
                        if 127 in celestials and len(contents_of_box) == 52:
                            print("the golden sun has multiplied mult!")
                            mult *= 4
                        if 133 in celestials and hand_type != 1:
                            print("duo has multiplied mult!")
                            mult *= 2
                        if 134 in celestials and hand_type > 4:
                            print("trio has multiplied mult!")
                            mult *= 3
                        if 135 in celestials and hand_type > 7:
                            print("quadro has multiplied mult!")
                            mult *= 4
                        if 136 in celestials and hand_type > 8 and hand_type != 11:
                            print("cinq has multiplied mult!")
                            mult *= 5
                        if 137 in celestials and hand_type == 1:
                            print("law of space has multiplied mult!")
                            mult *= 3
                        if 141 in celestials:
                            var_1 = contents_of_box.count(1)
                            var_2 = contents_of_box.count(2)
                            var_3 = contents_of_box.count(3)
                            var_4 = contents_of_box.count(4)
                            if len(contents_of_box) - (var_1 + var_2 + var_3 + var_4) > 15:
                                print("license of something has multiplied mult!")
                                mult *= 3
                        if 147 in celestials and len(eyes) != 0:
                            print("remina has multiplied mult by: x", len(eyes) + 1)
                            mult *= len(eyes) + 1
                        if 148 in celestials and planet_x != 1:
                            print("planet x has multiplied mult by: x", planet_x)
                            mult *= planet_x
#---------------------------------------score--------------------------------------------------------------------
                        score += pupils * mult
                        print("pupils in total are:", score)
                        if score >= b:
                            break
                        else:
                            continue
                if 26 in celestials and discards == discard_max:
                    print("delay in gravity has granted cash!")
                    cash += 2 * discards
                if 87 in celestials:
                    cash += 1 + ante * 2
                    print("rocket has provided,", 1 + ante * 2, "cash!")
                if 122 in celestials:
                    if high_die_level != 1:
                        cash += 1
                    if pair_level != 1:
                        cash += 1
                    if two_pair_level != 1:
                        cash += 1
                    if three_pair_level != 1:
                        cash += 1
                    if three_of_a_kind_level != 1:
                        cash += 1
                    if two_trio_level != 1:
                        cash += 1
                    if four_of_a_kind_level != 1:
                        cash += 1
                    if five_of_a_kind_level != 1:
                        cash += 1
                    if six_of_a_kind_level != 1:
                        cash += 1
                    if full_house_level != 1:
                        cash += 1
                    if overflow_house != 1:
                        cash += 1
                    print("satalite activated succesfully.")
                print("you won!")
                if box != 3:
                    if a == 1:
                        cash += 3
                        if cash >= 25:
                            cash += 5
                        elif cash >= 20:
                            cash += 4
                        elif cash >= 15:
                            cash += 3
                        elif cash >= 10:
                            cash += 2
                        elif cash >= 5:
                            cash += 1
                        if 8 in eyes:
                            if cash >= 50:
                                cash += 5
                            elif cash >= 45:
                                cash += 4
                            elif cash >= 40:
                                cash += 3
                            elif cash >= 35:
                                cash += 2
                            elif cash >= 30:
                                cash += 1
                    else:
                        cash += 4
                        if cash >= 25:
                            cash += 5
                        elif cash >= 20:
                            cash += 4
                        elif cash >= 15:
                            cash += 3
                        elif cash >= 10:
                            cash += 2
                        elif cash >= 5:
                            cash += 1
                        if 8 in eyes:
                            if cash >= 50:
                                cash += 5
                            elif cash >= 45:
                                cash += 4
                            elif cash >= 40:
                                cash += 3
                            elif cash >= 35:
                                cash += 2
                            elif cash >= 30:
                                cash += 1
                if 92 in celestials:
                    if cash >= 25:
                        cash += 5
                    elif cash >= 20:
                        cash += 4
                    elif cash >= 15:
                        cash += 3
                    elif cash >= 10:
                        cash += 2
                    elif cash >= 5:
                        cash += 1
                if rolls != 0:
                    cash += rolls
                    print("you have gained cash for remaining hands.")
                if box == 3:
                    cash += rolls + discards
                    print("green box has provided", rolls + discards, "cash.")
                if 52 in celestials:
                    print("golden planet has provided cash!")
                    cash += 4
                print("you have", cash, "cash.")
                shop_eye()
                shop_packs()

        ante += 1
