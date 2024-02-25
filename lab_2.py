def kubiki():
    num_list_a = int(input('Enter number of list for Anya: '))
    num_list_b = int(input('Enter number of list for Borya: '))
    print('Enter elements for Anya: ')
    set_a = set()
    for i in range(num_list_a):
        elem = int(input())
        set_a.add(elem)
    print('Enter elements for Borya: ')
    set_b = set()
    for i in range(num_list_b):
        elem = int(input())
        set_b.add(elem)
    print('Intersection Anya and Borya: ')
    print(len(set_a.intersection(set_b)))
    print(set_a.intersection(set_b))
    print('Only Anya: ')
    print(len(set_a.difference(set_b)))
    print(set_a.difference(set_b))
    print('Only Borya: ')
    print(len(set_b.difference(set_a)))
    print(set_b.difference(set_a))


