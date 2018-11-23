# Description
'''
Prints Hit and Miss latencies 
Prints processing time for packet on the requestor. measurements are made between onIncomingInterest and onOutgoingInterest. So It works well for intermediate forwarders.
This doesn't work well if data is satisfied from CS.
'''
import subprocess

bashCommand = {}

showCommand = " ndnping /ndn/metrics/show -i 1 -c 1 -n 1234567 -o 1"
zeroCommand = " ndnping /ndn/metrics/zero -i 1 -c 1 -n 1234567 -o 1"
resultDir = " >> /home/amaldar/clientLogs_1.txt"

# sample test pattern
# pingServer =  d ndnpingserver /ndn/d-site/d/prefix4/prefix5/prefix6/prefix7/prefix8/prefix9/prefix10 -x 1000000 &> /home/lenovo/Dropbox/Thesis/Logs/minindn3/serverLogs.txt &
# a ndnping /ndn/d-site/d/prefix4/prefix5/prefix6/prefix7/prefix8/prefix9/prefix10 -i 1 -c 1 -n 777777


print "Starting the pings"
interestPrefix = "/ndn/d-site/d/prefix4/prefix5/prefix6/prefix7/prefix8/prefix9/prefix10"

bashCommand[0] = zeroCommand
#measurement 1
bashCommand[1] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 1"				# request 5000 packets and call show
bashCommand[2] = showCommand	# miss
bashCommand[3] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 1"				# request same 5000 packets and call show
bashCommand[4] = showCommand	# hit

# setting up cs
bashCommand[5] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 5001"				# load 5000 more packets nCS = 10000
bashCommand[6] = zeroCommand
#measurement 2
bashCommand[7] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 10001"			# request 5000 packets and call show   
bashCommand[8] = showCommand 	# miss
bashCommand[9] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 10001"			# request same 5000 packets and call show   
bashCommand[10] = showCommand	# hit											

# setting up cs
bashCommand[11] = " ndnping " + interestPrefix + " -i 1 -c 10000 -n 15001"			# load 10000 more packets nCS = 25000
bashCommand[12] = zeroCommand
#measurement 3
bashCommand[13] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 25001"			# request 5000 packets and call show 
bashCommand[14] = showCommand	# miss													 
bashCommand[15] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 25001"			# request same 5000 packets and call show 
bashCommand[16] = showCommand	# hit										

# setting up cs
bashCommand[17] = " ndnping " + interestPrefix + " -i 1 -c 10000 -n 30001"			# load 10000 more packets nCS = 40000
bashCommand[18] = zeroCommand
#measurement 4
bashCommand[19] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 40001"			# request 5000 packets and call show
bashCommand[20] = showCommand	# miss
bashCommand[21] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 40001"			# request same 5000 packets and call show
bashCommand[22] = showCommand	# hit										

# setting up cs
bashCommand[23] = " ndnping " + interestPrefix + " -i 1 -c 10000 -n 45001"			# load 10000 more packets nCS = 55000
bashCommand[24] = zeroCommand
#measurement 5
bashCommand[25] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 55001"			# request 5000 packets and call show
bashCommand[26] = showCommand	# miss
bashCommand[27] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 55001"			# request same 5000 packets and call show
bashCommand[28] = showCommand	# hit 										

# setting up cs
bashCommand[29] = " ndnping " + interestPrefix + " -i 1 -c 5536 -n 60001"			# load 5535 more packets nCS = 65535
bashCommand[30] = zeroCommand
#measurement 6
bashCommand[31] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 66001"			# request 5000 packets and call show
bashCommand[32] = showCommand 	# miss
bashCommand[33] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 66001"			# request same 5000 packets and call show
bashCommand[34] = showCommand 	# hit

# Run 2 measurement for 65k+ scenario
#measurement 7
bashCommand[35] = zeroCommand
bashCommand[36] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 73000"			# request 5000 packets and call show
bashCommand[37] = showCommand	# miss
bashCommand[38] = " ndnping " + interestPrefix + " -i 1 -c 5000 -n 73000"			# request 5000 packets and call show
bashCommand[39] = showCommand	# hit									



for i, v in bashCommand.iteritems():
	output = subprocess.call(['bash', '-c', bashCommand[i] + resultDir])
	
	print "done",i+1

print "Get the results"




