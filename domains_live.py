#Ping all the registered domains in AWS. if they don't reply, they are probably not used
import os

def main():
	#read the domain file
	file=open("/Users/thanostak/Desktop/Domains_Bang.csv", "r")
	lines=file.readlines()
	file.close()
	with open( "/Users/thanostak/Desktop/notworkingdomains.csv", "a" ) as domain_list:
		for line in lines:
			domain=line.strip()
			response=os.system(" ping -c 4 " + domain)
			if response>0:
				domain_list.write("{}\n".format(domain))
				domain_list.flush()	

main()
