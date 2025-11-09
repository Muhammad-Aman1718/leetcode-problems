# Frames and Phrases

# Introduction
# Sometimes you hear a phrase so good, you just want to frame it and hang it up in your room.
# With the power of computer programming, we can do that digitally!
# Your task is to create a program that will take in a phrase and output the phrase inside a frame
# of asterisks.
# Program Input
# The first line of the input from STDIN will contain a positive integer T denoting the number of
# test cases that follow. Each test case will have the following input:
# • A single line containing a phrase or word of length n characters.
# Example Input:
# 4
# Live Laugh Love
# Bless This Mess
# i have high blood pressure
# A
# Program Output
# For each test case, your program should output the input phrase surrounded by a rectangular
# frame, with each word (counted by spaces) on a separate line. The frame must surround the
# text with no margins. The capitalization of the words must be conserved. Each test case output
# should be separated by a blank line.
# © 2021 California Informatics Competition
# Editor's Choice Fall '21 Page 9 of 21
# Example Output:
# *******
# *Live *
# *Laugh*
# *Love *
# *******
# *******
# *Bless*
# *This *
# *Mess *
# *******
# **********
# *i *
# *have *
# *high *
# *blood *
# *pressure*
# **********
# ***
# *A*
# ***
# Problem Constraints
# T ≤ 100
# 0 < n ≤ 500
# The input phrase may consist of multiple words.
# The input phrase may have certain letters capitalized.
# The input phrase may contain symbols or numbers.


t = int(input())

for _ in range(t):
    phrase = input().split(" ")
    frame: list[str] = []
    maxPhrase = max(phrase, key=len)
    for i in range(len(phrase) + 2):
        if i == 0 or i == len(phrase) + 1:
            frame.append("*" * (len(maxPhrase) + 2))
        else:
            frame.append(
                "*"
                + phrase[i - 1]
                + (" " * (len(maxPhrase) - len(phrase[i - 1])))
                + "*"
            )

    for x in frame:
        print(x)
