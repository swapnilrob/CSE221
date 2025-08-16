def knight_attacks_knight(n, m, k):
    knights = []
    for _ in range(k):
        x, y = map(int, input().split())
        knights.append((x - 1, y - 1)) 

    knight_set = set(knights)  

    knight_moves = [
        (-2, -1), (-1, -2), (-2, 1), (-1, 2),
        (1, -2), (2, -1), (1, 2), (2, 1)
    ]

    for x, y in knights:
        for dx, dy in knight_moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if (nx, ny) in knight_set:
                    return "YES"
    return "NO"

n, m, k = map(int, input().split())
print(knight_attacks_knight(n, m, k))
