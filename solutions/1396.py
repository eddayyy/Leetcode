from collections import defaultdict

class Passenger:
    def __init__(self, startingStation=None, startTime=None):
        self.startingStation = startingStation
        self.startTime = startTime
        self.endingStation = None
        self.endTime = 0
    
    def checkOut(self, station, time):
        self.endingStation = station
        self.endTime = time - self.startTime

class UndergroundSystem:

    def __init__(self):
        self.manifest = {}
        # Instead of a list of times, we store tuples of (totalTime, totalTrips)
        self.trips = defaultdict(lambda: (0, 0)) 

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.manifest[id] = Passenger(startingStation=stationName, startTime=t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        passenger = self.manifest.pop(id)
        passenger.checkOut(stationName, t)
        tripKey = (passenger.startingStation, passenger.endingStation)
        
        # Update the running total and count for the station pair
        totalTime, totalTrips = self.trips[tripKey]
        self.trips[tripKey] = (totalTime + passenger.endTime, totalTrips + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, totalTrips = self.trips[(startStation, endStation)]
        return totalTime / totalTrips if totalTrips > 0 else 0

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
