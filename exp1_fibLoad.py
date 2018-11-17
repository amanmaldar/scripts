import subprocess

 #a nfdc route add /ndn/d-site/d 261

print "Loading FIB Entries"
for i in range(6001,6005):
    bashCommand = " nfdc route add /ndn/d-site/d/"+str(i)+" 264"
    output = subprocess.call(['bash', '-c', bashCommand])
    #print bashCommand
print "1000 Fib Entries Loaded"

