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
        while len(self.mines) < mines:
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            self.mines.add((x, y))
        
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
                        print(count if count > 0 else ' ', end=' ')  # <-- Fix here
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
        # Si une mine est trouvée, retourne False (game over)
        if (x, y) in self.mines:
            return False
        self.revealed[y][x] = True
        
        # Si aucune mine autour, révèle les cases adjacentes
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def valid_coordinates(self, x, y):
        """Check if the coordinates are within the game board bounds."""
        return 0 <= x < self.width and 0 <= y < self.height

    def check_win(self):
        """Check if the player has revealed all non-mine cells."""
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) not in self.mines and not self.revealed[y][x]:
                    return False  # If there's any non-mine cell that's not revealed
        return True  # All non-mine cells have been revealed

    def play(self):
        while True:
            self.print_board()
            try:
                # Validate user input for x-coordinate
                while True:
                    try:
                        x = int(input(f"Enter x coordinate (0 to {self.width - 1}): "))
                        if self.valid_coordinates(x, 0):
                            break
                        else:
                            print("Invalid x-coordinate. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                
                # Validate user input for y-coordinate
                while True:
                    try:
                        y = int(input(f"Enter y coordinate (0 to {self.height - 1}): "))
                        if self.valid_coordinates(0, y):
                            break
                        else:
                            print("Invalid y-coordinate. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
                
                # Check if the player has won
                if self.check_win():
                    self.print_board(reveal=True)
                    print("Congratulations! You've won the game.")
                    break

            except KeyboardInterrupt:
                print("\nGame interrupted. Exiting...")
                break

if __name__ == "__main__":
    game = Minesweeper()
    game.play()

