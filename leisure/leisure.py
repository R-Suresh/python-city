from museum import draw_museum
from restaurant import draw_restaurant
from stadium import draw_stadium_parking


def draw_leisure():
    draw_museum()
    draw_restaurant()
    draw_stadium_parking(5, 50, 8)
    return


draw_leisure()
