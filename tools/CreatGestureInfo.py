filePath = "D:\\GestureIndex.csv"
f = open(filePath,'w')
indexID = 1
for LR in range(2):
    for a1 in range(4):
        for a2 in range(4):
            if a2 == a1:
                continue
            for a3 in range(4):
                if a3 == a2:
                    continue
                for a4 in range(4):
                    if a4 == a3:
                        continue
                    for a5 in range(4):
                        if a5 == a4:
                            continue
                        if LR == 0:
                            hand = 'L_'
                        else:
                            hand = 'R_'
                        wstr = hand+str(a1)+","+hand+str(a2)+","+hand+str(a3)+","+hand+str(a4)+","+hand+str(a5)
                        f.write(wstr+"\n")
f.close()


