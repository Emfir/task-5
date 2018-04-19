import NumberGuesser
import enums


class gameGuess():

    def start(self):
        engine = NumberGuesser.NumberGuesser()

        while 1:

            try:
                clientNumber = int(input("whats your guess\n"))
            except Exception as error:
                print("Write proper input!")
                continue

            output = engine.nextGuess(clientNumber)


            print (output.value)
            if output == enums.resultsOfTheGuess.goodGuess:
                break

