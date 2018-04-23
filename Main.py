from connection import client
import gameManager




while 1:
      while 1:

        anser = input("Do you want to run this aplication as a (C)Client or as a (S)Serever ?\n")
        if anser == "C":
            aplication = client.client()
            aplication.start()
        elif anser == "S":
            aplication = gameManager.gameManager()
            aplication.start()