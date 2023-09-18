import re
try:
    fhand = open("mbox.txt")
except:
    print("file cannot be opened")
    exit()
count = 0
for line in fhand:
    line = line.rtirp()
    if re.search('From:',line):
        print(line)
        count = count + 1
print("total %d lines printed" %count)