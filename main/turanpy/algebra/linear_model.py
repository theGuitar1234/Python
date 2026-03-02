from ..algebra.dot_product import dot_product as dt

def lm(w, x, b):
    return w*x+b

def multi_class_lm(w, x, b):
    return dt(w, x)+b

if __name__ == "__main__":
    pass