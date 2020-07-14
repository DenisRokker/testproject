import time
import json

JSON_TEXT_FILE_NAME = 'text.json'


def json_load():
    return json.load(open(JSON_TEXT_FILE_NAME, encoding='utf8'))


TEXT = json_load()


def delay(seconds):
    ...
    time.sleep(seconds)


class Character:
    ...


def create_character(name, health, power, intellect, dexterity):
    self = Character
    self.name = name
    self.health = health
    self.power = power
    self.intellect = intellect
    self.dexterity = dexterity

    return self


name = input(TEXT["name"])
print(TEXT["point"])

limit = 5
print(f"У вас осталось {limit} очков")

while True:

    power = int(input(TEXT["power"]))
    intellect = int(input(TEXT["intellect"]))
    dexterity = int(input(TEXT["dexterity"]))
    health = 10

    if limit >= power + dexterity + intellect > -1:
        break

    else:
        print(TEXT["repeat"])

equipment = []

print(f"Ваш персонаж: \"{name}\" "
      f"здоровье: {health} "
      f"его сила: {power} "
      f"интелект: {intellect}, "
      f"ловкость: {dexterity} ")

delay(3)

print(TEXT["chapter_1"])

delay(2)

print(TEXT["replica_1"])

delay(2)

input(TEXT["replica_2"].format(name))
print(TEXT["replica_3"])

while True:

    stone = input(TEXT["stone"])

    if stone == "да" and power >= 1:

        print(TEXT["replica_4"])
        delay(1)

        equipment.append("Меч")

        print(f"Ваш персонаж: \"{name}\" "
              f"здоровье: {health} "
              f"его сила: {power} "
              f"интелект: {intellect}, "
              f"ловкость: {dexterity} ")

        print("Ваш инвентарь: " + equipment[0])
        break

    elif stone == "да" and power == 0:
        print(TEXT["replica_5"])
        break
    elif stone == "нет":
        ...
        break
    else:
        print(TEXT["repeat_2"])

input(TEXT["continue"])
print(TEXT["replica_6"])

delay(2)
print(TEXT["replica_7"])

delay(2)
print(TEXT["replica_8"])

print(f"Ваш персонаж: \"{name}\" "
      f"здоровье: {health} "
      f"его сила: {power} "
      f"интелект: {intellect}, "
      f"ловкость: {dexterity} ")

if "Меч" in equipment:

    while True:

        fight = input(TEXT["punch"])

        if fight == "ударить" and power == 5:
            print(TEXT["replica_9"])
            delay(2)
            print(TEXT["replica_10"])
            delay(2)
            print(TEXT["replica_11"])
            print(TEXT["replica_12"])

            equipment.append('Ключ')

            print("Вы получили новый уровень!")

            limit = 6
            print(f"У вас осталось 1 очко навыков.")

            while True:

                power = power + int(input(TEXT["power"]))
                intellect = intellect + int(input(TEXT["intellect"]))
                dexterity = dexterity + int(input(TEXT["dexterity"]))

                if limit >= power + dexterity + intellect > 0:
                    break

                else:
                    print(TEXT["repeat"])

            print(f"Ваш персонаж: \"{name}\" "
                  f"здоровье: {health} "
                  f"его сила: {power} "
                  f"интелект: {intellect}, "
                  f"ловкость: {dexterity} ")

            print("Ваш инвентарь: " + equipment[0] + ", " + equipment[1])

            input(TEXT["continue"])
            print(TEXT["replica_13"])

            head_of_troll = 1

            break

        elif fight == "ударить" and power < 5:
            print(TEXT["replica_14"])
            delay(2)
            print(TEXT["replica_15"])
            delay(1)
            print(TEXT["die"])

            life = 0

            break

        elif fight == "убежать":
            print(TEXT["replica_16"])
            delay(2)
            print(TEXT["replica_17"])
            delay(1)
            print(TEXT["replica_18"])

            break

        else:
            print(TEXT["repeat_3"])

elif "Меч" not in equipment:
    print(TEXT["replica_16"])
    delay(2)
    print(TEXT["replica_17"])
    delay(1)
    print(TEXT["replica_18"])

delay(3)
print("Конец первой главы.")
input(TEXT["continue"])
print("Глава II.")
input("Продолжение следует...")