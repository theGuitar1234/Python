from turanpy.config import DEFAULTS

def sigmoid(z):
    e = DEFAULTS.e
    if z >= 0:
        ez = e**-z
        return 1.0 / (1.0 + ez)
    else:
        ez = e**z
        return ez / (1.0 + ez)

if __name__ == "__main__":
    pass