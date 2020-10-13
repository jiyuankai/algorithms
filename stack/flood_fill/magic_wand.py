import copy
import pprint

image = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
]

origin_color = 0
new_color = 4
visited = copy.deepcopy(image)


def flood_fill(image, x, y, origin_color, new_color):
    if x < 0 or y < 0 or x >= len(image) or y >= len(image[0]):
        return 0
    if visited[x][y] == -1:
        return 1
    if image[x][y] != origin_color:
        return 0
    visited[x][y] = -1

    surround = \
    flood_fill(image, x, y + 1, origin_color, new_color) +\
    flood_fill(image, x, y - 1, origin_color, new_color) +\
    flood_fill(image, x - 1, y, origin_color, new_color) +\
    flood_fill(image, x + 1, y, origin_color, new_color)
    if surround < 4:
        image[x][y] = new_color
    return 1


if __name__ == "__main__":
    flood_fill(image, 4, 4, origin_color, new_color)
    pprint.pprint(image)