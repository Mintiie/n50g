import random


def roll():
    min_value = 1
    max_value = 6
    rolling = random.randint(min_value, max_value)

    return rolling


while True:
    players = input("Wie viele Spieler spielen mit? (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Es können nur zwei bis vier Spieler mitspielen.")
    else:
        print("Versuch es nochmal.")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nSpieler", player_idx + 1, "ist jetzt dran!\n")
        print("Dein Score beträgt:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("\nMöchtest du würfeln (y/n)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("\nDu hast eine 1 gewürfelt! Der nächste Spieler ist dran!")
                current_score = 0
                break
            else:
                current_score += value
                print("\nDu hast eine", value, "gewürfelt!")

            print("Dein Score beträgt im Moment:", current_score)

        player_scores[player_idx] += current_score
        print("\nSpieler", player_idx + 1, "hat einen Score von:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Spieler", winning_idx + 1, "hat gewonnen mit einem Score von:", max_score)
