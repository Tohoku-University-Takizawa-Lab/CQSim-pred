import sys

with open("../data/InputFiles/" + sys.argv[1]) as origin:
    header = []
    body = []
    for line in origin:
        if(line[0] != ';'):
            body.append(line.split())
        else:
            header.append(line)
with open("../data/InputFiles/predict/" + sys.argv[2]) as time:
    predictTime = []
    for line in time:
        predictTime.append(line)

for i in range(len(body)):
    body[i].append(int(float(predictTime[i])))
    # print(body[i])

output_path = "../data/InputFiles/" + sys.argv[1][:len(sys.argv[1])-4] + "_" +sys.argv[2][:len(sys.argv[2])-4] + ".swf"
with open(output_path, mode="w") as output:
    for i in range(len(header)):
        output.write(header[i])
    for i in range(len(body)):
        for j in range(len(body[i])):
            output.write(str(body[i][j]))
            output.write("    ")
        output.write("\n")