'''вариант 5'''


'''Task1'''
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


'''Task2'''
f = open("task_2.txt", "r", encoding="utf-8")
text = f.read()
f_dict = {}
f_set = set()
f_list = []
for i in range(len(text)):
    if text[i].isalpha():
        f_set.add(text[i].lower())
        f_list.append(text[i].lower())
for i in f_set:
    f_dict[i] = str(f_list.count(i) / len(text) * 100) + " %"
print(f_dict)

'''считаем частоту встречаемости без учета регистра в тексте с учетом всех символов'''