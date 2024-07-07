#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 10:49:51 2023

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


def get_number_next_card(winner,numbers):
    return len(lst_win = [x for x in winner if x in numbers])


def main():
    inp = load_file("input.txt")
    result = 0
    for line in inp :
        winner, numbers = get_winner_and_numbers(line)
        number_next_card = get_number_next_card(winners, numbers)
    

main()