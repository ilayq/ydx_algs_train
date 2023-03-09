k = int(input())
points = []
for i in range(k):
    points.append(list(map(int, input().split())))

# x_min = 1 << 300
# y_min = 1 << 300
# x_max = -1 << 3000
# y_max = -1 << 3444
points.sort(key=lambda x: x[0])
left_p = points[0]
right_p = points[-1]
points.sort(key=lambda x: x[1])
upper = points[-1]
down = points[0]
print(left_p[0], down[1], right_p[0], upper[1])
