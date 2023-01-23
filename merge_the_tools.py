def merge_the_tools(string, k):
    t = []
    for i in range(len(string)//k):
        t.append(string[0+(k*i):k+(k*i)])
    u = [list(set(substring)) for substring in t]
    print('\n'.join([''.join(ustr) for ustr in u]))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)