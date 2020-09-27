import sys

def main():
    reader = (line.rstrip() for line in sys.stdin)
    string = next(reader)
    pattern = next(reader)
    print(func("$".join([pattern, string])).count(len(pattern)))

def func(string):
    
    lenStr = len(string)
    
    res = [0 for i in range(lenStr)]
    left, right = 0, 0

    for i in range(1, lenStr):
        res[i] = max(0, min(right - i, res[i - left]))
        while (i + res[i] < lenStr and
               string[res[i]] == string[i + res[i]]):
            res[i] += 1

        if i + res[i] >= right:
            left = i
            right = i + res[i]

    return res

if __name__ == "__main__":
    main()