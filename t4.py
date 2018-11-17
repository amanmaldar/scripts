import subprocess

bashCommand = {}

pingIt = " ndnping /ndn/d-site/d -c 1"
zeroCommand = " ndnping /ndn/metrics/zero -i 1 -c 1 -n 1234567 -o 1"
resultDir = " >> /home/lenovo/Dropbox/Thesis/Logs/minindn4/clientLogs_1.txt"

# sample test pattern
# pingServer =  d ndnpingserver /ndn/d-site/d/prefix4/prefix5/prefix6/prefix7/prefix8/prefix9/prefix10 -x 1000000 &> /home/lenovo/Dropbox/Thesis/Logs/minindn3/serverLogs.txt &
# a ndnping /ndn/d-site/d/prefix4/prefix5/prefix6/prefix7/prefix8/prefix9/prefix10 -i 1 -c 1 -n 777777


print "Starting the pings"

for i in range (0,10):
	#output = subprocess.call(['bash', '-c', pingIt])
	output = subprocess.call(['bash', '-c', pingIt + resultDir])


print "done"

print "Get the results"




