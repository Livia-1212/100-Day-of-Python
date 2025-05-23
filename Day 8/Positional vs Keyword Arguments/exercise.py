def calculate_love_score(name1, name2):
    names = (name1 + name2).upper()
    T = R = U = E = L = O = V = 0

    for c in names:
        if c in "TRUE":
            if c == 'T':
                T += 1
            elif c == 'R':
                R += 1
            elif c == 'U':
                U += 1
            elif c == 'E':
                E += 1
            else:
                continue
    Total_True = T + R + U + E

    print(f"Total_True = {Total_True}")

    E = 0

    for c in names:
        if c in "LOVE":
            if c == 'L':
                L += 1
            elif c == 'O':
                O += 1
            elif c == 'V':
                V += 1
            elif c == 'E':
                E += 1
            else:
                continue
    Love_Count = L + O + V + E
    print(f"Love_Count = {Love_Count}")

    print(f"Love Score = {Total_True}{Love_Count}")

calculate_love_score("Angela Yu", "Jack Bauer")
calculate_love_score("Kanye West", "Kim Kardashian")
