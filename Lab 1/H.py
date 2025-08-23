def train_sort(n, train, time, dest):
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if train[i] < train[j] or (train[i] == train[j] and time[i] > time[j]):
                train[i], train[j] = train[j], train[i]
                time[i], time[j] = time[j], time[i]
                dest[i], dest[j] = dest[j], dest[i]
                i = j
            elif train[i] == train[j] and time[i] == time[j]:
                break
            else:
                break
 
    for i in range(n):
        print(f'{train[i]} will departure for {dest[i]} at {time[i]}')
 
 
n = int(input())
train = []
time = []
dest = []
 
for x in range(n):
    line = input().split()
    train.append(line[0])
    time.append(line[-1])
    dest.append(line[-3])
 
train_sort(n, train, time, dest)