n, m, i_start, j_start, q = [int(x) for x in input().split()]

graph = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
visited = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
length = [[] for _ in range(max(n, m)**2 + 1)]

for _ in range(q):
    y, x = [int(m) for m in input().split()]
    graph[y][x] = 1

offsets = [(2, 1), (2, -1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]
length[0].append((i_start, j_start))
visited[i_start][j_start] = 1

now_len = 1

for len_item in length:
    for item in len_item:
        # print(len_item, item)
        for offset in offsets:
            new_coords = (item[0] + offset[0], item[1] + offset[1])
            try:
                if graph[new_coords[0]][new_coords[1]] and new_coords[0] > 0 and new_coords[1] > 0:
                    if not visited[new_coords[0]][new_coords[1]]:
                        visited[new_coords[0]][new_coords[1]] = 1
                        length[now_len].append(new_coords)
            except IndexError:
                continue
    now_len += 1
final_sum = 0
ans2 = []
# if is_ans:
for i in range(7):
    for j in range(len(length[i])):
        # print(i, length[i])
        graph[length[i][j][0]][length[i][j][1]] = i
        final_sum += i * len(length[i])
[print(i[1:]) for i in graph[1:]]