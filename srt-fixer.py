
import sys
import re
import argparse


parser = argparse.ArgumentParser()
# add mandatory (positional) arguments
parser.add_argument("fname",help="input srt file name")
parser.add_argument("offset",type=float,help="subtitle offset in seconds to apply (can be fractional)")

# parse arguments
args = parser.parse_args()

with open(args.fname,newline='') as ifp:	
	for line in ifp:
	           rexp = re.findall("(\d\d:\d\d:\d\d --> \d\d:\d\d:\d\d)", line)   //κανονικη εκφραση
		   m = rexp.search(line)
		
		if m is None: 
	            sys.stdout.write(line)
		
		
		else:
		    hours = int(m.group(1))   //Διαχωρισμος για  ωρες λεπτα δευτερολεπτα
		    min=int(m.group(2))
		    sec=int(m.group(3))
			
		    sum = hours*3600+min*60+sec+offset    //Προσθηκη offset
		    sys.stdout.write(sum)

