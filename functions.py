from math import exp

SAMPLING_TIME = 0.1

def mux_2(sel, in1, in2):
    return [j if s else i for s,i,j in zip(sel, in1, in2)]


def greater_or_equal(in1, in2):
    return [i>=j for i,j in zip(in1, in2)]


def smaller(in1, in2):
    return [i<j for i,j in zip(in1, in2)]


def or_3(in1, in2, in3):
    return [bool(i or j or k) for i,j,k in zip(in1, in2, in3)]


def and_2(in1, in2):
    return [bool(i and j) for i,j in zip(in1, in2)]


def and_3(in1, in2, in3):
    return [bool(i and j and k) for i,j,k in zip(in1, in2, in3)]


def and_4(in1, in2, in3, in4):
    return [bool(i and j and k and l) for i,j,k,l in zip(in1, in2, in3, in4)]


def and_5(in1, in2, in3, in4, in5):
    return [bool(i and j and k and l and m) for i,j,k,l,m in zip(in1, in2, in3, in4, in5)]


def bitwiseAND(in1, in2):
    return [i & j for i,j in zip(in1, in2)]


def bitwiseOR(in1, in2):
    return [i | j for i,j in zip(in1, in2)]


def not_(in1):
    return [not(i) for i in in1]


def abs_(in1):
    return [abs(i) for i in in1]


def min_2(in1, in2):
    return [min(i, j) for i,j in zip(in1, in2)]


def max_2(in1, in2):
    return [max(i, j) for i,j in zip(in1, in2)]


def curve_1d(in1):
    return in1


def curve_2d(in1, in2):
    return (in1 + in2) // 2


def turn_on_delay(in1, delay_time, dt):
    pass


def hysteresis(in1, lsp, rsp):
    output = [0]
    for index, _ in enumerate(in1[1:], 1):
        if in1[index] < lsp[index]:
            output.append(False)
        elif in1[index] > rsp[index]:
            output.append(True)
        else:
            output.append(in1[index-1] if index > 0 else 0)
             
    return output


def pt1(x, t1, dt):
    output = []
    for index, t in enumerate(t1):
        if t:
            Q = exp(-dt[index]/t)
            state = Q * (output[index-1] if len(output) > 0 else 0) + (1.0-Q)*x[index]
        else:
            state = x[index]
        
        output.append(state)
    return output


def raising_edge(in1):
    output = [0]
    for index in range(1, len(in1)):
        output.append(in1[index] > in1[index - 1])
    
    return output


def falling_edge(in1):
    output = [0]
    for index in range(1, len(in1)):
        output.append(in1[index] < in1[index - 1])
    
    return output


def DSM_DebRepCheck(dfc_id, inp, _, deb_t):
    dfc = dfc_id
    output = []
    for index, _ in enumerate(inp[1:], 1):
        if index*SAMPLING_TIME >= deb_t:
            if inp[index] == 1 and inp[index-1] == 0:
                dfc = (1 << 4) | dfc
            elif inp[index] == 0 and inp[index-1] == 1:
                dfc = dfc & ( ~(1 << 4))

        output.append(dfc)
    
    return output


def dsm_getPermission(fid):
    return getbit(fid,12)


def getbit(n,bit):
    return (n >> (bit)) & 1 == True


def dsm_resetDeb(n):
    return (n & (~(1 << 2)))


def rsflipflop(r,s):
    flip_flop_q = [0]
    for index in range(1, len(r)):
        if (r[index] is True) & (s[index] is False):
            q = False
        elif (r[index] is False) & (s[index] is False):
            q = flip_flop_q[-1]
        elif (r is False) & (s is True):
            q = True
        else:
            q = False
    
        flip_flop_q.append(q)

    return flip_flop_q

