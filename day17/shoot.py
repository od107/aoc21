def angle():
    # x_target = [20, 30]
    # y_target = [-10, -5]
    # target = [[20, -5], [30, -10]]
    # real target area: x=209..238, y=-86..-59
    x_target = [209, 238]
    y_target = [-86, -59]

    # the issue here is correctly limiting the search space
    # how do we choose a proper upper bound for y_vel?
    y_max = 10 * abs(y_target[0]-y_target[1])
    x_max = max(x_target) + 1
    y_min = y_target[0]

    count = 0

    for y_vel in reversed(range(y_min, y_max)):
        for x_vel in range(x_max):
            success, max_height = shoot(x_vel, y_vel, x_target, y_target)
            if success:
                count += 1
                # print(x_vel, y_vel)
                # return x_vel, y_vel, max_height
    # return "nothing found"
    return count


def shoot(x_vel, y_vel, x_target, y_target):
    x_pos, y_pos, max_height = 0, 0, 0
    while x_pos <= x_target[1] and y_pos >= y_target[0]:
        x_pos += x_vel
        y_pos += y_vel
        if y_pos > max_height:
            max_height = y_pos
        if x_vel > 0:
            x_vel -= 1
        elif x_vel < 0:
            x_vel += 1
        y_vel -= 1
        # print(x_pos, y_pos, x_vel, y_vel)
        if x_target[0] <= x_pos <= x_target[1] and y_target[0] <= y_pos <= y_target[1]:
            return True, max_height
    return False, max_height


def main():
    # print("the answer is ")
    print(angle())
    # print(shoot(6, 14, [20, 30], [-10, -5]))


if __name__ == "__main__":
    main()
