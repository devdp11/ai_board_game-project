from games.mijnlieff.players.MijnlieffMinimax import MinimaxMijnlieffPlayer
from games.mijnlieff.players.MijnlieffRandom import RandomMijnlieffPlayer
from games.mijnlieff.players.MijnlieffHuman import HumanMijnlieffPlayer
from games.mijnlieff.MijnlieffSimulator import MijnlieffSimulator
from games.mijnlieff.MijnlieffRules import MijnlieffRules

from games.game_simulator import GameSimulator

def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc}-----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("\nResults for the game:")
    simulator.print_stats()
    

"""def menu():
    print("[1] - Human vs Human")
    print("[2] - Human vs Random")
    print("[3] - Human vs Minimax")
    print("[4] - Minimax vs Random")
    print("[0] - Close Program")

    escolha = int(input("\nEscolha uma opção:"))"""

def main():
    print("\n INTELIGÊNCIA ARTIFICIAL TP1 GAME")

    name = input("\nIntroduza o seu nome:\t")
    print(f"Bem Vindo {name}, vamos começar com os jogos!\n")
    
    num_iterations = 2

    mijnlieff_simulations = [
        {
           "name": f"\nMijnLieff - {name} VS MiniMax\n",
           "player1": HumanMijnlieffPlayer(f"{name}"),
           "player2": MinimaxMijnlieffPlayer("MiniMax")
        },
    ]

    for sim in mijnlieff_simulations:
        run_simulation(sim["name"], MijnlieffSimulator(sim["player1"], sim["player2"]), num_iterations)


if __name__ == "__main__":
    main()
