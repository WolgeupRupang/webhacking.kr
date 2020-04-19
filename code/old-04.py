import hashlib

f = open("rainbowtable.txt",'w')

for i in range(10000000, 10000010):
    session = "%dsalt_for_you" % i
    h = session
    for j in range(0,500):
        h = hashlib.sha1(h.encode('utf-8')).hexdigest()
    data = session + " - " + h + "\n"
    f.write(data)

f.close()
