from tkinter import *
from tkinter import messagebox
import random

class TIC_TAC_TOE_AI:
    def __init__(self, root):
        self.window = root
        self.setup_ui()
        self.reset_game()

    def setup_ui(self):
        self.window.title("Tic-Tac-Toe AI")
        self.canvas = Canvas(self.window, background="#333", relief=RAISED, bd=3)
        self.canvas.pack(fill=BOTH, expand=1)

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = Button(self.canvas, text="", font=("Arial", 20, "bold"), width=5, height=2, bg="#444", fg="#FFF",
                                activebackground="#555", bd=3, command=lambda i=i, j=j: self.human_play(i*3+j+1))
                button.grid(row=i, column=j, padx=10, pady=10)
                row.append(button)
            self.buttons.append(row)

        self.btn_frame = Frame(self.canvas, bg="#333")
        self.btn_frame.place(relx=0.5, rely=0.9, anchor=CENTER)

        self.start_btn = Button(self.btn_frame, text="Start Game", font=("Arial", 15, "bold"), bg="#444",
                                fg="#9d9dff", command=self.start_game)
        self.start_btn.grid(row=0, column=0, padx=10)

        self.reset_btn = Button(self.btn_frame, text="Reset", font=("Arial", 15, "bold"), bg="#444", fg="#9d9dff", state=DISABLED,
                                command=self.reset_game)
        self.reset_btn.grid(row=0, column=1, padx=10)

    def reset_game(self):
        self.machine_moves = []
        self.human_moves = []
        self.signs = {}
        self.move_count = 0
        self.enable_buttons()
        self.update_buttons()
        self.start_btn.config(state=NORMAL)
        self.reset_btn.config(state=DISABLED)

    def start_game(self):
        self.start_btn.config(state=DISABLED)
        self.reset_btn.config(state=NORMAL)
        self.enable_buttons()

    def enable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state=NORMAL, text="")

    def update_buttons(self):
        for move, sign in self.signs.items():
            row, col = divmod(move - 1, 3)
            self.buttons[row][col].config(text=sign, state=DISABLED, disabledforeground="#0F0" if sign == "X" else "red")

    def machine_play(self):
        available_moves = [i for i in range(1, 10) if i not in self.signs]
        move = random.choice(available_moves)
        self.make_move(move, "X")

    def human_play(self, move):
        if move in self.signs:
            return
        self.move_count += 1
        self.make_move(move, "O")
        if self.move_count < 9 and not self.check_winner("O"):
            self.machine_play()

    def make_move(self, move, sign):
        self.signs[move] = sign
        self.update_buttons()
        if self.check_winner(sign):
            messagebox.showinfo("Game Over", f"{'Computer' if sign == 'X' else 'Human'} wins!")
            self.end_game()
        elif self.move_count == 9:
            messagebox.showinfo("Game Over", "It's a tie!")
            self.end_game()

    def check_winner(self, sign):
        win_conditions = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
        for condition in win_conditions:
            if all(self.signs.get(pos) == sign for pos in condition):
                return True
        return False

    def end_game(self):
        for row in self.buttons:
            for button in row:
                button.config(state=DISABLED)

if __name__ == "__main__":
    root = Tk()
    game = TIC_TAC_TOE_AI(root)
    root.mainloop()
