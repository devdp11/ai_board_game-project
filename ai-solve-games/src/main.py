from games.mijnlieff.players.MijnlieffMinimax import MinimaxMijnlieffPlayer
from games.mijnlieff.players.MijnlieffGreedy import GreedyMijnlieffPlayer
from games.mijnlieff.players.MijnlieffRandom import RandomMijnlieffPlayer
from games.mijnlieff.players.MijnlieffHuman import HumanMijnlieffPlayer
from games.mijnlieff.MijnlieffSimulator import MijnlieffSimulator

from games.game_simulator import GameSimulator

def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"\n----- {desc} -----\n")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("\n\nResults for the game:")
    print(simulator.print_stats())
    
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
    

    num_iterations = 100
    while True:

        print("\n1 - Player vs Player")
        print("2 - Player vs Computer")
        print("3 - Computer vs Computer")
        print("0 - Return to Lobby")
        
        escolha = input("Select and option: ")

        if escolha not in ["0", "1", "2", "3"]:
            print("\nWrong Option | Choose another...")
            continue

        if escolha in ["2", "3"]:
            if True:

                try:
                    if escolha in ["3"]:
                        num_iterations = int(input("\nChoose how many interactions you want: "))
                        if num_iterations <= 0 or not int:
                            return

                    print("\n1 - Random")
                    print("2 - Greedy")
                    print("3 - Minimax")
                    level = input("Select a Difficulty: ")
                except ValueError:
                    return
        
        if escolha in "1":
            mijnlieff_simulations = [
                {
                    "name": "Mijnlieff",
                    "player1": HumanMijnlieffPlayer("Player1"),
                    "player2": HumanMijnlieffPlayer("Player2")
                }
            ]
 
        elif escolha in "2" and level not in ["1", "2", "3"]:
            print("\nYou have to choose a valid level...")
            continue
        
        elif escolha in "2" and level in "1":
            mijnlieff_simulations = [
                {
                    "name": "Mijnlieff - Player - Random",
                    "player1": HumanMijnlieffPlayer("Player1"),
                    "player2": RandomMijnlieffPlayer("Random")
                }
            ]
        elif escolha in "3" and level in "1":
            mijnlieff_simulations = [
                {
                    "name": "Mijnlieff - Random1 - Random2",
                    "player1": RandomMijnlieffPlayer("Random1"),
                    "player2": RandomMijnlieffPlayer("Random2")
                }
            ]

        elif escolha in '0':
            return
    
        for sim in mijnlieff_simulations:
            run_simulation(sim["name"], MijnlieffSimulator(sim["player1"], sim["player2"]), num_iterations)

menu()