import dotnessus_v2
import sys, os


if (len(sys.argv) > 0):
 nessinput = sys.argv[1] 
 if (os.path.isfile(nessinput)):
   pass
 else:
   print("That doesn't look like a file")
   sys.exit()
else:
 print("You need to supply a nessus file as input")

rpt = dotnessus_v2.Report()
rpt.parse(nessinput)

output = []

for t in rpt.targets:
  openports = "" 
  ports = t.get_open_ports()
  try:
    tcp = ports['tcp']
    openports = ",".join(tcp)
  except:
    pass
  
  print('%s\t%s\t%s' % (t.get_scanned_ip(), t.get('host-fqdn'), openports))
