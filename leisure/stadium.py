def draw_stadium_parking(stadium_height, stadium_width, length):
    draw_stadium(stadium_height, stadium_width)
    draw_parkinglot(length)


def draw_stadium(stadium_height=5, stadium_width=50):
    """
    Prints a stadium of given parameters:

    args:
        stadium_height: Height of the rectangular stadium
        stadium_width : Width of the rectangular stadium
    """

    draw_width = " "
    draw_height = ""

    for i in range(stadium_width):
        draw_width += "-"

    draw_width += "\n"

    for i in range(stadium_height):
        draw_height += "|"
        for j in range(stadium_width + 1):
            draw_height += " "

        draw_height += "|\n"

    stadium = draw_width + draw_height + draw_width

    print()
    print(stadium)
    print()


def print_a_cell():
    print("[ ]", end="")


def draw_parkinglot(length=5):
    """
    Prints a road of a given lenth:

    args:
        length: integer define the length of the parking lot.
    """

    # sanitizing parameters
    if length < 0:
        raise ValueError("length is negative")
    if length == 0:
        return

    # Drawing Cells
    for i in range(length):
        for j in range(length):
            print_a_cell()
        print("")