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

bashCommand[0] = zeroCommand
bashCommand[1] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 1"				# request 5000 packets and call show
bashCommand[2] = showCommand

bashCommand[3] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 5001"				# load 5000 more packets nCS = 10000
bashCommand[4] = zeroCommand
bashCommand[5] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 10001"			# request 5000 packets and call show   
bashCommand[6] = showCommand													

bashCommand[7] = " ndnping " + interestPrefix + " -i 1 -c 10000 -n 15001"			# load 10000 more packets nCS = 25000
bashCommand[8] = zeroCommand
bashCommand[9] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 25001"			# request 5000 packets and call show 
bashCommand[10] = showCommand													

bashCommand[11] = " ndnping " + interestPrefix + " -i 1 -c 10000 -n 30001"			# load 10000 more packets nCS = 40000
bashCommand[12] = zeroCommand
bashCommand[13] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 40001"			# request 5000 packets and call show
bashCommand[14] = showCommand													

bashCommand[15] = " ndnping " + interestPrefix + " -i 1 -c 10000 -n 45001"			# load 10000 more packets nCS = 55000
bashCommand[16] = zeroCommand
bashCommand[17] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 55001"			# request 5000 packets and call show
bashCommand[18] = showCommand													

bashCommand[19] = " ndnping " + interestPrefix + " -i 1 -c 5536 -n 60001"			# load 5535 more packets nCS = 65535
bashCommand[20] = zeroCommand
bashCommand[21] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 66001"			# request 5000 packets and call show
bashCommand[22] = showCommand		

bashCommand[23] = zeroCommand
bashCommand[24] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 73000"			# request 5000 packets and call show
bashCommand[25] = showCommand												


for i, v in bashCommand.iteritems():
	output = subprocess.call(['bash', '-c', bashCommand[i] + resultDir])
	
	print "done",i+1

print "Get the results"




