#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 18:53:44 2024

@author: orane
"""

def collect_maps(inp):
    dico = {}
    lines = inp.split("\n")
    for line in lines :
        if ":" in line :
            new_key = line.split(":")[0]
            value_list = []
            if new_key == "seeds" :
                seeds = [int(x) for x in line.split(":")[1].split()]
                dico[new_key] = seeds
        if  line != ""  and ":" not in line :
            value_list.append([int(x) for x in line.split()])
            dico[new_key] = value_list  
    return dico

def transform_values(initial_values, mapping):
    transformed_values = []
    for seed in initial_values :
        for i, line in enumerate(mapping):
            if seed >= line[1] and seed <= line[1] + line[2] :
                #print(f"{seed}, {line} yes")
                transformed_values.append(line[0] + abs(line[1] - seed))
                break
            if i == len(mapping)-1 : 
              # print(f"{seed}, {line} no")
               transformed_values.append(seed)
    return transformed_values

def main():
    with open("input.txt", "r") as file:
        inp = file.read()
    maps = collect_maps(inp)
    seeds = maps["seeds"]
    for i, key in enumerate(maps) :
        if i == len(maps) - 1 :
            break
        if key == "seeds" :
            initial_values = maps["seeds"]
            mapping = maps["seed-to-soil map"]
            transformed_values = transform_values(initial_values,mapping)
            initial_values = transformed_values
            continue
        mapping = maps[list(maps.keys())[i+1]]
        transformed_values = transform_values(initial_values, mapping)
        initial_values = transformed_values
    print(min(transformed_values))
main()
    
        
            
    
        

         

    
            