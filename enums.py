from enum import Enum

class game_state(Enum):
    x_won = "x"
    o_won = "o"
    draw = 2
    game_is_not_finished = 3


class players(Enum):
    x = 0
    o = 1

class error(Enum):
    different_position = "This position does not exist or is already ocupied. Write different position "
    proper_position = "Write proper position"


class resultsOfTheGuess(Enum):
    tooSmall = "too Small"
    tooBig   = "too Big"
    goodGuess = "good guess"


class typeOfMessage (Enum):
    informationRequireResponse = 0
    gameInformationDoNotExpectResponse = 1
    actionInformation = 3
    finalMessageFromTheGame = 4
