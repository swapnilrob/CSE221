def king_moves(n):
    x, y = map(int, input().split())

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    valid_positions = []

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 1 <= nx <= n and 1 <= ny <= n:
            valid_positions.append((nx, ny))

    valid_positions.sort()

    print(len(valid_positions))
    for px, py in valid_positions:
        print(px, py)


n = int(input())
king_moves(n)
