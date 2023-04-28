with open('logfile.txt', 'r', encoding='utf-8') as log, open('output.txt', 'w', encoding='utf-8') as out:
    lst = [line.strip().split(', ') for line in log.readlines()]
    for item in lst:
        item_1, item_2 = item[1].split(':'), item[2].split(':')
        print(item_1, item_2)
        if item_2[0] > item_1[0] and item_2[1] >= item_1[1]:
            print(item[0])

    print(lst)
