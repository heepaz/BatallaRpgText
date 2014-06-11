import random


class Personatge (object):
    def __init__(self, vida, atacs, nom="Enemic"):
        self.vida = vida
        self.atacs = atacs
        self.nom = nom

    def is_alive(self):
        return self.vida > 0

    def show_attacks(self):
        i = 0
        for atac in self.atacs:
            i += 1
            print(str(i) + '.', atac.nom,
                  '(' + str(atac.restants)+'/'+str(atac.maxim) + ')')

    def choose_attack(self):
        self.show_attacks()
        n = input("Escull l'atac a realitzar: ")
        while not self.valid_attack(n):
            print("Atac no disponible, selecciona un atac viable")
            n = input("Escull l'atac a realitzar: ")
        return self.atacs[int(n)-1]

    def rand_attack(self):
        n = random.choice(range(1, len(self.atacs)+1))
        while not self.valid_attack(n):
            n = random.choice(range(1, len(self.atacs)+1))
        return self.atacs[int(n)-1]

    def attack(self, atac, enemic):
        print(self.nom, 'ha triat', atac.nom)
        atac.restants -= 1
        enemic.vida -= atac.mal

    def valid_index(self, n):
        try:
            return 1 <= int(n) <= len(self.atacs)
        except:
            return False

    def valid_attack(self, n):
        if not self.valid_index(n):
            return False
        else:
            n = int(n)
            atac = self.atacs[n-1]
            if atac.restants <= 0:
                return False
            else:
                return True


class Atac (object):
    def __init__(self, nom, mal, maxim):
        self.nom = nom
        self.mal = mal
        self.maxim = maxim
        self.restants = maxim
