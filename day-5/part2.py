#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 21:00:56 2024

@author: orane
"""

example= """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
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



def collect_intervals(seeds):
    intervals = []
    for i in range(1,len(seeds), 2):
        intervals.append((seeds[i-1], seeds[i-1] + seeds[i]-1))
    return intervals

def test_intervals(intervals, mapping):
    transformed_seeds = []
    for interval in intervals :
        for i, line in enumerate(mapping):
            if interval[1] < line[1] or interval[0] > line[1] + line[2] and i == len(mapping) - 1: #No overlap
                transformed_seeds.append((interval[0], interval[1]))
            elif interval[0]  in range(line[1], line[1] + line[2]) and interval[1] in range(line[1], line[1] + line[2]) : #Full overlap
                transformed_seeds.append((line[0] + abs(line[1] - interval[0]), line[0] + abs(line[1] - interval[1])))
                break
            elif interval[0]  in range(line[1], line[1] + line[2]) : #Overlap from left 
                transformed_seeds.append((line[0] + abs(line[1] - interval[0]), interval[0] + line[2]))
                break
            elif interval[1]  in range(line[1], line[1] + line[2]) : #Overlap from right
                transformed_seeds.append((line[0] + abs(line[1] - interval[1]), interval[1] - line[2]))
                break
    return transformed_seeds


    
def main():
    with open("input.txt", "r") as file:
        inp = file.read()
    maps = collect_maps(inp)
    seeds = maps["seeds"]
    intervals = collect_intervals(seeds)

    for i, key in enumerate(maps) :
        if i == len(maps) - 1 :
            break
        if key == "seeds":
            initial_values = test_intervals(intervals, maps[list(maps.keys())[i+1]])
            continue
        mapping = maps[list(maps.keys())[i+1]]
        transformed_values = test_intervals(initial_values, mapping)
        initial_values = transformed_values
    
    print(transformed_values)
        
   # result = [j for i in transformed_values for j in i ]
   # print(result)
   # print(min(result))

        

        
       
main()


