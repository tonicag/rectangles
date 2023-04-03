

def readPoints(in_file):
    points = []
    # the points are of the form (x,y) and each point is on a line
    for l in in_file:
        coords = l.split()
        x = int(coords[0])
        y = int(coords[1])
        points.append((x,y))
    return points

def countRectangles(points):
    result = 0
    edges = {} # hashmap used for storing the count of pairs of y-coordinates


    for pA in points: 
        (xA,yA) = pA
        for pB in points: # iterating to each pair of two points from the list
            (xB,yB) = pB
            if (xA==xB) and yB>yA: # checking if the points make a segment that is parallel to the y axes
                if (yA,yB) not in edges:
                    edges[(yA,yB)] = 0
                edges[(yA,yB)] = edges[(yA,yB)] + 1 # adding the pair of y-coordinates of the segment to the hashmap

    for e in edges: # for each segment dected the number of rectangles that can be created is n*(n-1)/2, which is the formula of n taken 2
        cnt = edges[e]
        result = result + int(cnt * (cnt - 1) / 2)

    #print(edges)
    return result 

def main():
    in_file = open("input.in","r")

    
    points = readPoints(in_file) # reading the input file and returning the list of points
    result = countRectangles(points) # function to calculate the number of rectangles, given a list of points
    print(f"The number of rectangles formed is {result}")






if __name__=='__main__':
    main()