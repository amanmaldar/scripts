import subprocess


subprocess.call(['bash', '-c', " nfdc status show"])
eraseCommand = " nfdc cs erase /ndn/d-site count 250 >> /home/lenovo/Dropbox/erase.txt"

for i in range (265):
	output = subprocess.call(['bash', '-c', eraseCommand])


print "Done"
subprocess.call(['bash', '-c', " nfdc status show"])




