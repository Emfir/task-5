from connection import client, server
import gameGuess




while 1:
    anser = input("Do you want to play a (T)TicTacToe or (N)NumberGuesser?\n")
    if anser == "N":
        game = gameGuess.gameGuess()
        game.start()
    elif anser == "T":
        while 1:

            anser = input("Do you want to run this aplication as a (C)Client or as a (S)Serever ?\n")
            if anser == "C":
                aplication = client.client()
                aplication.start()
            elif anser == "S":
                aplication = server.server()
                aplication.start()