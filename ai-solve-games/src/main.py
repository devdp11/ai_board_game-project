from games.tictactoe.players.TicTacToeMinimax import MinimaxTicTacToePlayer
from games.tictactoe.players.TicTacToeRandom import RandomTicTacToePlayer
from games.tictactoe.players.TicTacToeHuman import HumanTicTacToePlayer
from games.tictactoe.TicTacToeSimulator import TicTacToeSimulator

from games.game_simulator import GameSimulator

def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc}-----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("\nResults for the game:")
    simulator.print_stats()


def main():
    print("ESTG IA Games Simulator")

    name = input("\nIntroduza o seu nome:")
    print(f"Bem Vindo {name}, vamos começar com os jogos!\n")

    num_iterations = 2

    tictactoe_simulations = [
        # uncomment to play as human
        {
           "name": f"\nTicTacToe - {name} VS MiniMax\n",
           "player1": HumanTicTacToePlayer(f"{name}"),
           "player2": MinimaxTicTacToePlayer("MiniMax")
        },
    ]

    for sim in tictactoe_simulations:
        run_simulation(sim["name"], TicTacToeSimulator(sim["player1"], sim["player2"]), num_iterations)


if __name__ == "__main__":
    main()
