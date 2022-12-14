from app import pixels, pretty_print

# test a rectangle in cartesian quadrant I
def test_quadrant1_and_array_access():
     corner_points = [
             (1, 1),
             (3, 1),
             (1, 3),
             (3, 3)]
     dimensions = (3, 3)

     solution = pixels(corner_points, dimensions)

     assert solution[0,0,0] == 1
     assert solution[0,0,1] == 3
     assert solution[1,2,0] == 3
     assert solution[1,2,1] == 2
     assert solution[2,2,0] == 3
     assert solution[2,2,1] == 1

     assert pretty_print(solution) == '[[[1.0, 3.0],  [2.0, 3.0],  [3.0, 3.0]], [[1.0, 2.0],  [2.0, 2.0],  [3.0, 2.0]], [[1.0, 1.0],  [2.0, 1.0],  [3.0, 1.0]]]'

# test a large number of dimensions so we get fractional output in array and can verify values are rounded correctly
def test_fractions():
     corner_points = [
             (1.5, 1.5),
             (4.0, 1.5),
             (1.5, 8.0),
             (4.0, 8.0)]
     dimensions = (10, 12)

     solution = pixels(corner_points, dimensions)
     
     assert solution[0,0,0] == 1.5
     assert solution[0,0,1] == 8

     # check each row (e.g. solution[x] instead of solution) in the matrix individually as otherwise this would be a very long line
     assert pretty_print(solution[0]) == '[[1.50, 8.0], [1.73, 8.0], [1.95, 8.0], [2.18, 8.0], [2.41, 8.0], [2.64, 8.0], [2.86, 8.0], [3.09, 8.0], [3.32, 8.0], [3.55, 8.0], [3.77, 8.0], [4.0, 8.0]]'
     assert pretty_print(solution[1]) == '[[1.50, 7.28], [1.73, 7.28], [1.95, 7.28], [2.18, 7.28], [2.41, 7.28], [2.64, 7.28], [2.86, 7.28], [3.09, 7.28], [3.32, 7.28], [3.55, 7.28], [3.77, 7.28], [4.0, 7.28]]'
     assert pretty_print(solution[2]) == '[[1.50, 6.56], [1.73, 6.56], [1.95, 6.56], [2.18, 6.56], [2.41, 6.56], [2.64, 6.56], [2.86, 6.56], [3.09, 6.56], [3.32, 6.56], [3.55, 6.56], [3.77, 6.56], [4.0, 6.56]]'
     assert pretty_print(solution[3]) == '[[1.50, 5.83], [1.73, 5.83], [1.95, 5.83], [2.18, 5.83], [2.41, 5.83], [2.64, 5.83], [2.86, 5.83], [3.09, 5.83], [3.32, 5.83], [3.55, 5.83], [3.77, 5.83], [4.0, 5.83]]'
     assert pretty_print(solution[4]) == '[[1.50, 5.11], [1.73, 5.11], [1.95, 5.11], [2.18, 5.11], [2.41, 5.11], [2.64, 5.11], [2.86, 5.11], [3.09, 5.11], [3.32, 5.11], [3.55, 5.11], [3.77, 5.11], [4.0, 5.11]]'
     assert pretty_print(solution[5]) == '[[1.50, 4.39], [1.73, 4.39], [1.95, 4.39], [2.18, 4.39], [2.41, 4.39], [2.64, 4.39], [2.86, 4.39], [3.09, 4.39], [3.32, 4.39], [3.55, 4.39], [3.77, 4.39], [4.0, 4.39]]'
     assert pretty_print(solution[6]) == '[[1.50, 3.67], [1.73, 3.67], [1.95, 3.67], [2.18, 3.67], [2.41, 3.67], [2.64, 3.67], [2.86, 3.67], [3.09, 3.67], [3.32, 3.67], [3.55, 3.67], [3.77, 3.67], [4.0, 3.67]]'
     assert pretty_print(solution[7]) == '[[1.50, 2.94], [1.73, 2.94], [1.95, 2.94], [2.18, 2.94], [2.41, 2.94], [2.64, 2.94], [2.86, 2.94], [3.09, 2.94], [3.32, 2.94], [3.55, 2.94], [3.77, 2.94], [4.0, 2.94]]'
     assert pretty_print(solution[8]) == '[[1.50, 2.22], [1.73, 2.22], [1.95, 2.22], [2.18, 2.22], [2.41, 2.22], [2.64, 2.22], [2.86, 2.22], [3.09, 2.22], [3.32, 2.22], [3.55, 2.22], [3.77, 2.22], [4.0, 2.22]]'
     assert pretty_print(solution[9]) == '[[1.50, 1.50], [1.73, 1.50], [1.95, 1.50], [2.18, 1.50], [2.41, 1.50], [2.64, 1.50], [2.86, 1.50], [3.09, 1.50], [3.32, 1.50], [3.55, 1.50], [3.77, 1.50], [4.0, 1.50]]'

# test a rectangle in cartesian quadrant II
def test_quadrant2():
     corner_points = [
             (-1, 1),
             (-3, 1),
             (-1, 3),
             (-3, 3)]
     dimensions = (3, 3)

     solution = pixels(corner_points, dimensions)

     assert pretty_print(solution) == '[[[-3.0, 3.0],  [-2.0, 3.0],  [-1.0, 3.0]], [[-3.0, 2.0],  [-2.0, 2.0],  [-1.0, 2.0]], [[-3.0, 1.0],  [-2.0, 1.0],  [-1.0, 1.0]]]'

# test a rectangle in cartesian quadrant III
def test_quadrant3():
     corner_points = [
             (-1, -1),
             (-3, -1),
             (-1, -3),
             (-3, -3)]
     dimensions = (3, 3)

     solution = pixels(corner_points, dimensions)

     assert pretty_print(solution) == '[[[-3.0, -1.0],  [-2.0, -1.0],  [-1.0, -1.0]], [[-3.0, -2.0],  [-2.0, -2.0],  [-1.0, -2.0]], [[-3.0, -3.0],  [-2.0, -3.0],  [-1.0, -3.0]]]'

# test a rectangle in cartesian quadrant IV
def test_quadrant4():
     corner_points = [
             (1, -1),
             (3, -1),
             (1, -3),
             (3, -3)]
     dimensions = (3, 3)

     solution = pixels(corner_points, dimensions)

     assert pretty_print(solution) == '[[[1.0, -1.0],  [2.0, -1.0],  [3.0, -1.0]], [[1.0, -2.0],  [2.0, -2.0],  [3.0, -2.0]], [[1.0, -3.0],  [2.0, -3.0],  [3.0, -3.0]]]'

# test a rectanble overlapped among quadrants I - IV
def test_quadrant_overlap():
     corner_points = [
             (-1, -1),
             (-1, 3),
             (1, -1),
             (1, 3)]
     dimensions = (3, 3)

     solution = pixels(corner_points, dimensions)

     assert pretty_print(solution) == '[[[-1.0, 3.0],  [0.0, 3.0],  [1.0, 3.0]], [[-1.0, 1.0],  [0.0, 1.0],  [1.0, 1.0]], [[-1.0, -1.0],  [0.0, -1.0],  [1.0, -1.0]]]'

