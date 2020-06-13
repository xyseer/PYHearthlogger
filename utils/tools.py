from variables import *
import json


def sum_stat():
    with open(BUDDY_STAT_PATH, "r")as f:
        all = json.load(f)
    sum = 0
    for key, value in all.items():
        sum += value
    return sum


# def stop_after_x_games(x):
#     with open(BUDDY_STAT_PATH, "r") as f:
#         all=json.load(f)
#     sum=0
