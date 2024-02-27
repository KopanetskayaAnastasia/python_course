'''вариант 5'''


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


def access_rights():
    dict1 = {}
    num_files = int(input('Enter number of files: '))
    for i in range(num_files):
        set_operations = set()
        s = str(input('Enter file name, operations: '))
        s = s.split(" ")
        name_file = s[0]
        for j in s:
            if j != s[0]:
                set_operations.add(j.lower())
        dict1[name_file] = set_operations
    print(dict1)
    num_request = int(input('Enter number of request: '))
    dict2 = {}
    for i in range(num_request):
        s = str(input('Enter operation from {write,read,execute}, file_name: '))
        s = s.split(" ")
        if dict1[s[1]].__contains__(s[0][0]):
            print("OK")
        else:
            print("Access denied")


