import subprocess

bashCommand = {}

showCommand = " ndnping /ndn/metrics/show -i 1 -c 1 -n 1234567 -o 1"
zeroCommand = " ndnping /ndn/metrics/zero -i 1 -c 1 -n 1234567 -o 1"
resultDir = " >> /home/lenovo/Dropbox/Thesis/Logs/minindn4/clientLogs_1.txt"

# sample test pattern
pingServer
d ndnpingserver /ndn/d-site/d -x 1000000 &> /home/lenovo/Dropbox/Thesis/Logs/minindn3/serverLogs.txt &
testing
a ndnping /ndn/d-site/d -i 1 -c 1 -n 777777

a ndnping /ndn/metrics/zero -c 1 -i 1 -o 1 -n 1234567 
d ndnping /ndn/metrics/zero -c 1 -i 1 -o 1 -n 1234567 

a ndnping /ndn/d-site/d -i 1 -c 1000 -n 1
a ndnping /ndn/metrics/show -c 1 -i 1 -o 1 -n 1234567 
d ndnping /ndn/metrics/show -c 1 -i 1 -o 1 -n 1234567 

a ndnping /ndn/d-site/d -i 1 -c 1000 -n 500
a ndnping /ndn/metrics/show -c 1 -i 1 -o 1 -n 1234567 
d ndnping /ndn/metrics/show -c 1 -i 1 -o 1 -n 1234567 

a ndnping /ndn/d-site/d -i 1 -c 1000 -n 1000
a ndnping /ndn/metrics/show -c 1 -i 1 -o 1 -n 1234567 
d ndnping /ndn/metrics/show -c 1 -i 1 -o 1 -n 1234567 


a ndnping /ndn/d-site/d -i 1 -c 1000 -n 1400
a ndnping /ndn/metrics/show -c 1 -i 1 -o 1 -n 1234567 
d ndnping /ndn/metrics/show -c 1 -i 1 -o 1 -n 1234567 


a ndnping /ndn/d-site/d -i 1 -c 1000 -n 1700
a ndnping /ndn/metrics/show -c 1 -i 1 -o 1 -n 1234567 
d ndnping /ndn/metrics/show -c 1 -i 1 -o 1 -n 1234567 


a ndnping /ndn/d-site/d -i 1 -c 1000 -n 2000
a ndnping /ndn/metrics/show -c 1 -i 1 -o 1 -n 1234567 
d ndnping /ndn/metrics/show -c 1 -i 1 -o 1 -n 1234567 


a ndnping /ndn/d-site/d -i 1 -c 1000 -n 2200
a ndnping /ndn/metrics/show -c 1 -i 1 -o 1 -n 1234567 
d ndnping /ndn/metrics/show -c 1 -i 1 -o 1 -n 1234567 


bashCommand[0] = zeroCommand
bashCommand[1] = " ndnping " + interestPrefix + " -i 1 -c 1000 -n 1"	# 1-1000
bashCommand[2] = showCommand
bashCommand[3] = " ndnping " + interestPrefix + " -i 1 -c 1000 -n 500"	# 500-1500
bashCommand[4] = showCommand
bashCommand[5] = " ndnping " + interestPrefix + " -i 1 -c 1000 -n 1000"	# 1000-2000
bashCommand[6] = showCommand
bashCommand[7] = " ndnping " + interestPrefix + " -i 1 -c 1000 -n 1400"	# 1400-2400
bashCommand[8] = showCommand
bashCommand[9] = " ndnping " + interestPrefix + " -i 1 -c 1000 -n 1700"	# 1700-2700
bashCommand[10] = showCommand
bashCommand[11] = " ndnping " + interestPrefix + " -i 1 -c 1000 -n 2000" # 2000 - 3000
bashCommand[12] = showCommand
bashCommand[13] = " ndnping " + interestPrefix + " -i 1 -c 1000 -n 2200" # 2200 - 3200
 

