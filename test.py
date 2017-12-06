#hw2_q1_skl_slm.py

import statistics
import math
def slm(xlist, ylist):
    #develop your function here...
    for i in range(len(xlist)):
        xlist[i] = float(xlist[i])
    for j in range(len(ylist)):
        ylist[j] = float(ylist[j])
	
    if len(xlist) != len(ylist):
        return None
    elif len(xlist) < 5 or len(ylist) < 5:
        return None
    else:
        n = len(xlist)
        xmean = statistics.mean(xlist)
        ymean = statistics.mean(ylist)
        
        eupsum = float(0)
        upsum = float(0)
        downsum = float(0)

        for i in range(n):
            upsum += (ylist[i] - ymean) * (xlist[i] - xmean)
            downsum += pow((xlist[i] - xmean), 2)
			
        b = float(upsum / downsum)
        a = ymean - b * xmean
		
        for i in range(n):
            eupsum += pow((ylist[i] - a - b * xlist[i]), 2)
			
        s = pow((eupsum / (n - 2)), 0.5)
		
        final_list = [a, b, s]
        return final_list
		
#=======
xstr = input()
ystr = input()

xall = xstr.split(',')
yall = ystr.split(',')

out1 = slm(xall, yall)
if(out1 == None):
    print("DATA_ERROR")
else:
    print("%0.6f" % out1[0])
    print("%0.6f" % out1[1])
    print("%0.6f" % out1[2])
