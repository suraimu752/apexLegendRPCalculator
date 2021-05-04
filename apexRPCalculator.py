l_p = [0, 100, 60, 40, 40, 30, 30, 20, 20, 10, 10,  5,  5,  5,  0]
l_k = [0,  25, 20, 20, 15, 15, 12, 12, 12, 12, 12, 10, 10, 10, 10]

def placeKill2RP(place: int, kill: int):

    rp = l_p[place] + l_k[place] * kill
    return rp

def getLeast(need: int, cost: int):
    l = []
    b_k = 0
    for p in range(14, 0, -1):
        for k in range(0, 7):
            b_k = k
            rp = placeKill2RP(p, k) - cost
            if rp >= need:
                l.append([p, k, rp])
                break
        if b_k == 0:
            break
    if len(l) == 0:
        l = -1
    return l

if __name__ == "__main__":
    import sys
    args = sys.argv
    if len(args) != 3 or not args[1].isdigit() or not args[2].isdigit():
        print("引数が間違っています")
    else:
        l = getLeast(int(args[1]), int(args[2]))
        if l == -1:
            print("達成不可能")
        else:
            for e in l:
                print(f"Place: {e[0]}, Kill: {e[1]}, RP: {e[2]}")
