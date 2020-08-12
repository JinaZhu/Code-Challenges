
# count hedges surrounding current location
# takes in garden matrix and i and j as the location of the current position


def count_populated_neighbors(garden, i, j):
    populated_neighbors = 0
    for delta_i in (-1, 0, 1):
        for delta_j in (-1, 0, 1):
            # skip over the current position
            if delta_i == 0 and delta_j == 0:
                continue
            neighbor_i = i + delta_i
            neighbor_j = j + delta_j
            # check for position that is out of bound
            if 0 <= neighbor_i < len(garden) and 0 <= neighbor_j < len(garden[0]):
                # add adjacent if it exist
                if garden[neighbor_i][neighbor_j] == 1:
                    populated_neighbors += 1
    return populated_neighbors
