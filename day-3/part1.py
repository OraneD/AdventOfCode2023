#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 14:14:03 2023

@author: orane
"""
import re
import pandas as pd

def load_input(file):
    with open(file, 'r') as f :
        lines = f.readlines()
    return [line.strip() for line in lines]

inp = load_input("test.txt")

def get_matrix(inp):
    matrix = []
    for line in inp :
        matrix.append(list(line))
    
    
    return matrix

matrix = get_matrix(inp)

def get_indexes_number(matrix):
    i = 0
    lst_numbers_lines = []
    while i < len(matrix) :
        line = matrix[i]
        i_line= 0
        lst_numbers_line = []
        while i_line < len(line) :
            car = str(line[i_line])
            if car.isdigit():
                index_num = [i_line]
                c = 1
                num = car
                #print(num)
                next_car = i_line + c
                while next_car < len(line) and str(line[next_car]).isdigit() :
                    #print(f' Next car : {line[next_car]}')
                    num += str(line[next_car])
                    index_num.append(next_car)
                    #print(f'Num : {num}')
                    c += 1
                    next_car = i_line + c
                lst_numbers_line.append(index_num)
                i_line += len(num)
                continue
            i_line += 1
        lst_numbers_lines.append(lst_numbers_line)
        i += 1
    return lst_numbers_lines

indexes = get_indexes_number(matrix)

def get_number(line, indexes):
    num = ""
    i = 0
    while i < len(indexes):
        num += line[indexes[i]]
        i += 1
    return num
        

not_symbols = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
result = 0
for i, index in enumerate(indexes):
    print(f'Number of line : {i}, line : {matrix[i]}')

    if i != 0 and i < len(matrix) - 1:
        print("i pas 0 et pas len matrix")
        for set_pos_number in index :
            for pos_number in set_pos_number:
                #Check line
                if pos_number - 1 > 0 and pos_number + 1 < len(matrix[i]) -1:
                    if matrix[i][pos_number -1] not in not_symbols  :
                        num = get_number(matrix[i], set_pos_number)
                        print(num)
                        result+= int(num)
                        break
                    elif matrix[i][pos_number + 1] not in not_symbols :
                        num = get_number(matrix[i], set_pos_number)
                        print(num)
                        result+= int(num)
                        break
                # Check previous line
                if pos_number - 1 > 0 and pos_number + 1 < len(matrix[i-1]):
                    if matrix[i-1][pos_number -1] not in not_symbols  :
                        num = get_number(matrix[i], set_pos_number)
                        print(num)
                        result+=int(num)
                        break
                    elif matrix[i-1][pos_number + 1] not in not_symbols:
                        num = get_number(matrix[i], set_pos_number)
                        print(num)
                        result+=int(num)
                        break
                elif matrix[i-1][pos_number] not in not_symbols :
                    num = get_number(matrix[i], set_pos_number)
                    print(num)
                    result+= int(num)
                    break
                #Check next line
                if pos_number - 1 > 0 and pos_number != len(matrix[i+1]) -1:
                    if matrix[i+ 1][pos_number -1] not in not_symbols :
                        num = get_number(matrix[i], set_pos_number)
                        print(num)
                        result+= int(num)
                        break
                    elif matrix[i + 1][pos_number + 1] not in not_symbols :
                        num = get_number(matrix[i], set_pos_number)
                        print(num)
                        result+= int(num)
                        break
                elif matrix[i + 1 ][pos_number] not in not_symbols :
                    num = get_number(matrix[i], set_pos_number)
                    print(num)
                    result+= int(num)
                    break

    if i == 0  :
        print("i = 0")
        for set_pos_number in index :
            for pos_number in set_pos_number:
                #Check line 
                if pos_number - 1 > 0 and pos_number + 1 < len(matrix[i]):
                    if matrix[i][pos_number -1] not in not_symbols  :
                        num = get_number(matrix[i], set_pos_number)
                        result+= int(num)
                        break
                    elif matrix[i][pos_number + 1] not in not_symbols :
                        num = get_number(matrix[i], set_pos_number)
                        result+= int(num)
                        break
                #Check next line
                if pos_number - 1 > 0 and pos_number != len(matrix[i+1]) -1:
                    if matrix[i+ 1][pos_number -1] not in not_symbols :
                        num = get_number(matrix[i], set_pos_number)
                        print(num)
                        result+= int(num)
                        break
                    elif matrix[i + 1][pos_number + 1] not in not_symbols :
                        num = get_number(matrix[i], set_pos_number)
                        print(num)
                        result+= int(num)
                        break
                elif matrix[i + 1 ][pos_number] not in not_symbols :
                    num = get_number(matrix[i], set_pos_number)
                    print(num)
                    result+= int(num)
                    break
    if i == len(matrix) - 1 :
        print("i len matrix")
        for set_pos_number in index :
            for pos_number in set_pos_number:
                #Check line 
                if pos_number - 1 > 0 and pos_number + 1 < len(matrix[i]):
                    if matrix[i][pos_number -1] not in not_symbols  :
                        num = get_number(matrix[i], set_pos_number)
                        result+= int(num)
                        break
                    elif matrix[i][pos_number + 1] not in not_symbols :
                        num = get_number(matrix[i], set_pos_number)
                        result+= int(num)
                        break
                # Check previous line
                if pos_number - 1 > 0 and pos_number + 1 < len(matrix[i-1]):
                    if matrix[i-1][pos_number -1] not in not_symbols  :
                        num = get_number(matrix[i], set_pos_number)
                        print(num)
                        result+=int(num)
                        break
                    elif matrix[i-1][pos_number + 1] not in not_symbols:
                        num = get_number(matrix[i], set_pos_number)
                        print(num)
                        result+=int(num)
                        break
                elif matrix[i-1][pos_number] not in not_symbols :
                    num = get_number(matrix[i], set_pos_number)
                    print(num)
                    result+= int(num)
                    break
                
print(result)
                
                
        

            
    
    

            