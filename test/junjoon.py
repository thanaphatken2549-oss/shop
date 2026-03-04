def sqrt_n_times(x, n):
    a = x**(1/(2**n))
    return a
def cube_root(y):
    b = y**((1/4)*(1/4)*(1/16)*(1/256))
    return b
def main():
    q = float(input())
    print(cube_root(q))
exec(input()) # DON'T remove this line