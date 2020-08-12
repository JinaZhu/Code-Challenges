
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

# produce the matrix garden of the cycle(year)


def simulate_one_year_growth(garden):
    # create new garden template
    # first loop is creating items in each rows and producing the number of rows
    new_garden = [[0 for j in range(len(garden[0]))]
                  for i in range(len(garden))]
    for i in range(len(garden)):
        for j in range(len(garden[0])):
            # get back status of neighbors
            populated_neighbors = count_populated_neighbors(garden, i, j)
            # if current location is hedge(1) and all neighbors(8) are hedges, the hedge dies(0)
            if garden[i][j] == 1 and populated_neighbors == 8:
                new_garden[i][j] = 0
            # if location is empty(0) and at least 1 neighbor is a hedge, location is now a hedge(1)
            elif garden[i][j] == 0 and populated_neighbors > 0:
                new_garden[i][j] = 1
            # any other case, location stays the same
            else:
                new_garden[i][j] = garden[i][j]
    return new_garden

# count adjacent pairings


def count_adjacent_pairs(garden):
    adjacent_pairs = 0
    for i in range(len(garden)):
        for j in range(len(garden[0])):
            if garden[i][j] == 1:
                adjacent_pairs += count_populated_neighbors(garden, i, j)
    # each pair counted twice
    return adjacent_pairs // 2

# simulate the garden for x numbers of years and return the number of adjacent pairs after the last year


def neighbors_after_years(garden, years):
    # simulate years number of times and update garden each year
    for year in range(years):
        garden = simulate_one_year_growth(garden)
    # count adjacent pairs in the end
    return count_adjacent_pairs(garden)


garden = [[1, 0, 0, 0], [1, 1, 0, 0], [1, 0, 0, 1]]
garden2 = [[0, 0, 1], [0, 0, 0]]

print(neighbors_after_years(garden, 2))
# >> 21
print(neighbors_after_years(garden2, 1))
# >> 6
