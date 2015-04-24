#!/usr/bin/python3

"""
Given a source string and a destination string write a program to display
sequence of strings to travel from source to destination.

Rules for traversing:
    1. You can only change one character at a time
    2. Any resulting word has to be a valid word from dictionary

Example: Given source word CAT and destination word DOG, one of the valid
         sequence would be
            CAT -> COT -> DOT -> DOG
         Another valid sequence can be
            CAT -> COT -> COG -> DOG 

    One character can change at one time and every resulting word has be a valid
    word from dictionary


This is a form of graph search constrained by a dictionary. The algo gets fun
when you have

    1) words of differing length
        source: cat, dest: apple
        cat -> catl X
        etc.

    2) words where there isn't a direct translation path, ex.
        source: bird, dest: wolf
                v
        bird -> wird X
                 v
                bord X
                  v
                bild X
                   v
                birf X

A possible approach would be a simple-ish algorithm along the lines of:
    1)  For each letter in the source word
            Replace the letter with the positional letter of the destination word
            Do a dictionary lookup to see if the word is valid
            If it is, restart the loop with the new word
            If not, continue to the next letter
    2)  If no solution is found, attempt to mutate any vowels to make new words
    3)  If vowel mutation is successful, goto (=D) 1
    4)  Attempt to mutate consonants
    5)  If unsuccessful, flip table
"""
