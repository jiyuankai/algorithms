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


directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]

# BFS
class Solution:

    def floodFill(self, image, sr, sc, newColor):
        if not image:
            return
        origin_color = image[sr][sc]
        queue = [(sr, sc)]
        while queue:
            r, c = queue.pop(0)
            if image[r][c] != origin_color:
                continue
            if image[r][c] == newColor:
                continue
            image[r][c] = newColor
            for direction in directions:
                x, y = direction
                if 0 <= r + x < len(image) and 0 <= c + y < len(image[0]):
                    queue.append((r + x, c + y))
        return image

# DFS
class Solution:

    def floodFill(self, image, sr, sc, newColor):
        if not image:
            return
        return self.dfs(image, sr, sc, newColor, image[sr][sc])

    def dfs(self, image, sr, sc, newColor, oriColor):
        if image[sr][sc] != oriColor or image[sr][sc] == newColor:
            return image
        image[sr][sc] = newColor

        for direction in directions:
            x, y = direction
            if 0 <= sr + x < len(image) and 0 <= sc + y < len(image[0]):
                self.dfs(image, sr + x, sc + y, newColor, oriColor)
        return image



if __name__ == "__main__":
    flood_fill(image, 1, 1, origin_color, new_color)
    print(image)