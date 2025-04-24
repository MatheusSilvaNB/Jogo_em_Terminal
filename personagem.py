import time
import random

class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def esta_vivo(self):
        return self.vida > 0

    def status(self):
        print(f"{self.nome} tem {self.vida} de vida.")

class HarukiDoro(Personagem):
    def atacar(self, inimigo):
        print("Haruki Dōro invoca dois cones coberto de fogo explosivo e lança contra Negtune ")
        time.sleep(1)
        dano = random.randint(10, 20)
        inimigo.vida -= dano
        print(f"{inimigo.nome} perdeu {dano} de vida!")

class Negtune(Personagem):
    def atacar(self, inimigo):
        print("Negtune invoca acima de sua cabeca a aura de um dado, querendo causar uma imprevisibilidade no combate ")
        time.sleep(1)
        chance = random.randint(1, 6)
        if chance <= 3:
            print("O ataque é eminente, Negtsune causa dano ")
            dano = random.randint(15, 25)
            inimigo.vida -= dano
            print(f"{inimigo.nome} perdeu {dano} de vida!")
        else:
            print("A imprevisibilade do dado o atrapalha, sua magia falha")