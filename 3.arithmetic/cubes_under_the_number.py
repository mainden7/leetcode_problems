def main(number: int):
    # a ** 3 + b ** 3 = c ** 3 + d ** 3
    row = [i ** 3 for i in range(number)]
    dd = {}
    for i in row:
        for j in row[i + 1 :]:
            dd.setdefault(i + j, []).extend([i, j])
    print(dd)
    print({k: v for (k, v) in dd.items() if len(v) == 4})


if __name__ == "__main__":
    main(1000)
