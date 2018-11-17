import subprocess

resultDir = " >> /home/lenovo/Dropbox/Thesis/Logs/minindn4/clientLogs_1.txt"

ndnping = "ndnping /ndn/d-site/d -c 1"

print "Starting the pings"


for i in range(0,10):
	output = subprocess.call(['bash','-c', ndnping + " -n "+str(i)])
	

print "Get the results"




