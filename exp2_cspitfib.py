import subprocess

bashCommand = []
for i in range (0,7):
	bashCommand.append("hello");

showCommand = " ndnping /ndn/metrics/show -i 1 -c 1 -n 1"
resultDir = " >> /home/lenovo/Dropbox/Thesis/Logs/minindn3/clientLogs.txt"
statusDir = " >> /home/lenovo/Dropbox/Thesis/Logs/minindn3/status_2.txt"

print "Starting the pings"
bashCommand[0] = " ndnping /ndn/d-site/d -i 1 -c 5000 -n 1" 
bashCommand[1] = " ndnping /ndn/d-site/d -i 1 -c 5000 -n 6001"
bashCommand[2] = " ndnping /ndn/d-site/d -i 1 -c 10000 -n 15001"
bashCommand[3] = " ndnping /ndn/d-site/d -i 1 -c 20000 -n 30001"
bashCommand[4] = " ndnping /ndn/d-site/d -i 1 -c 25000 -n 60001"
bashCommand[5] = " ndnping /ndn/d-site/d -i 1 -c 5000 -n 100001"
bashCommand[6] = " ndnping /ndn/d-site/d -i 1 -c 5000 -n 110001"

for i in range (0,7):
	output = subprocess.call(['bash', '-c', bashCommand[i] + resultDir])
	output = subprocess.call(['bash', '-c', showCommand + statusDir])
	print "done",i+1,"/7"

print "Get the results"




