'''вариант 5'''


for file in '27-166a.txt', '27-166b.txt':
    f = open(file)
    f_list = []
    for line in f:
        f_list.append(line)
    n = int(f_list[0].split()[0])
    k = int(f_list[0].split()[1])
    f_list[0] = 0
    f_list = [int(a) for a in f_list]
    max_i = 0
    for i in range(1, n - 2 * k + 1):
        '''+2, т.к. длина списка = n+1 и последний индекс в stop среза не включается'''
        res = max(f_list[i:n - 2 * k + 2]) + max(f_list[i + k:n - k + 2]) + max(f_list[i + 2 * k:n + 2])
        if res > max_i:
            max_i = res
    print(max_i)
    f.close()
'''27-166a.txt: 280212'''
'''27-166b.txt: 26997'''




