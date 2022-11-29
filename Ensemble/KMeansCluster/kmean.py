import random
import numpy as np
class KMeans:
    def __init__(self, n_clusters=2, max_iter=100):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.centroids = None

    def fit_predict(self, X):
        # print(X)
        random_index = random.sample(range(0, X.shape[0]), self.n_clusters)
        self.centroids = X[random_index]
        # print(self.centroids)

        for i in range(self.max_iter):
            # assign cluster
            cluster_group = self.assign_cluster(X)
            # move centroids
            # check finish

    def assign_cluster(self, X):
        cluster_group = []
        distances = []

        for row in X:
            for centroid in self.centroids:
                distances.append(np.sqrt(np.dot(row-centroid, row-centroid)))
            #print(distances)
            min_distance = min(distances)
            index_position = distances.index(min_distance)
            #print(index_position)
            cluster_group.append(index_position)

            distances.clear()
        return np.array(cluster_group)     
