def hanoi(n, source, target, auxialiary):
    if n > 0:
        hanoi(n - 1, source, auxialiary, target)
        print(f"Se movio el disco {n} desde {source} a {target}")
        hanoi(n - 1, auxialiary, target, source)


hanoi(7, "A", "B", "C")
