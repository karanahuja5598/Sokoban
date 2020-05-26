def isValid(room,currLocation, human, box):
    if currLocation == human:
        return True
    rowCount = len(room)
    colCount = len(room[0])
    queue = [human]
    visited = [human]

    while len(queue) != 0:
        i, j = queue.pop()
        if (i, j) == currLocation:
            return True
        neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for x, y in neighbors:
            if x >= 0 and x < rowCount and y >= 0 and y < colCount:
                if (x, y) != box and room[x][y] != 1 and (x, y) not in visited:
                    queue.append((x, y))
                    visited.append((x, y))
    return False
# Do not rename this function, otherwise, the automated checks will fail.
def solve_sokoban(room):
    """
    :param room: 2-dimensional array filled with values ranging from 0 to and including 4 where
        0 = empty, 1 = obstacle, 2 = human, 3 = box, 4 = destination
    :return: YES or NO depending on whether there is a sequence of moves that terminate
    with the box at the destination
    """
    # Write your code in this method.
    
    human = None
    box = None
    destination = None
    
    rowCount = len(room)
    if rowCount == 0:
        return "NO"
    colCount = len(room[0])
    if colCount == 0:
        return "NO"
    
    for i in range(rowCount):
        for j in range(colCount):
            if room[i][j] == 2:
                human = (i,j)
            if room[i][j] == 4:
                destination = (i,j)
            if room[i][j] == 3:
                box = (i,j)
            if human != None and destination != None and box != None:
                break
        if human != None and destination != None and box != None:
            break
    
    queue = [(box,destination,human,0)]
    visited = set([(box,human)])
    
    while len(queue) > 0:
        box, target, human, dist = queue.pop()
        if target == box:
            return "YES"
        i, j = box
        if i > 0 and i < (rowCount-1) and room[i-1][j] != 1 and room[i+1][j] != 1:
                if ((i+1, j), (i, j)) not in visited:
                    if isValid(room, (i-1, j), human, box):
                        queue.insert(0, ((i+1, j), target, (i, j), dist + 1))
                        visited.add(((i+1, j), (i, j)))
                if ((i-1, j), (i, j)) not in visited:
                    if isValid(room, (i+1, j), human, box):
                        queue.insert(0, ((i-1, j), target, (i, j), dist + 1))
                        visited.add(((i-1, j), (i, j)))

        if j > 0 and j < (colCount-1) and room[i][j-1] != 1 and room[i][j+1] != 1:
                if ((i, j-1), (i, j)) not in visited:
                    if isValid(room, (i, j+1), human, box):
                        queue.insert(0, ((i, j-1), target, (i, j), dist + 1))
                        visited.add(((i, j-1), (i, j)))
                if ((i, j+1), (i, j)) not in visited:
                    if isValid(room, (i, j-1), human, box):
                        queue.insert(0, ((i, j+1), target, (i, j), dist + 1))
                        visited.add(((i, j+1), (i, j)))
    return "NO"


# Feel free to modify main function
def main():
    # Example 1, expecting NO:
    test_1 = [[4, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 0],
              [0, 0, 0, 2, 0, 0],
              [0, 0, 0, 3, 0, 0],
              [0, 0, 0, 0, 0, 0]]

    assert solve_sokoban(test_1) == "NO", "Test 1 failed."
    # Example 2, expecting YES:
    test_2 = [[4, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 0, 0],
              [0, 0, 0, 2, 0, 0],
              [0, 0, 0, 3, 0, 0],
              [0, 0, 0, 0, 0, 0]]

    assert solve_sokoban(test_2) == "YES", "Test 2 failed."
    
    test_3 = [[0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 3, 0],
              [0, 0, 4, 0, 2, 0],
              [1, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]]

    assert solve_sokoban(test_3) == "YES", "Test 3 failed."
    
    test_4 = [[4, 2, 0, 0, 1],
              [1, 0, 3, 0, 1],
              [1, 0, 0, 1, 1]]

    assert solve_sokoban(test_4) == "YES", "Test 4 failed."
    
    test_5 = [[0, 0, 0, 0, 0, 0],
              [1, 0, 0, 0, 0, 0],
              [0, 0, 1, 1, 2, 3],
              [4, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]]
    assert solve_sokoban(test_5) == "NO", "Test 5 failed."
    
    test_6 = [[4,3,0],
              [1,2,1]]

    assert solve_sokoban(test_6) == "NO", "Test 6 failed."
    
    test_7 = [[1, 1, 0, 0, 0, 4],
              [1, 0, 3, 0, 1, 2],
              [0, 0, 0, 0, 1, 1],
              [0, 0, 0, 0, 1, 0],
              [0, 0, 1, 0, 0, 0]]
              
    assert solve_sokoban(test_7) == "YES", "Test 7 failed."
    
if __name__ == "__main__":
    main()
