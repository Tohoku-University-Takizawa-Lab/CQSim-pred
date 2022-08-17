import sys

# read in result file
file = open("../data/Results/" + sys.argv[1] + '.rst', 'r')
rst = file.readlines()
log = []
count = 0
for line in rst:
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

# read in log file
with open("../data/InputFiles/" + sys.argv[1] + '.swf', 'r') as file:
    log = []
    for line in file:
        if(line[0] != ';'):
            log.append(line.split())

# calculate success percentage
success = 0.0
for i in range(len(log)):
    if (float(log[i][18]) >= float(log[i][3])):
        success += 1
print("success  : ", '{:.2%}'.format(success / len(log)))