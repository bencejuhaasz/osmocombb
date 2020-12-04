import re
import pexpect
import telnetlib

def RunKraken(keystream):

	kraken_ip=self.kraken_ip
	kraken_port=self.kraken_port
	results = []

	tn= telnetlib.Telnet(kraken_ip, kraken_port)

	tn.write("crack %s\r\n" % keystream)


	(index, match, text)= tn.expect(['crack','Found [0-9]{1,}','@ [0-9]{1,}'], 90)
	if(match.group(0)!="crack"):
		key=match.group(0)
		key=key.split("Found ")[1]
	(index, match, text)= tn.expect(['crack','@ [0-9]{1,}'], 90)
	if(match.group(0)!="crack"):
		pos=match.group(0)
		pos=pos.split("@ ")[1]
		results.append((key, int(pos)))

	(index, match, text)= tn.expect(['crack','Found [0-9]{1,}','@ [0-9]{1,}'], 90)
	if(match.group(0)!="crack"):
		key=match.group(0)
		key=key.split("Found ")[1]
	(index, match, text)= tn.expect(['crack','@ [0-9]{1,}'], 90)
	if(match.group(0)!="crack"):
		pos=match.group(0)
		pos=pos.split("@ ")[1]
		results.append((key, int(pos)))
	return results
