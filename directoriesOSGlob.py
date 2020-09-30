import os, time, glob

os.chdir("C:/")

n, t = 0, time.time()
# for i in range(1000):
#     n += len(os.listdir("./%d" % i))

for each in os.listdir("./"):
	n += 1;
t = time.time() - t
print ("os.listdir: %.4fs, %d files found"% (t, n))


os.chdir("H:/1. Python Data Science/Exercises/Log File Analysis")
n, t = 0, time.time()
# for each in os.walk("./"):
# 	print (each)
for root, dirs, files in os.walk("./"):
	print (os.getcwd())
	print (files)
	for file in files:
		n += 1
t = time.time() - t
print ("os.walk: %.2fs, %d files found" % (t, n))

n, t = 0, time.time()
for i in range(1000):
    n += len(glob.glob("./%d/*" % i))
t = time.time() - t
print ("glob.glob: %.4fs, %d files found" % (t, n))

for each in glob.glob("H:/1. Python Data Science/Exercises"):
	print (each)