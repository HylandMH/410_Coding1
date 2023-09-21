#!/usr/bin/env python3

print("The Test Scores application")
print()

more_tests = "y"

while more_tests.lower() == "y":
    print("Enter test scores")
    print("Enter 'end' to end input")
    print("========================")
    print()

    counter = 0
    score_total = 0
    test_score = 0

    more_tests = input("Enter another set of teset scores (y/n)? ")

    print("bye")