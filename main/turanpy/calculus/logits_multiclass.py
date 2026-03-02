from ..algebra.dot_product import dot_product as dt

def lgts_mc(W, b, x):
    return [dt(Wk, x) + bk for Wk, bk in zip(W, b)]

if __name__ == "__main__":
    pass