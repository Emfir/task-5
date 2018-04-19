import random
import enums


class NumberGuesser():

    def __init__(self):
        self.numberToGues = random.randint(0 , 100);


    def nextGuess(self, clientNumber):
        if clientNumber == self.numberToGues:
            return enums.resultsOfTheGuess.goodGuess

        elif clientNumber > self.numberToGues:
            return enums.resultsOfTheGuess.tooBig
        elif clientNumber < self.numberToGues:
            return enums.resultsOfTheGuess.tooSmall

    # while 1 :
    #
    #     try:
    #         clientNumber = int(input("whats your gues\n"))
    #     except Exception as error:
    #         print("Write proper input!")
    #         continue
    #
    #
    #
    #     if clientNumber == numberToGues:
    #         print ("You guest")
    #         break
    #     elif clientNumber > numberToGues:
    #         print ("to big")
    #     elif clientNumber < numberToGues:
    #         print ("to small")

