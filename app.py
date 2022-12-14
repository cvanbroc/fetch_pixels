# app.py

from flask import Flask, request
import numpy as np

app = Flask(__name__)

@app.post("/coordinates")
def get_coordinates():
    if request.is_json:
        json = request.get_json()

        # assume user input of corner points and dimensions are correct (four corners, not null, etc), could make function to check inputs later
        corner_points = json["corner_points"]
        dimensions = json["dimensions"]

        solution = pixels(corner_points, dimensions)
        formatted_solution = pretty_print(solution)

        # add in tab and newline spacing for better visual display to user and to make the end result look the same as in document
        user_display_solution = str(formatted_solution).replace(']],', ']],\n\t').replace('[[[', '[\n\t [[').replace(']]]', ']]\n]\n')
            
        return user_display_solution
    
    return {"error": "Request is not JSON"}, 415

# helper function for formatting a numpy array to string and rounding
# this makes for cleaner results checking readability in test.py by compressing array into one line
def pretty_print(solution: list) -> list:

    # converts array to string for stripping out newlines, inserts commas between values
    # lambda function pads integers with one decimal place (e.g. 3. -> 3.0) and trims decimals to two decimal places (e.g. 2.732 -> 2.73)
    # if more digits need to be displayed in output '.2f' can be increased (e.g. '.3f') but some tests would need to be redone as they currently check on two digits
    string_array = np.array2string(solution, separator = ', ', formatter={'float_kind': lambda x: format(x, '.1f') if x.is_integer() else format(x, '.2f')})

    # remove newlines so solution can be displayed on one line for easy test checking
    formatted_array = str(string_array).replace('\n', '')

    return formatted_array

# algorithm to make NxMx2 array from corner points and dimensions
def pixels(corner_points: list, dimensions: tuple) -> list:
    corner_points_x = []
    corner_points_y = []

    # store x and y coordinates of corner points
    for coordinate in corner_points:
        corner_points_x.append(coordinate[0])
        corner_points_y.append(coordinate[1])

    #dimensions[1] is the number of columns which corresponds to spacing needed between x-axis values
    axis_spacing_x = dimensions[1]
    # dimensions[0] is the number for rows which corresponds to spacing needed between y-axis values
    axis_spacing_y = dimensions[0]

    # find all values on the x and y-axis for coordinates by starting at the minimum value and spacing evenly to the maximum value
    coordinates_x = np.linspace(min(corner_points_x), max(corner_points_x), num = axis_spacing_x)
    coordinates_y = np.linspace(min(corner_points_y), max(corner_points_y), num = axis_spacing_y)

    # create a grid of those values, reverse the y coordinates to get the correct order of display
    grid = np.meshgrid(coordinates_x, np.flip(coordinates_y))

    # stack the grid coordinates to create the final array
    coordinates = np.dstack(grid)

    return coordinates

