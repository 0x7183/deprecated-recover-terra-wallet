from tkinter import *
from brute import *

def main():

    root = Tk()

    with open('../en.txt') as f:
        words = f.read().splitlines()

    root.title("Recover your Terra Wallet")

    canvas = Canvas(root, width=450, height=45)
    canvas.pack()

    seed = Entry(root, width=100)
    seed.insert(0, "Delete and enter your seed phrase")
    seed.pack()

    pub_key = Entry(root, width=50)
    pub_key.insert(0, "Delete and enter your address")
    pub_key.pack()

    result = Label(root, text='')
    result.pack()

    startBtn = Button(root, text="Start")
    startBtn.config(command=lambda: result.config(text=brute(seed.get(), words, pub_key.get())))
    startBtn.pack()

    root.mainloop()



if __name__ == "__main__":
    main()
