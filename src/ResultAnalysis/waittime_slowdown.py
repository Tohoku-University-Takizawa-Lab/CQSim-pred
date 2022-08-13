import sys

file = open("../data/Results/" + sys.argv[1], 'r')
Lines = file.readlines()
log = []
count = 0
for line in Lines:
    count += 1
    element = []
    # print("Line{}: {}".format(count, line.strip()))
    element.append(int(line.split(';')[0]))
    element.append(int(line.split(';')[1]))
    element.append(int(line.split(';')[2]))
    element.append(float(line.split(';')[3]))
    element.append(float(line.split(';')[4]))
    element.append(float(line.split(';')[5]))
    element.append(float(line.split(';')[6]))
    element.append(float(line.split(';')[7]))
    log.append(element)

# calculate average wait time
sum = 0.0
for i in range(len(log)):
    sum +=log[i][5]

print("wait time: ", sum/len(log))

# calculate average slowdown
slowdown = 0.0
for i in range(len(log)):
    slowdown += (log[i][5] + log[i][4]) / log[i][4]

print("slow down: ", slowdown/len(log))
