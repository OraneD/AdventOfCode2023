#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 15:31:44 2024

@author: orane
"""
from collections import Counter

example = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

def get_cards(inp):
    cards = []
    for line in inp.split("\n"):
        if line != "":
            cards.append((line.split()[0], line.split()[1]))
    return cards

def conversion(letter):
    if letter == "A" : return 20
    if letter == "K" : return 19
    if letter == "Q" : return 18
    if letter == "J" : return 17
    if letter == "T" : return 16
    
def get_hand_type(hand):
        if len(set(hand[0])) == 5 :
            return (hand[0], hand[1], "High card",1)
        if hand[0].count(hand[0][0]) == 5 :
            return (hand[0], hand[1], "Five of a kind", 7)
        if hand[0].count(hand[0][0]) == 4 or hand[0].count(hand[0][1]) == 4 :
            return (hand[0], hand[1], "Four of a kind",6)
        if len(set(hand[0])) == 2 and (hand[0].count(list(set(hand[0]))[0]) == 2 or hand[0].count(list(set(hand[0]))[1]) == 2):
            return (hand[0], hand[1],"Full house",5)
        if len(set(hand[0])) == 3 :
            if list(Counter(hand[0]).values()).count(2) == 2 :
                return (hand[0], hand[1], "Two pair",3)
        if len(set(hand[0])) == 3 :
            return (hand[0], hand[1], "Three of a kind",4)
        if len(set(hand[0])) == 4 :
            return (hand[0], hand[1], "One pair",2)

def compare_hand(hand_1, hand_2):
        i = 0
        if hand_1[0] == hand_2[0] :
            return hand_1
        while hand_1[0][i] == hand_2[0][i]:
            i += 1
            continue
        if hand_1[0][i].isalpha() and hand_2[0][i].isalpha():
            if conversion(hand_1[0][i]) > conversion(hand_2[0][i]):
               # print(f"{hand_1[0]} and {hand_2[0]}, winner = {hand_1[0]}")
                return hand_1
            else : 
               # print(f"{hand_1[0]} and {hand_2[0]}, winner = {hand_2[0]}")

                return hand_2
        elif hand_1[0][i].isalpha() and hand_2[0][i].isdigit():
                #print(f"{hand_1[0]} and {hand_2[0]}, winner = {hand_1[0]}")
                return hand_1
        elif hand_1[0][i].isdigit() and hand_2[0][i].isalpha() :
                #print(f"{hand_1[0]} and {hand_2[0]}, winner = {hand_2[0]}")
                return hand_2
        elif hand_2[0][i].isdigit() and hand_1[0][i].isdigit():
            if int(hand_1[0][i]) > int(hand_2[0][i]):
               # print(f"{hand_1[0]} and {hand_2[0]}, winner = {hand_1[0]}")
                return hand_1
            else :
               # print(f"{hand_1[0]} and {hand_2[0]}, winner = {hand_2[0]}")
                return hand_2

def separate_hand(sorted_hand):
    seven = [x for x in sorted_hand if x[3] == 7]
    six = [x for x in sorted_hand if x[3] == 6]
    five = [x for x in sorted_hand if x[3] == 5]
    four = [x for x in sorted_hand if x[3] == 4]
    three = [x for x in sorted_hand if x[3] == 3]
    two = [x for x in sorted_hand if x[3] == 2]
    one = [x for x in sorted_hand if x[3] == 1]
    return [seven, six, five, four, three, two, one]


def second_sort(hand_lst):
    """Selection Sort"""
    sorted_hand = []
    while len(hand_lst) > 1 :
        candidate = hand_lst[0]
        for i in range(len(hand_lst)):
            if compare_hand(candidate, hand_lst[i]) == candidate :
               continue
            elif compare_hand(candidate, hand_lst[i]) == hand_lst[i]:
                candidate = hand_lst[i]
        hand_lst.pop(hand_lst.index(candidate))
        sorted_hand.append(candidate)   
        continue

    if len(hand_lst) == 1 :
        sorted_hand.append(hand_lst[0])
    return sorted_hand

def count_score(sorted_hand):
    score = 0
    for i in range(1, len(sorted_hand) +1):
        score += int(sorted_hand[i-1][1]) * (len(sorted_hand) + 1 - i)
        print( int(sorted_hand[i-1][1]), len(sorted_hand) + 1 - i)
        print(len(sorted_hand) + 1 - i, sorted_hand[i-1])
    return score
        
def main():
    with open("input.txt", "r") as f :
        inp = f.read()
    cards = get_cards(inp)
   # print(len(cards))
    hand_types = []
    for hand in cards :
        hand_types.append(get_hand_type(hand))
    hand_types.sort(key = lambda x: x[3], reverse = False)
    separated_hands = separate_hand(hand_types)
   # print(separated_hands)
    all_sorted = []
    for hand in separated_hands:
        if hand != []:
            all_sorted.append(second_sort(hand))
        else :
            all_sorted.append(hand)
    #print(f"All sorted : {all_sorted}")
    all_sorted = [x for j in all_sorted for x in j]
   # print(all_sorted)
    with open("all_sorted.txt", "w" ) as file :
        for hand in all_sorted :
            file.write(f"{hand}\n")
    score = count_score(all_sorted)
    print(f"Score  : {score}")
    
            
            
            
            
        

main()
    
        

    
    
    
    