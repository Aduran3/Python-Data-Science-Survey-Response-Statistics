# Data Science: Visualized statistics
#
# @author     Duran, Aaron
# @date       12/05/2021

import random
import numpy as np
import matplotlib.pyplot as plt


# Generating 50 random responses rating the food in a cafeteria
# feel free to change this to serve your data
def GenerateResponses():
    responses = []
    for i in range(50):                           # the for loop appends 50 random responses from 1 to 5
        responses.append(random.randint(1, 5))
    return responses


# Determining the frequency of responses in dictionary form
def Frequency(responses):
    frequencies = {}
    for item in responses:            # the for loop inserts the argument's (responses) values
        if item in frequencies:       # into the dictionary "frequencies"
            frequencies[item] += 1
        else:
            frequencies[item] = 1
    return frequencies


# Here the response list is turned into an array for statistical purposes
def CreateArrayStats(responses):
    ArrayResponses = np.array(responses)
    return ArrayResponses


# a dictionary is used as an argument and its values are used in
# creating a bar chart with matplotlib
def FrequencyBarChart(frequency):
    plt.bar(frequency.keys(), frequency.values())
    plt.title('Response Frequencies')
    plt.xlabel('Response Options')
    plt.ylabel('Frequency')
    plt.show()


# The main function, used to put other functions together
# and test/display the information
def main():
    responses = GenerateResponses()                    # responses is defined with 50 random ratings
    frequencies = Frequency(responses)                 # frequencies is defined using responses as an argument
    ArrayResponses = CreateArrayStats(responses)       # an array is defined using the responses

    print("This program serves to gather 50 ratings of food from 1 to 5")
    print("and display various statistical information regarding the ratings.")
    print()

    print("Responses:", end=" ")
    for i in responses:                                # for loop used to cleanly print the responses
        print(i, end=" ")
    print()

    print("Frequency: ", end="")
    for key, value in sorted(frequencies.items()):     # for loop used to clearly display the frequency dictionary
        print(str(key) + ":" + str(value), end="  ")   # in key order
    print()

    print("Minimum:", ArrayResponses.min())            # Various statistical information is printed using
    print("Maximum:", ArrayResponses.max())            # the array created and numpy operators
    print("Range:", np.ptp(ArrayResponses))
    print("Mean:", ArrayResponses.mean())
    print("Median:", np.median(ArrayResponses))
    print("Variance:", ArrayResponses.var())
    print("Standard Deviation:", ArrayResponses.std())

    FrequencyBarChart(frequencies)                    # the function is called to display a bar graph of frequency

main()
