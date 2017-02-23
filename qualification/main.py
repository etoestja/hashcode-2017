import sys

V = 0
E = 0
R = 0
C = 0
X = 0
S = []

Requests = []
Latencies = [[]]

def get_arr(inp):
    return([int(k) for k in inp.readline().split()])

def read_file(filename):
    inp = open(filename, 'r')
    global V, E, R, C, X, S
    [V, E, R, C, X] = get_arr(inp)
    S = get_arr(inp)
    for e in range(E):
        print("reading {}".format(e))
        [Ld, K] = get_arr(inp)
        print(Ld, K)
        for c in range(K):
            print("reading _{}".format(c))
            [c, Lc] = get_arr(inp)
            Lc = Ld - Lc
            print("{}, {}".format(c, Lc))

    global Requests
    for r in range(R):
        [Rv, Re, Rn] = get_arr(inp)
        Requests.append([Rv, Re, Rn, 0])
        print(Rv, Re, Rn)

def main():
    if len(sys.argv) < 3:
        sys.exit('Usage: %s input.in output.out'.format(sys.argv[0]))
    

    read_file(sys.argv[1])
    print(V,E,R,C,X)
    print(S)
    out = open(sys.argv[2], 'w')

if __name__ == '__main__':
    main()
