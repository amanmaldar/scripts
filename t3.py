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
bashCommand[2] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 1"				# request same 5000 packets and call show
bashCommand[3] = showCommand

bashCommand[4] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 5001"				# load 5000 more packets nCS = 10000
bashCommand[5] = zeroCommand
bashCommand[6] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 10001"			# request 5000 packets and call show   
bashCommand[7] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 10001"			# request 5000 packets and call show   
bashCommand[8] = showCommand													


bashCommand[9] = " ndnping " + interestPrefix + " -i 1 -c 10000 -n 15001"			# load 10000 more packets nCS = 25000
bashCommand[10] = zeroCommand
bashCommand[11] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 25001"			# request 5000 packets and call show 
bashCommand[12] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 25001"			# request 5000 packets and call show 
bashCommand[13] = showCommand													

bashCommand[14] = " ndnping " + interestPrefix + " -i 1 -c 10000 -n 30001"			# load 10000 more packets nCS = 40000
bashCommand[15] = zeroCommand
bashCommand[16] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 40001"			# request 5000 packets and call show
bashCommand[17] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 40001"			# request 5000 packets and call show
bashCommand[18] = showCommand													

bashCommand[19] = " ndnping " + interestPrefix + " -i 1 -c 10000 -n 45001"			# load 10000 more packets nCS = 55000
bashCommand[20] = zeroCommand
bashCommand[21] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 55001"			# request 5000 packets and call show
bashCommand[22] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 55001"			# request 5000 packets and call show
bashCommand[23] = showCommand													


bashCommand[24] = " ndnping " + interestPrefix + " -i 1 -c 5536 -n 60001"			# load 5535 more packets nCS = 65535
bashCommand[25] = zeroCommand
bashCommand[26] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 66001"			# request 5000 packets and call show
bashCommand[27] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 66001"			# request 5000 packets and call show
bashCommand[28] = showCommand		


bashCommand[29] = zeroCommand
bashCommand[30] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 73000"			# request 5000 packets and call show
bashCommand[31] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 73000"			# request 5000 packets and call show
bashCommand[32] = showCommand												



for i, v in bashCommand.iteritems():
	output = subprocess.call(['bash', '-c', bashCommand[i] + resultDir])
	
	print "done",i+1

print "Get the results"




