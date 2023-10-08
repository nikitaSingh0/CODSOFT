
import tkinter as tk
import random


class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        root.geometry("550x500")
        root.resizable(0,0)
      

        self.rounds_to_play = 0
        self.current_round = 0
        self.score = {"user": 0, "computer": 0}
        self.game_active = False

        # Create labels

        
        self.title_frame = tk.Frame(root, pady=10)
        self.title_frame.pack()
        self.rounds_label = tk.Label(self.title_frame, text="Choose the number of rounds:",font=("Georgia", 12, "bold"),bg="black",fg="white")
        self.rounds_label.pack()
        
        
        self.rounds_frame = tk.Frame(root)
        self.rounds_frame.pack()

        self.btn3 = tk.Button(self.rounds_frame,bg='cornsilk3',fg='black',text='3',width=5,height=2,font=("Georgia", 12, "normal"), command=lambda c=3: self.set_rounds(c))
        self.btn3.pack(side=tk.LEFT)


        self.btn5 = tk.Button(self.rounds_frame,bg='cornsilk3',fg='black',width=5,height=2, text='5',font=("Georgia", 12, "normal"), command=lambda c=5: self.set_rounds(c))
        self.btn5.pack(side=tk.LEFT)

        self.btn10 = tk.Button(self.rounds_frame,bg='cornsilk3',fg='black',width=5,height=2, text='7',font=("Georgia", 12, "normal"), command=lambda c=7: self.set_rounds(c))
        self.btn10.pack(side=tk.LEFT)

        self.btn9 = tk.Button(self.rounds_frame,bg='cornsilk3',fg='black',width=5,height=2, text='9',font=("Georgia", 12, "normal"),command=lambda c=9: self.set_rounds(c))
        self.btn9.pack(side=tk.LEFT)

        self.round_count_label = tk.Label(root, text="Rounds: ",font=("verdana", 19),fg="black")
        self.round_count_label.pack()

        self.lbl_instruction = tk.Label(root, text="Choose Rock, Paper, or Scissor!!!",font=("Helvetica", 20, "bold","underline"),fg='dimgray')
        self.lbl_instruction.pack()

        self.lbl_computer_choice = tk.Label(root, text="")
        self.lbl_computer_choice.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        self.score_label = tk.Label(root, text="")
        self.score_label.pack()

        self.game_result_label = tk.Label(root, text="")
        self.game_result_label.pack()

        # Create frames
        

        self.choices_frame = tk.Frame(root)
        self.choices_frame.pack()

        # Create buttons for each choice
        self.rock_btn = tk.Button(self.choices_frame,bg='cadetblue4',font=("Georgia", 10, "normal"), text="Rock",width=20,height=2, command=lambda: self.on_choice_click("Rock"))
        self.rock_btn.pack(side=tk.LEFT)

        self.paper_btn = tk.Button(self.choices_frame,bg='cadetblue4',font=("Georgia", 10, "normal"), text="Paper",width=20,height=2, command=lambda: self.on_choice_click("Paper"))
        self.paper_btn.pack(side=tk.LEFT)

        self.scissor_btn = tk.Button(self.choices_frame,bg='cadetblue4',font=("Georgia", 10, "normal"), text="Scissor",width=20,height=2, command=lambda: self.on_choice_click("Scissor"))
        self.scissor_btn.pack(side=tk.LEFT)

        # Create buttons for selecting rounds
        round_counts = [3, 5, 10, 9]

        

        # Create "Play" and "Play Again" buttons
        self.start_frame = tk.Frame(root,pady=10,padx=10)
        self.start_frame.pack()
        self.play_btn = tk.Button(self.start_frame, text="Start",fg='white',width=20,height=2 ,bg='#007FFF',font=("Georgia", 15, "bold"),command=self.start_game)
        self.play_btn.pack()
        self.play_again_frame = tk.Frame(root)
        self.play_again_frame.pack()
        self.play_again_btn = tk.Button(self.play_again_frame, text="Play Again!!",fg='black',bg='cornsilk3', width=20,height=2,font=("Georgia", 15, "bold"),command=self.start_game, state=tk.DISABLED)
        self.play_again_btn.pack()

    def set_rounds(self, round_count):
        self.rounds_to_play = round_count
        self.round_count_label.config(text=f"Rounds: {self.rounds_to_play}")

    def start_game(self):
        self.current_round = 0
        self.score = {"user": 0, "computer": 0}
        self.game_active = True
        self.update_score_label()
        self.game_result_label.config(text="")
        self.lbl_computer_choice.config(text="")
        self.enable_choices()
        self.disable_play()

    def play_game(self, user_choice):
        if not self.game_active:
            return

        computer_choice = random.choice(["Rock", "Paper", "Scissor"])
        self.lbl_computer_choice.config(text="Computer chose: " + computer_choice)

        choices = {"Rock": "Paper", "Paper": "Scissor", "Scissor": "Rock"}

        if user_choice == computer_choice:
            self.result_label.config(text="It's a tie!",fg='black', font=("Georgia", 15, "normal","underline"))
        elif choices[computer_choice] == user_choice:
            self.result_label.config(text="You Win!",fg='black', font=("Georgia", 15, "normal","underline"))
            self.score["user"] += 1
        else:
            self.result_label.config(text="Computer Wins!",fg='black', font=("Georgia", 15, "normal","underline"))
            self.score["computer"] += 1

        self.current_round += 1
        self.update_score_label()

        if self.current_round >= self.rounds_to_play:
            self.disable_choices()
            self.determine_game_winner()


    def on_choice_click(self, choice):
        self.play_game(choice)

    def determine_game_winner(self):
        if self.score["user"] > self.score["computer"]:
            self.game_result_label.config(text="Yay!!  You won the game with a score of {}-{}!".format(self.score["user"], self.score["computer"]),fg='darkgreen', font=("Georgia", 15, "bold"))
        elif self.score["user"] < self.score["computer"]:
            self.game_result_label.config(text=":( Computer won the game with a score of {}-{}!".format(self.score["computer"], self.score["user"]),fg='red', font=("Georgia", 15, "bold"))
        else:
            self.game_result_label.config(text="It's a tie game!",fg='#ED9121', font=("Georgia", 15, "bold"))

        self.game_active = False
        self.disable_choices()
        self.enable_play_again()

    def enable_choices(self):
        self.rock_btn.config(state=tk.NORMAL)
        self.paper_btn.config(state=tk.NORMAL)
        self.scissor_btn.config(state=tk.NORMAL)

    def disable_choices(self):
        self.rock_btn.config(state=tk.DISABLED)
        self.paper_btn.config(state=tk.DISABLED)
        self.scissor_btn.config(state=tk.DISABLED)

    def enable_play_again(self):
        self.play_again_btn.config(state=tk.NORMAL)
        self.btn3.config(state=tk.NORMAL)
        self.btn5.config(state=tk.NORMAL)
        self.btn10.config(state=tk.NORMAL)
        self.btn9.config(state=tk.NORMAL)

    def disable_play(self):
        self.play_btn.config(state=tk.DISABLED)
        self.play_again_btn.config(state=tk.DISABLED)

        self.btn3.config(state=tk.DISABLED)
        self.btn5.config(state=tk.DISABLED)
        self.btn10.config(state=tk.DISABLED)
        self.btn9.config(state=tk.DISABLED)

    def update_score_label(self):
        self.score_label.config(text=f"User: {self.score['user']}  Computer: {self.score['computer']}")


if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
