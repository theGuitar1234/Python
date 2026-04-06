def adaptive_trapezoid(func, a, b, error) :
    area_full = (b-a)*0.5*(func(a) + func(b))
    mid = (a+b)/2
    area_mid = (mid-a)*0.5*(func(a) + func(mid)) + (b-mid)*0.5*(func(mid) + func(b))

    if abs(area_full-area_mid) < error :
        return area_mid
    else :
        return adaptive_trapezoid(func, a, mid, error/2) + adaptive_trapezoid(func, mid, b, error/2)

def func(x):
    return x**2

print(adaptive_trapezoid(func, 0, 1, 0.00000001))
