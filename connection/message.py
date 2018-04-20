

class message:
    def __init__(self, tittle, data):
        self._tittle = tittle
        self._data = data


    def getTittle(self):
        return self._tittle

    def getData(self):
        return self._data

    def setTittle(self, tittle):
        self._tittle = tittle

    def setData(self, data):
        self._data = data

