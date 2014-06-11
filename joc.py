from personatge import Personatge, Atac


def all_alive(players):
    for player in players:
        if not player.is_alive():
            return False
    return True


def show_lives(players):
    for player in players:
        print(player.nom + ':', player.vida)

atacs_p = [Atac('Punxa', 10, 3), Atac('Talla', 5, 10), Atac('Empeny', 3, 20)]
atacs_e = [Atac('Punxa', 10, 3), Atac('Talla', 5, 10), Atac('Empeny', 3, 20)]

player = Personatge(100, atacs_p, "Jugador")
enemy = Personatge(100, atacs_e, "Enemic")
players = [player, enemy]


def main_loop():
    while all_alive(players):
        show_lives(players)
        atac = player.choose_attack()
        player.attack(atac, enemy)
        if not all_alive(players):
            break
        atac = enemy.rand_attack()
        enemy.attack(atac, player)
    for p in players:
        if not p.is_alive():
            print(p.nom, "ha mort!")


if __name__ == '__main__':
    main_loop()
