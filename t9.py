import subprocess
import time


bashCommand = {}

showCommand = " ndnping /ndn/metrics/show -i 1 -c 1 -n 1234567 -o 1"
zeroCommand = " ndnping /ndn/metrics/zero -i 1 -c 1 -n 1234567 -o 1"
resultDir = " >> /home/lenovo/Dropbox/Thesis/Logs/minindn4/clientLogs_1.txt"

# sample test pattern
# pingServer =  d ndnpingserver /ndn/d-site/d -x 1000000 &> /home/lenovo/Dropbox/Thesis/Logs/minindn3/serverLogs.txt &
# a ndnping /ndn/d-site/d -i 1 -c 1 -n 777777

# how to run
#  a /usr/bin/python /home/lenovo/Dropbox/scripts/t6.py


print "Starting the pings"


ping1 = " ndnping /ndn/d-site/d -i 1 -c 5000 -n 1"
ping2 = " ndncatchunks -d iterative -v /ndn/d-site/d/100MB.txt &> /home/lenovo/Dropbox/10mb.txt"


subprocess.call(['bash', '-c', zeroCommand + resultDir])
start = time.time()
#subprocess.call(['bash', '-c', ping1 + resultDir])


subprocess.call(['bash','-c', ping2 ])
	

done = time.time()
elapsed = done - start
print "elapsed", elapsed*1000, "mS"
subprocess.call(['bash', '-c', showCommand + resultDir])

print "Get the results"




