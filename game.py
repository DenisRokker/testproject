import time
import json
import psycopg2
import sys

from character import Character

JSON_TEXT_FILE_NAME = 'text.json'


def json_load():
    return json.load(open(JSON_TEXT_FILE_NAME, encoding='utf8'))


TEXT = json_load()


def delay(seconds):
    ...
    time.sleep(seconds)


def create_character():
    name = input(TEXT["name"])
    print(TEXT["point"])

    limit_point = 5
    print(f"У вас осталось {limit_point} очков")

    while True:

        power = int(input(TEXT["power"]))
        intellect = int(input(TEXT["intellect"]))
        dexterity = int(input(TEXT["dexterity"]))
        health = 10

        if limit_point >= power + dexterity + intellect > -1:
            break

        else:
            print(TEXT["repeat"])

    player = Character(name,
                       power=power,
                       intellect=intellect,
                       dexterity=dexterity,
                       health=health)

    print(f"Ваш персонаж: \"{player.name}\" "
          f"его сила: {player.power} "
          f"интелект: {player.intellect}, "
          f"ловкость: {player.dexterity} "
          f"здоровье: {player.health} ")

    return player


class Item:

    def __init__(self, name, power, intellect, dexterity, health):
        self.name = name
        self.health = health
        self.power = power
        self.intellect = intellect
        self.dexterity = dexterity

    def save(self):
        """
            Saving character to database
        """

        conn = psycopg2.connect("dbname=postgres user=postgres password=postgres")
        cursor = conn.cursor()

        # Insert
        cursor.execute(
            "INSERT INTO inventory (name, health, power, intellect, dexterity) VALUES (%s, %s, %s, %s, %s) RETURNING id",
            (self.name, self.health, self.power, self.intellect, self.dexterity),
        )

        conn.commit()
        cursor.close()
        conn.close()


def part_one(player):
    global sword

    conn = psycopg2.connect("dbname=postgres user=postgres password=postgres")
    cursor = conn.cursor()

    delay(3)
    print(TEXT["chapter_1"])
    delay(2)
    print(TEXT["replica_1"])
    delay(2)
    input(TEXT["replica_2"].format(player.name))
    print(TEXT["indent"])
    print(TEXT["replica_3"])

    while True:

        stone = input(TEXT["stone"])

        if stone == "да" and player.power >= 1:

            print(TEXT["replica_4"])
            delay(1)

            name = "Меч"
            sword_power = 1
            sword_intellect = 0
            sword_dexterity = 0
            sword_health = 0

            sword = Item(name,
                         power=sword_power,
                         intellect=sword_intellect,
                         dexterity=sword_dexterity,
                         health=sword_health)

            player.add_inventory(sword)
            player.has_sword = True

            print(f"Ваш персонаж: \"{player.name}\" "
                  f"его сила: {player.power} "
                  f"интелект: {player.intellect}, "
                  f"ловкость: {player.dexterity} "
                  f"здоровье: {player.health} ")

            print("Ваш инвентарь: " + str(sword.name))
            break

        elif stone == "да" and player.power == 0:
            print(TEXT["replica_5"])
            break
        elif stone == "нет":
            ...
            break
        else:
            print(TEXT["repeat_2"])

    input(TEXT["continue"])
    print(TEXT["indent"])
    print(TEXT["replica_6"])

    delay(2)
    print(TEXT["replica_7"])

    delay(2)
    print(TEXT["replica_8"])

    print(f"Ваш персонаж: \"{player.name}\" "
          f"его сила: {player.power} "
          f"интелект: {player.intellect}, "
          f"ловкость: {player.dexterity} "
          f"здоровье: {player.health} ")

    while True:

        fight = input(TEXT["punch"])

        if fight == "ударить" and player.power >= 3 and player.has_sword == True:

            print(TEXT["replica_9"])
            delay(2)
            print(TEXT["replica_10"])
            delay(2)
            print(TEXT["replica_11"])
            print(TEXT["replica_12"])

            name = "Ключ"
            key_power = 0
            key_intellect = 0
            key_dexterity = 0
            key_health = 0

            key = Item(name,
                       power=key_power,
                       intellect=key_intellect,
                       dexterity=key_dexterity,
                       health=key_health)

            player.add_inventory(key)

            print("Вы получили новый уровень!")

            limit = player.power + player.intellect + player.dexterity + player.health + 1
            print(f"У вас осталось 1 очко навыков.")

            while True:

                player.power += int(input(TEXT["power"]))
                player.intellect += int(input(TEXT["intellect"]))
                player.dexterity += int(input(TEXT["dexterity"]))

                if limit >= player.power + player.dexterity + player.intellect > 0:
                    break

                else:
                    print(TEXT["repeat"])

            print(f"Ваш персонаж: \"{player.name}\" "
                  f"его сила: {player.power} "
                  f"интелект: {player.intellect}, "
                  f"ловкость: {player.dexterity} "
                  f"здоровье: {player.health} ")

            print("Ваш инвентарь: " + sword.name + ", " + key.name)

            input(TEXT["continue"])
            print(TEXT["replica_13"])

            break

        elif fight == "ударить" and player.power < 3:
            print(TEXT["replica_14"])
            delay(2)
            print(TEXT["replica_15"])
            delay(1)
            print(TEXT["die"])

            delay(6)
            sys.exit()

        elif fight == "убежать":
            print(TEXT["replica_16"])
            delay(2)
            print(TEXT["replica_17"])
            delay(1)
            print(TEXT["replica_18"])

            break

        elif fight == "ударить" and player.power >= 3 and player.has_sword == False:

            print(TEXT["replica_14"])
            delay(2)
            print(TEXT["replica_15"])
            delay(1)
            print(TEXT["die"])

            delay(6)
            sys.exit()

        else:
            print(TEXT["repeat_3"])

    delay(3)
    print("Конец первой главы.")
    input(TEXT["continue"])

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    one = create_character()

    part_one(one)
