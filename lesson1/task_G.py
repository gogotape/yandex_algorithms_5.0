def calc_rounds_with_skip(soldiers: int, barracks_hp: int, enemies_producing: int, skip=0):

    barracks_hp -= soldiers
    if barracks_hp > 0:
        enemies = enemies_producing
    else:
        enemies = 0

    rnd = 1

    while (barracks_hp > 0 or enemies) > 0 and soldiers > 0:
        potential_attack = soldiers - barracks_hp
        res_enemy = enemies_producing - potential_attack
        res_sold = soldiers - res_enemy

        if soldiers >= barracks_hp and res_sold * 1.618 >= res_enemy and skip == 0:
            sld_to_barack = barracks_hp
            sld_to_attack = soldiers - sld_to_barack

        elif barracks_hp > 0 and soldiers > enemies_producing:
            sld_to_attack = enemies_producing
            sld_to_barack = soldiers - sld_to_attack
        elif barracks_hp > 0:
            sld_to_barack = min(barracks_hp, soldiers)
            sld_to_attack = soldiers - sld_to_barack
        else:
            sld_to_barack = 0
            sld_to_attack = soldiers

        if soldiers >= barracks_hp and res_sold * 1.618 >= res_enemy and skip != 0:
            skip -= 1

        barracks_hp -= sld_to_barack
        enemies -= sld_to_attack
        soldiers -= enemies

        if barracks_hp > 0:
            enemies += enemies_producing

        rnd += 1

    if barracks_hp <= 0 and enemies <= 0:
        return rnd

    return -1


def calc_rounds(soldiers, barracks_hp, enemies_producing):
    results = []
    for skip in range(0, 3):
        result = calc_rounds_with_skip(
            soldiers=soldiers,
            barracks_hp=barracks_hp,
            enemies_producing=enemies_producing,
            skip=skip,
        )
        results.append(result)

    return min(results)


if __name__ == "__main__":
    soldiers = int(input())
    barracks_hp = int(input())
    enemies_producing = int(input())
    res = calc_rounds(soldiers, barracks_hp, enemies_producing)
    print(res)