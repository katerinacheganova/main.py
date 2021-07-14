import random
import sys

global hp
global attack
global monster_counter
global hp_mon
global attack_mon


def choose_answer(answer: str):
    """Возвращает флаг в зависимости от введенных данных."""
    while True:
        if answer.isdigit() and int(answer) == 1:
            return True
        elif answer.isdigit() and int(answer) == 2:
            return False
        else:
            print("Вы ввели некорректные данные. " "Введите число 1 или 2")
            return choose_answer(input())


def get_random_event():
    """Возвращает одно из трёх значений для случайного выбора."""
    event = random.randrange(0, 3)
    if event == 0:
        print("Итак перед Вами яблоко")
        return 0
    elif event == 1:
        print("Итак перед Вами меч")
        return 1


def create_monster():
    """Используется для создания параметров монстра: здоровье и атака."""
    global hp_mon
    global attack_mon
    hp_mon = random.randrange(1, 41)
    attack_mon = random.randrange(1, 31)
    return hp_mon, attack_mon


def fight():
    """Возвращает количество единиц жизни у героя и монстра после одного удара."""
    global hp
    global attack
    global hp_mon
    global attack_mon
    hp -= attack_mon
    hp_mon -= attack
    return hp, hp_mon


def game():
    """Содержит основное тело игры."""
    global hp
    global attack
    global monster_counter
    hp = random.randrange(10, 81, 10)
    attack = random.randrange(10, 51, 10)
    monster_counter = 0

    print('Добро пожаловать в игру "Мир Героев"! \n')
    print(
        "Королевство в опасности! Из подвала королевы \n"
        "выползли забытые любовники - теперь это жуткие монстры! \n"
        "Наконец появился тот, кто сможет их одолеть!\n"
    )
    print(
        f"Герой обладает {hp} единицами здоровья и" f" {attack} единицами силы удара.\n"
    )

    while monster_counter < 10 and hp > 0:
        rand = get_random_event()
        if rand == 0:  # яблоко
            apple = random.randint(5, 30)
            hp += apple
            print(
                f"Герой съел ЯБЛОКО , его здоровье"
                f" увеличилось на {apple} и равно {hp}\n"
            )
        elif rand == 1:  # меч
            sword = random.randint(5, 50)
            print(f"Найденный МЕЧ обладает силой удара {sword}")
            print(
                f"Для того чтобы заменить свой меч с силой {attack} на найденный нажмите 1, \n"
                f"чтобы отказаться нажмите 2\n"
            )
            ans = choose_answer(input())
            if ans == 1:
                attack = sword
                print(f"Теперь сила вашего удара равна {attack}\n")
            else:
                print("Вы выбросили найденный меч. Продолжайте путь.\n")

        hp_mon, attack_mon = create_monster()
        print(
            f"Перед Вами МОНСТР, он обладает {hp_mon} единицами здоровья и силой удара {attack_mon}. \n"
            "Если Вы готовы вступить с ним в БОЙ нажмите 1. Спрятаться в кустах - нажмите 2"
        )
        ans = choose_answer(input())
        if ans == 1:
            hit_cnt = 0
            while hp > 0 and hp_mon > 0:
                hp, hp_mon = fight()
                hit_cnt += 1
                print(
                    f"Герой и монстр нанесли по {hit_cnt} ударов, \n "
                    f"жизнь героя равна {hp} и жизнь монстра равна {hp_mon}."
                )
            if hp > 0:
                monster_counter += 1
                print(
                    f"Герой победил {monster_counter} монстров! \n "
                    f"Осталось победить всего {10 - monster_counter} монстров. \n"
                )
            else:
                print("Увы, герой пал смертью храбрых!")
        else:
            print("Вы отказались от сражения. Посмотрим, что ждет Вас впереди.\n")

    if monster_counter == 10:
        print("ПОБЕДА ! \n Королевство может спать спокойно!")
    if hp <= 0:
        print(" ПОРАЖЕНИЕ ! \n GAME OVER!")
    sys.exit()


game()
