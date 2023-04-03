
# Count the number of rectangles formed by a list of points

    The approach I took for this problem is the following:
    I take every pair of 2 points possible and add it to a hashmap, in order to count the number of edges that have tha same length and the same end points y coordinates.
    For each of those edges the number of rectangles that can be formed is n taken 2, where n is the number of edges with the same end points y coordinates

