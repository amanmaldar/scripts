# Description
# pit processing time for FIB load scenario
import subprocess

bashCommand = {}

showCommand = " ndnping /ndn/metrics/show -i 1 -c 1 -n 1234567 -o 1"
zeroCommand = " ndnping /ndn/metrics/zero -i 1 -c 1 -n 1234567 -o 1"
resultDir = " >> /home/amaldar/clientLogs_1.txt"

# sample test pattern. This should pass before starting test
# pingServer =  ndnpingserver /ndn/d-site/d/prefix4/prefix5/prefix6/prefix7/prefix8/prefix9/prefix10 -x 1000000 &> /home/amaldar/serverLogs.txt &
# ndnping /ndn/d-site/d/prefix4/prefix5/prefix6/prefix7/prefix8/prefix9/prefix10 -i 1 -c 1 -n 777777


print "Starting the pings"
interestPrefix = "/ndn/d-site/d/"

bashCommand[0] = zeroCommand
#measurement 1
bashCommand[1] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 1"				# request 5000 packets and call show
bashCommand[2] = showCommand	# miss
bashCommand[3] = zeroCommand
bashCommand[4] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 1"				# request same 5000 packets and call show
bashCommand[5] = showCommand	# hit

# setting up cs
bashCommand[6] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 5001"				# load 5000 more packets nCS = 10000
bashCommand[7] = zeroCommand
#measurement 2
bashCommand[8] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 10001"			# request 5000 packets and call show   
bashCommand[9] = showCommand 	# miss
bashCommand[10] = zeroCommand
bashCommand[11] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 10001"			# request same 5000 packets and call show   
bashCommand[12] = showCommand	# hit											

# setting up cs
bashCommand[13] = " ndnping " + interestPrefix + " -i 1 -c 10000 -n 15001"			# load 10000 more packets nCS = 25000
bashCommand[14] = zeroCommand
#measurement 3
bashCommand[15] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 25001"			# request 5000 packets and call show 
bashCommand[16] = showCommand	# miss													 
bashCommand[17] = zeroCommand
bashCommand[18] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 25001"			# request same 5000 packets and call show 
bashCommand[19] = showCommand	# hit										

# setting up cs
bashCommand[20] = " ndnping " + interestPrefix + " -i 1 -c 10000 -n 30001"			# load 10000 more packets nCS = 40000
bashCommand[21] = zeroCommand
#measurement 4
bashCommand[22] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 40001"			# request 5000 packets and call show
bashCommand[23] = showCommand	# miss
bashCommand[24] = zeroCommand
bashCommand[25] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 40001"			# request same 5000 packets and call show
bashCommand[26] = showCommand	# hit										

# setting up cs
bashCommand[27] = " ndnping " + interestPrefix + " -i 1 -c 10000 -n 45001"			# load 10000 more packets nCS = 55000
bashCommand[28] = zeroCommand
#measurement 5
bashCommand[29] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 55001"			# request 5000 packets and call show
bashCommand[30] = showCommand	# miss
bashCommand[31] = zeroCommand
bashCommand[32] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 55001"			# request same 5000 packets and call show
bashCommand[33] = showCommand	# hit 										

# setting up cs
bashCommand[34] = " ndnping " + interestPrefix + " -i 1 -c 5536 -n 60001"			# load 5535 more packets nCS = 65535
bashCommand[35] = zeroCommand
#measurement 6
bashCommand[36] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 66001"			# request 5000 packets and call show
bashCommand[37] = showCommand 	# miss
bashCommand[38] = zeroCommand
bashCommand[39] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 66001"			# request same 5000 packets and call show
bashCommand[40] = showCommand 	# hit

# Run 2 measurement for 65k+ scenario
#measurement 7
bashCommand[41] = zeroCommand
bashCommand[42] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 73000"			# request 5000 packets and call show
bashCommand[43] = showCommand	# miss
bashCommand[44] = zeroCommand
bashCommand[45] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 73000"			# request 5000 packets and call show
bashCommand[46] = showCommand	# hit									



for i, v in bashCommand.iteritems():
	output = subprocess.call(['bash', '-c', bashCommand[i] + resultDir])
	
	print "done",i+1

print "Get the results"




