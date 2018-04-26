import abc

class AbstractGameFactory(object):
    #__metaclass__ = abc.ABCMeta

    #@abc.abstractmethod
    def getGame(self, gameName):
        pass


