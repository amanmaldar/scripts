import subprocess

 #a nfdc route add /ndn/d-site/d 261
# How to run?
# a /usr/bin/python /home/lenovo/Dropbox/scripts/zeroAll.py
bashCommand = {}

resultDir =  " >> /home/lenovo/Dropbox/loadingFib.txt"
print "Zero all"

bashCommand[0] = "ndnping /ndn/metrics/zero -i 1 -c 1 -n 123456 -o 1"
bashCommand[1] = "b ndnping /ndn/metrics/zero -i 1 -c 1 -n 123456 -o 1"
bashCommand[2] = "c ndnping /ndn/metrics/zero -i 1 -c 1 -n 123456 -o 1"
bashCommand[3] = "d ndnping /ndn/metrics/zero -i 1 -c 1 -n 123456 -o 1"


for i, v in bashCommand.iteritems():
	output = subprocess.call(['bash', '-c', bashCommand[i] + resultDir])
	
	print "done",i+1

