import sqlite3 as db

"""get the RIGHT gesture info from db"""
def GetTrueActions(id):
    cu.execute("select * from gestureInfo where ID='" + id + "'")
    rows = cu.fetchall()
    for row in rows:
        TA = [row[1],row[2],row[3],row[4],row[5]]
    return TA

"""compere the gesture between database and rec file"""
def CompereActions(ta,na):
    rightNo = 0
    for i in range(5):
        if ta[i] == na[i]:
            rightNo += 1
    return rightNo

#filename = input("Plz input out filename:")
recfile = open("rec.out",'r')	#ファイルを開く
lines = recfile.readlines()
recfile.close()

conn = db.connect("D:\\Database\\sqlite\\gustureInfo.db")
cu = conn.cursor()
conn.row_factory = db.Row
actionNo = 0
Taction = []
Naction = []
name = ''
results = {}


for line in lines:
    line = line.rstrip()
    if line.find("rec")>0:
        strings = line.split("_")
        num = strings[1][:-5]
        name = strings[0][-3:]
        if name in results:
            results[name][0] += 5
        else:
            results[name] = [5,0]
        actionNo = 0
        Taction = GetTrueActions(num)

    if (line.find("R_") > 0) or (line.find("L_") > 0):
        strings = line.split(" ")
        Naction.append(strings[2])
        actionNo += 1
        if actionNo == 5:
            rightNo = CompereActions(Taction,Naction)
            results[name][1] += rightNo
            del Naction[:]

results = sorted(results.items(), key=lambda d: d[0])
filePath = "D:\\result.txt"
wf = open(filePath,'w')
for res in results:
    wf.write(str(res[0])+",")
    wf.write(str(res[1][0])+",")
    wf.write(str(res[1][1])+"\n")
wf.close()
print(results)
print("done")


