#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set()
        # Placer les mines de manière correcte en utilisant des coordonnées (x, y)
        while len(self.mines) < mines:
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            self.mines.add((x, y))  # Ajouter les mines en utilisant des coordonnées (x, y)
        
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (x, y) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (nx, ny) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if (x, y) in self.mines:
            return False
        self.revealed[y][x] = True
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def check_win(self):
        """Check if the player has revealed all non-mine cells."""
        for y in range(self.height):
            for x in range(self.width):
                # Si la case n'est pas une mine et qu'elle n'a pas été révélée
                if (x, y) not in self.mines and not self.revealed[y][x]:
                    return False  # Il y a encore des cases non-mines non révélées
        return True  # Toutes les cases non-mines ont été révélées

    def play(self):
        while True:
            self.print_board()  # Affiche la grille à chaque tour
            try:
                # Demande les coordonnées x et y avec une validation des entrées
                x = int(input(f"Enter x coordinate (0 to {self.width - 1}): "))
                y = int(input(f"Enter y coordinate (0 to {self.height - 1}): "))
                
                # Vérification que les coordonnées sont dans les limites du plateau
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print(f"Coordinates out of bounds. Please enter values between 0 and {self.width - 1} for x, and between 0 and {self.height - 1} for y.")
                    continue

                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break

                # Vérification de la victoire
                if self.check_win():
                    self.print_board(reveal=True)
                    print("Congratulations! You've won the game.")
                    break

            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
