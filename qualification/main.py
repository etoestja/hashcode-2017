import sys
import heapq

V = 0
E = 0
R = 0
C = 0
X = 0

# sizes of videos
S = []

# Cached videos endpoints (endpoint e, video e) => which last cache server?
CVE = {}

# latencies for BestCache list (endpt i)
Latencies = []

# which videos on server i?
CachedVideos = {}

# heap of requests
RH = []

# best by Ld-Lc server for endpoint i
BestCache = []

def goodness(v, e, n):
    return(0)

def get_arr(inp):
    return([int(k) for k in inp.readline().split()])

def read_file(filename):
    inp = open(filename, 'r')
    global V, E, R, C, X, S
    [V, E, R, C, X] = get_arr(inp)
    global CachedVideos
    for c in range(C):
        CachedVideos[c] = []

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
        print(Rv, Re, Rn)



def processQ():
    req = heapq.heappop(RH)

    v = req[2]
    e = req[3]
    n = req[4]

    if (e, v) in CVE.keys():
        if CVE[(e, v)] == GetBC(e, S[v]):
            return
        else:
            heapq.heappush(RH, (goodness(v, e, n), req[1], v, e, n))


def main():
    if len(sys.argv) < 3:
        sys.exit('Usage: %s input.in output.out'.format(sys.argv[0]))
    

    read_file(sys.argv[1])
    print(V,E,R,C,X)
    print(S)
    out = open(sys.argv[2], 'w')

if __name__ == '__main__':
    main()
