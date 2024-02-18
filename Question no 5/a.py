import random
import numpy as np

class AntColony:
    def __init__(self, distanceMatrix, numAnts, evaporationRate, alpha, beta):
        self.distanceMatrix = distanceMatrix
        self.numAnts = numAnts
        self.evaporationRate = evaporationRate
        self.alpha = alpha
        self.beta = beta
        self.numCities = len(distanceMatrix)
        self.pheromoneMatrix = np.ones((self.numCities, self.numCities)) / self.numCities
        self.probabilities = np.zeros((self.numCities, self.numCities))
        self.bestTour = []
        self.bestTourLength = float('inf')
    
    def initializePheromones(self):
        self.pheromoneMatrix = np.ones((self.numCities, self.numCities)) / self.numCities
    
    def solve(self, maxIterations):
        self.bestTourLength = float('inf')
        self.bestTour = []
        for iteration in range(maxIterations):
            for ant in range(self.numAnts):
                visited = [False] * self.numCities
                tour = [0] * self.numCities
                currentCity = random.randint(0, self.numCities-1)
                tour[0] = currentCity
                visited[currentCity] = True
                for i in range(1, self.numCities):
                    self.calculateProbabilities(currentCity, visited)
                    nextCity = self.selectNextCity(currentCity)
                    tour[i] = nextCity
                    visited[nextCity] = True
                    currentCity = nextCity
                tourLength = self.calculateTourLength(tour)
                if tourLength < self.bestTourLength:
                    self.bestTourLength = tourLength
                    self.bestTour = tour
            self.updatePheromones()
    
    def calculateProbabilities(self, city, visited):
        total = 0.0
        for i in range(self.numCities):
            if not visited[i]:
                self.probabilities[city][i] = (self.pheromoneMatrix[city][i] ** self.alpha) * (1.0 / self.distanceMatrix[city][i] ** self.beta)
                total += self.probabilities[city][i]
            else:
                self.probabilities[city][i] = 0.0
        self.probabilities[city] /= total
    
    def selectNextCity(self, city):
        probabilities = self.probabilities[city]
        r = random.random()
        cumulativeProbability = 0.0
        for i in range(self.numCities):
            cumulativeProbability += probabilities[i]
            if r <= cumulativeProbability:
                return i
        return -1
    
    def updatePheromones(self):
        self.pheromoneMatrix *= (1.0 - self.evaporationRate)
        for ant in range(self.numAnts):
            for i in range(self.numCities - 1):
                city1 = self.bestTour[i]
                city2 = self.bestTour[i + 1]
                self.pheromoneMatrix[city1][city2] += (1.0 / self.bestTourLength)
                self.pheromoneMatrix[city2][city1] += (1.0 / self.bestTourLength)
    
    def calculateTourLength(self, tour):
        length = 0
        for i in range(len(tour) - 1):
            length += self.distanceMatrix[tour[i]][tour[i + 1]]
        length += self.distanceMatrix[tour[-1]][tour[0]]
        return length
    
    def getBestTourLength(self):
        return self.bestTourLength
    
    def getBestTour(self):
        return self.bestTour

distanceMatrix = np.array([
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
])
numAnts = 5
evaporationRate = 0.5
alpha = 1.0
beta = 2.0

colony = AntColony(distanceMatrix, numAnts, evaporationRate, alpha, beta)
colony.solve(1000)

bestTour = colony.getBestTour()
bestTourLength = colony.getBestTourLength()

print("Best tour:", bestTour)
print("Best tour length:", bestTourLength)


