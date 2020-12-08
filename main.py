#!/usr/bin/python3

from random import shuffle
from sys import argv
from time import perf_counter

# Restrict category count to the first x
if len(argv) == 2:
    max_category_index = int( argv[1] )
elif len(argv) == 3:
    min_category_index = int( argv[1] )
    max_categoryo_index = int( argv[2] )

category1 = [
    "Category 1 Name",
    {
        "Question 1" : "Yes",
        "Question 2" : "No"
    }
]

category2 = [
    "Category 2 Name",
    {
        "Question 1" : "Yes",
        "Question 2" : "No"
    }
]

categories = [
    category1,
    category2
    ]

flashcards = {}
flashcards_keys = []
correct_keys = []
questions_asked = 0.0

tic = perf_counter()

category_counter = 0
if not "min_category_index" in locals():
    min_category_index = 0
if not "max_category_index" in locals():
    max_category_index = len( categories )

for category in categories:
    if category_counter < min_category_index:
        category_counter += 1
    elif category_counter >= min_category_index and category_counter <= max_category_index:
        category_counter += 1
        category_name = category[ 0 ]
        category_questions = category[ 1 ]
        for question in category_questions:
            key = category_name + " | " + question
            flashcards[ key ] = category_questions[ question ]
            flashcards_keys.append( key )

while len( flashcards_keys ) != len( correct_keys ):
    shuffle( flashcards_keys )
    for question in flashcards_keys:
        if question not in correct_keys:
            user_response = input( question + ": " )
            questions_asked += 1
            if user_response == flashcards [ question ]:
                print( "CORRECT!" )
                correct_keys.append( question )
            else:
                print( "INCORRECT" )
                print( "Correct answer was: " + flashcards[ question ] )
            print( "" )

print( "" )
toc = perf_counter()
print( "Completed in " + str( int( toc - tic ) ) + " seconds." )
accuracy = "{:.2f}".format( ( len( flashcards ) / questions_asked ) * 100 )
print( "Accuracy: " + str( accuracy ) + "%" )   
