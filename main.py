from personagem import HarukiDoro, Negtune
from batalha import iniciar_batalha
from lore import mostrar_lore

def main():
    mostrar_lore()
    
    haruki = HarukiDoro("Haruki Dōro", 100)
    negtune = Negtune("Negtune", 100)

    iniciar_batalha(haruki, negtune)

if __name__ == "__main__":
    main()