import abc

class AbstractState(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def newTicTackToePlayer(self, factory, server, state):
        pass

    @abc.abstractmethod
    def newNumberGuesserPlayer(self, factory, sever  ):
        pass

