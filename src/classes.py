import random
import numpy as np

class Schelling:

    def __init__(self, size, empty_ratio, similarity_threshold, n_neighbors):
        self.size = size
        self.empty_ratio = empty_ratio
        self.similarity_threshold = similarity_threshold
        self.n_neighbors = n_neighbors

        p = [(1-empty_ratio)/2, (1-empty_ratio)/2, empty_ratio]
        city_size = int(np.sqrt(self.size))**2
        self.city = np.random.choice([-1, 1, 0], size=city_size, p=p)
        self.city = np.reshape(self.city, (int(np.sqrt(city_size)), int(np.sqrt(city_size))))

    def run(self):
        for (row, col), value in np.ndenumerate(self.city):
            race = self.city[row, col]
            if race != 0:
                neighborhood = self.city[row-self.n_neighbors:row+self.n_neighbors, col-self.n_neighbors:col+self.n_neighbors]
                neighborhood_size = np.size(neighborhood)
                n_empty_houses = len(np.where(neighborhood == 0)[0])
                if neighborhood_size != n_empty_houses + 1:
                    n_similar = len(np.where(neighborhood == race)[0]) - 1
                    similarity_ratio = n_similar / (neighborhood_size - n_empty_houses - 1.)
                    is_unhappy = (similarity_ratio < self.similarity_threshold)
                    if is_unhappy:
                        empty_houses = list(zip(np.where(self.city == 0)[0], np.where(self.city == 0)[1]))
                        random_house = random.choice(empty_houses)
                        self.city[random_house] = race
                        self.city[row, col] = 0

    def get_mean_similarity_ratio(self):
        count = 0
        similarity_ratio = 0
        for (row, col), value in np.ndenumerate(self.city):
            race = self.city[row, col]
            if race != 0:
                neighborhood = self.city[row-self.n_neighbors:row+self.n_neighbors, col-self.n_neighbors:col+self.n_neighbors]
                neighborhood_size = np.size(neighborhood)
                n_empty_houses = len(np.where(neighborhood == 0)[0])
                if neighborhood_size != n_empty_houses + 1:
                    n_similar = len(np.where(neighborhood == race)[0]) - 1
                    similarity_ratio += n_similar / (neighborhood_size - n_empty_houses - 1.)
                    count += 1
        return similarity_ratio / count