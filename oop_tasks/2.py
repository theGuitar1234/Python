class MyList(list):
    def print_sorted(self):
        new_list = [i for i in self]
        new_list.sort()
        print(new_list)

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)

# [1, 4, 2, 3, 5]
# [1, 2, 3, 4, 5]
# [1, 4, 2, 3, 5]