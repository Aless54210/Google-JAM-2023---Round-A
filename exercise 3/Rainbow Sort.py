def solve_case(colors):
    num_colors = len(colors)
    color_to_int = {}
    last_int = 0
    ints = []
    for i in range(num_colors):
        color = colors[i]
        if color not in color_to_int:
            last_int += 1
            color_to_int[color] = last_int
        ints.append(color_to_int[color])
    for i in range(1, num_colors):
        if ints[i] < ints[i - 1]:
            return "IMPOSSIBLE"
    return " ".join(str(color) for color in sorted(color_to_int, key=color_to_int.get))

num_cases = int(input())
for case in range(1, num_cases + 1):
    n = int(input())
    colors = list(map(int, input().split()))
    result = solve_case(colors)
    print("Case #{}: {}".format(case, result))