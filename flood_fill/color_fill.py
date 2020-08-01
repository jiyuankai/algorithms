image = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 0],
    [1, 1, 0, 1],
]
origin_color = 1
new_color = 2


def flood_fill(image, x, y, origin_color, new_color):
    if x < 0 or y < 0 or x >= len(image) or y >= len(image[0]):
        return
    if image[x][y] != origin_color:
        return
    if image[x][y] == -1:
        return

    image[x][y] = -1
    flood_fill(image, x, y + 1, origin_color, new_color)
    flood_fill(image, x, y - 1, origin_color, new_color)
    flood_fill(image, x - 1, y, origin_color, new_color)
    flood_fill(image, x + 1, y, origin_color, new_color)
    image[x][y] = new_color


if __name__ == "__main__":
    flood_fill(image, 1, 1, origin_color, new_color)
    print(image)