import sys

if __name__ == "__main__":
    args = sys.argv[1]
    left_list: list[int] = []
    right_list: list[int] = []
    distance_list: list[int] = []

    for line in args.splitlines():
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

    left_list.sort()
    right_list.sort()

    for left, right in zip(left_list, right_list):
        distance_list.append(abs(left - right))

    print(sum(distance_list))
