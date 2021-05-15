#!/usr/bin/python3

import os
import yaml
import tkinter as tk
# import tkinter.messagebox as mb

def run_game(executable):
    def game_executor():
        os.system("./" + executable)

    return game_executor

def game_loader():
    with open('catalogue.yaml', 'r') as f:
        cat = yaml.load(f, Loader=yaml.BaseLoader)
    window = tk.Tk()
    window.title("AK Games - game loader")
    window.geometry('800x600')
    row_no = 0
    for game_name in cat:
        btn = tk.Button(window, text=game_name, bg="blue", command=run_game(cat[game_name]['exec']))
        btn.grid(column=0, row=row_no)
        row_no += 1

    window.mainloop()

if __name__ == '__main__':
    game_loader()
