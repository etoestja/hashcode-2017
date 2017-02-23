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

# which videos on server i?
CachedVideos = {}

# heap of requests
RH = []

# best by Ld-Lc server for endpoint i
BestCache = []

def remaining_size(cs_index):
    s = 0
    global CachedVideos, X
    for v in CachedVideos[cs_index]:
        s += S[v]
    return(X - s)

def getBC(e, size):
    global BestCache
    for cc in BestCache[e]:
        if remaining_size(cc[0]) >= size:
            return(cc[0])
    return(-1)


def goodness(v, e, n):
    global S
    return(n * getBC(e, S[v]) / S[v])

def get_arr(inp):
    return([int(k) for k in inp.readline().split()])

def read_file(filename):
    inp = open(filename, 'r')

    global V, E, R, C, X
    [V, E, R, C, X] = get_arr(inp)

    global S
    S = get_arr(inp)

    global CachedVideos
    for c in range(C):
        CachedVideos[c] = []

    global BestCache
    BestCache = [0] * E
    for e in range(E):
        [Ld, K] = get_arr(inp)
        BCList = []
        for c in range(K):
            [c, Lc] = get_arr(inp)
            Lc = Ld - Lc
            BCList.append((c, Lc))
        sorted(BCList, key = lambda x: -x[1])
        BestCache[e] = BCList

    for r in range(R):
        [Rv, Re, Rn] = get_arr(inp)


def addVideo(e, v, BC):
    CVE[(e, v)] = BC
    CachedVideos[BC].append(v)

def processQ():
    req = heapq.heappop(RH)
    v = req[2]
    e = req[3]
    n = req[4]
    BC = getBC(e, S[v])
    if BC < 0:
        return
    if (e, v) in CVE.keys():
        if CVE[(e, v)] != BC:
            heapq.heappush(RH, (goodness(v, e, n), req[1], v, e, n))
        return
    addVideo(e, v, BC)

def main():
    if len(sys.argv) < 3:
        sys.exit('Usage: %s input.in output.out'.format(sys.argv[0]))
    

    read_file(sys.argv[1])
    print(V,E,R,C,X)
    print(S)
    out = open(sys.argv[2], 'w')

if __name__ == '__main__':
    main()
