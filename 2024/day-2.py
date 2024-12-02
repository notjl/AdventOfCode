import sys

if __name__ == "__main__":
    args = sys.argv[1]
    codes_list: list[list[int]] = [
        [int(x) for x in line.split()] for line in args.splitlines()
    ]
    safe = 0

    for codes in codes_list:
        unsafe_flag = False
        trend = None

        for i in range(len(codes)):
            if i == len(codes) - 1:
                break

            diff = codes[i] - codes[i + 1]
            if diff > 0:
                if trend == "dec":
                    unsafe_flag = True
                    break
                trend = "inc"
            elif diff < 0:
                if trend == "inc":
                    unsafe_flag = True
                    break
                trend = "dec"

            if abs(diff) not in range(1, 4):
                unsafe_flag = True
                break
        if not unsafe_flag:
            safe += 1

    print(safe)
