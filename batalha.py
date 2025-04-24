import time

def iniciar_batalha(jogador1, jogador2):
    print("O comabte comecou se prepare!!!")
    time.sleep(1)
    
    while jogador1.esta_vivo() and jogador2.esta_vivo():
        jogador1.atacar(jogador2)
        jogador2.status()
        time.sleep(1)
        if not jogador2.esta_vivo():
            break

        jogador2.atacar(jogador1)
        jogador1.status()
        time.sleep(1)

    print("\nFim da batalha!")
    if jogador1.esta_vivo():
        print(f" {jogador1.nome} venceu!")
    else:
        print(f"{jogador2.nome} venceu!")