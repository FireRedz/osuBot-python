

# idk if i should use sqlite3 db or this
class storage:
    mapData = {}

    def insertData(self, dataName,data):
        self.mapData[dataName] = data

    def getData(self, dataName):
        return self.mapData[dataName]
