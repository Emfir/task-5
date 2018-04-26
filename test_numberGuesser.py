from unittest import TestCase


class TestNumberGuesser(TestCase):
    def test_nextGuessCorrect(self):
        self.numberToGues = 0
        self.assertEqual(nextGuess(0), enums.resultsOfTheGuess.goodGuess)
        self.numberToGues = 50
        self.assertEqual(nextGuess(50), enums.resultsOfTheGuess.goodGuess)
        self.numberToGues = 100
        self.assertEqual(nextGuess(100), enums.resultsOfTheGuess.goodGuess)

    def test_nextGuessTooBig(self):
        self.numberToGues = 100
        self.assertEqual(nextGuess(101), enums.resultsOfTheGuess.tooBig)
        self.numberToGues = 49
        self.assertEqual(nextGuess(50), enums.resultsOfTheGuess.tooBig)
        self.numberToGues = 0
        self.assertEqual(nextGuess(1), enums.resultsOfTheGuess.tooBig)

    def test_nextGuessTooSmall(self):
        self.numberToGues = 100
        self.assertEqual(nextGuess(99), enums.resultsOfTheGuess.tooSmall)
        self.numberToGues = 49
        self.assertEqual(nextGuess(-5), enums.resultsOfTheGuess.tooSmall)
        self.numberToGues = 1
        self.assertEqual(nextGuess(0), enums.resultsOfTheGuess.tooSmall)


