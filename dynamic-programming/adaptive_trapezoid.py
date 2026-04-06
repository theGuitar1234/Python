def adaptive_trapezoid(func, a, b, error) :

    stack = [(a, b, error)]
    total_area = 0

    while len(stack)>0 :
        a, b, error = stack.pop()
        area_full = (b-a)*0.5*(func(a) + func(b))
        mid = (a+b)/2
        area_mid = (mid-a)*0.5*(func(a) + func(mid)) + (b-mid)*0.5*(func(mid) + func(b))

        if abs(area_full-area_mid) < error :
            total_area += area_mid
        else :
            stack.append((a, mid, error/2))
            stack.append((mid, b, error/2))

    return total_area

def func(x):
    return x**2

print(adaptive_trapezoid(func, 0, 1, 0.00000001))
