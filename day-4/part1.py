#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 09:42:39 2023

@author: orane
"""

def load_file(file):
    with open(file, "r") as f:
        text = f.readlines()
    return text

def get_winner_and_numbers(line):
    winner = line.split(":")[1].split("|")[0].split()
    numbers = line.split(":")[1].split("|")[1].split()
    return winner,numbers

def compute_card_worth(winner,numbers):
    worth = 0
    lst_win = [x for x in winner if x in numbers]
    if len(lst_win) > 0 :
        worth = 1
        if len(lst_win) > 1 :
            for i in range(len(lst_win)-1) :
                worth *= 2
    return worth

def main():
    inp = load_file("input.txt")
    result = 0
    for line in inp :
        winner, numbers = get_winner_and_numbers(line)
        card_worth = compute_card_worth(winner,numbers)
        result += card_worth
    
    print(result)
    
main()
    