import subprocess

bashCommand = {}

showCommand = " ndnping /ndn/metrics/show -i 1 -c 1 -n 1234567 -o 1"
zeroCommand = " ndnping /ndn/metrics/zero -i 1 -c 1 -n 1234567 -o 1"
resultDir = " >> /home/lenovo/Dropbox/Thesis/Logs/minindn4/clientLogs_1.txt"

# sample test pattern
# pingServer =  d ndnpingserver /ndn/d-site/d/prefix4/prefix5/prefix6/prefix7/prefix8/prefix9/prefix10 -x 1000000 &> /home/lenovo/Dropbox/Thesis/Logs/minindn3/serverLogs.txt &
# a ndnping /ndn/d-site/d/prefix4/prefix5/prefix6/prefix7/prefix8/prefix9/prefix10 -i 1 -c 1 -n 777777


print "Starting the pings"
interestPrefix = "/ndn/d-site/d/prefix4/prefix5/prefix6/prefix7/prefix8/prefix9/prefix10"


 # pre requisite
 d ndnpingserver /ndn/d-site/d/ -x 1000000 &> /home/lenovo/Dropbox/Thesis/Logs/minindn3/serverLogs.txt &
 
 b ndnping /ndn/d-site/d -i 1 -c 1000 -n 1	# loading B-CS

 a ndnping /ndn/d-site/d -i 1 -c 1000 -n 5001 # loading A-CS

 # experiment
 c ndnping /ndn/metrics/zero -i 1 -c 1 -n 1234567 -o 1
 
 c ndnping /ndn/d-site/d -i 1 -c 1000 -n 7001 	# all new data
 c ndnping /ndn/metrics/show -i 1 -c 1 -n 1234567 -o 1
 
 c ndnping /ndn/d-site/d -i 1 -c 1000 -n 500 	# 500 from b, 500 from d 
 c ndnping /ndn/metrics/show -i 1 -c 1 -n 1234567 -o 1
 
 c ndnping /ndn/d-site/d -i 1 -c 1000 -n 5500 	# 500 from a, 500 from d 
 c ndnping /ndn/metrics/show -i 1 -c 1 -n 1234567 -o 1

