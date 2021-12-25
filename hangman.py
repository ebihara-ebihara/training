import random

def hangman():
    answer = ["cat", "dog", "cow", "bird", "tiger"]
    word = random.choice(answer)
    wrong = 0
    stages = ["",
              "---------       ",
              "|       |       ",
              "|       |       ",
              "|       O       ",
              "|      /|\      ",
              "|      / \      ",
              "|               " 
              ]
    rletters = list(word) # ⇒["c", "a", "t"]
    board = ["_"] * len(word) # ⇒["_", "_", "_"]
    win = False
    print("ハングマンへようこそ！")
    
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board)) #　⇒  "間に挿入する文字列".join([連結したい文字列のリスト])
        e = wrong + 1 # ⇒ e = 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {}".format(word))


hangman()
