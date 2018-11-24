import subprocess

 #a nfdc route add /ndn/d-site/d 261
# How to run?
# a /usr/bin/python /home/lenovo/Dropbox/scripts/fibLoad.py

resultDir =  " >> /home/lenovo/Dropbox/loadingFib.txt"
interestPrefix = [ "/ndn/d-site/d/prefix4/prefix5/prefix6/prefix7/prefix8/prefix9/",
"/ndn/d-site/d/prefix4/prefix5/prefix6/prefix7/prefix8/",
"/ndn/d-site/d/prefix4/prefix5/prefix6/prefix7/",
"/ndn/d-site/d/prefix4/prefix5/prefix6/",
"/ndn/d-site/d/prefix4/prefix5/",
"/ndn/d-site/d/prefix4/"
]
total = 0

print "Loading FIB Entries"
n = 0
for n in range (0,1): #len(interestPrefix)
	for i in range(80001,90000):
		
		bashCommand = " nfdc route add "+ interestPrefix[n]+str(i)+" udp://129.62.205.73"  
		# bashCommand = " nfdc route add "+ interestPrefix[n]+str(i)+" 264"  
		output = subprocess.call(['bash', '-c', bashCommand + resultDir])
		total += 1
	print "done", n
		#print bashCommand
print total, "Fib Entries Loaded"

