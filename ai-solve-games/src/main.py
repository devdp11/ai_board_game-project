from games.mijnlieff.players.MijnlieffMinimax import MinimaxMijnlieffPlayer
from games.mijnlieff.players.MijnlieffRandom import RandomMijnlieffPlayer
from games.mijnlieff.players.MijnlieffHuman import HumanMijnlieffPlayer
from games.mijnlieff.MijnlieffSimulator import MijnlieffSimulator

from games.game_simulator import GameSimulator

def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"\n----- {desc} -----\n")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("\nResults for the game:")
    simulator.print_stats()
    
def menu():
    while(True):
        print("\n[1] - Play Mijnlieff")
        print("[2] - Mijnlieff Gameplay Information")
        print("[0] - Close Program")

        escolha = int(input("\nEscolha uma opção:"))

        if escolha > 3:
            print("\nWrong Option | Choose another...")
            continue

        if escolha == 1:
            main()
        elif escolha == 2:
            information()
        elif escolha == 0:
            print("\nLeaving the Program...")
            break

def information():
    print("\n-- Regras do Jogo --")
    print('Peça  Straights (S) - Ao jogar esta peça, o oponente só poderá jogar nas posições retas à ultima peça colocada.')
    print('Peça  Diagonals (D) - Ao jogar esta peça, o oponente só poderá jogar nas posições diagonais à ultima peça colocada.')
    print('Peça  Pushers (H) - Ao jogar esta peça, o oponente só poderá jogar nas posições não adjacentes à ultima peça colocada.')
    print('Peça  Pullers (L) - Ao jogar esta peça, o oponente só poderá jogar nas posições adjacentes à ultima peça colocada.\n')
    print("-> O jogo só termina quando o tabuleiro esta completo ou quando o jogador já não consegue colocar mais nenhuma peça.")
    print("-> A primeira jogada poderá ser em qualquer lugar do tabuleiro mas de adiante as jogadas terão que respeitar o regulamento conforme as peças.")
    print("-> O jogador terá 8 peças, 2 de cada tipo podendo usar apenas cada tipo 2 vezes e não podendo mudar a posição depois de colocada.\n")

    

def main():
    print("\nINTELIGÊNCIA ARTIFICIAL TP1 GAME")
    
    num_iterations = 1

    mijnlieff_simulations = [
        {
           "name": "MijnLieff - Player VS Random",
           "player1": HumanMijnlieffPlayer("Player"),
           "player2": RandomMijnlieffPlayer("Random")
        },
       """  {
           "name": sim_name,
           "player1": player1,
           "player2": player2
        }, """
    ]

    for sim in mijnlieff_simulations:
        run_simulation(sim["name"], MijnlieffSimulator(sim["player1"], sim["player2"]), num_iterations)

menu()
