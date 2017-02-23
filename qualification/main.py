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

    global RH
    for r in range(R):
        [Rv, Re, Rn] = get_arr(inp)
        heapq.heappush(RH, (goodness(Rv, Re, Rn), r, Rv, Re, Rn))

def addVideo(e, v, BC):
    CVE[(e, v)] = BC
    CachedVideos[BC].append(v)

def printState():
    print("VERCX: " + str((V, E, R, C, X)))
    print("VSizes: " + str(S))
    print("CVE: " + str(CVE))
    print("CachedVideos: " + str(CachedVideos))
    print("RH: " + str(RH))
    print("BestCache: " + str(BestCache))

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

def write_answer(filename):
    out = open(filename, 'w')
    global CachedVideos
    s = 0
    for cv in CachedVideos:
        cv = CachedVideos[cv]
        if len(cv) > 0:
            s += 1

    out.write("{}\n".format(s))

    for cv in CachedVideos:
        idx = cv
        cv = CachedVideos[cv]
        if len(cv) > 0:
            out.write("{} ".format(idx))
            for x in cv:
                out.write("{} ".format(x))
            out.write("\n")

def testVideos():
    global CachedVideos
    CachedVideos[0] = [1,2]
    CachedVideos[1] = [3,4]

def main():
    if len(sys.argv) < 3:
        sys.exit('Usage: %s input.in output.out'.format(sys.argv[0]))
    

    read_file(sys.argv[1])


    printState()
    write_answer(sys.argv[2])


    while len(RH) > 0:
        processQ()

if __name__ == '__main__':
    main()
