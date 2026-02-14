spam = "initial spam"

def do_local():
    spam = "local spam"
    print(spam)

print(spam)
do_local()

var = 2

def func():
    global var
    var += 1
    print(var)

print(var)
func()

def outer():
    def do_nonlocal():
        nonlocal spam
        spam = "non-local spam"
    def do_local():
        spam = "local spam"
    spam = "outer_spam"
    do_local()
    print(spam) #local can't affect
    do_nonlocal()
    print(spam) #nonlocal can affect
outer()