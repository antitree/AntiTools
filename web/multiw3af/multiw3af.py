#!/usr/bin/python
#author: antitree
#Description: script to automate the scanning of w3af against
# a supplied list of urls

from optparse import OptionParser
import subprocess
import re
import sys
import time

def main():
  parser = OptionParser(usage="%prog -i listofurls \
-s pathtoscript.w3af [-o outputnames]", version="%prog 0.1")

  parser.add_option("-i", dest="urls", action="store",
    help="list of URLs on separate lines (https://bla/")
  parser.add_option("-s", dest="w3afscript", action="store",
    help="path to w3af script with options in it")
  (options, args) = parser.parse_args()

  #process input urls
  if options.urls:
    try: 
      #open file and put into a list
      f = open(options.urls, 'r')
      urls = f.readlines()
      f.close()
    except:
      parser.error("Invalid input file")
  else:
    parser.error("Need a list of urls")
 
  #process input script
  if options.w3afscript:
    try:
      f = open(options.w3afscript, 'r')
      w3script = f.readlines()
      f.close()
    except:
      parser.error("Invalid w3af script")
  else:
    parser.error("Need a script to use for automation")

  autoscripts = []
  for url in urls:
    autoscripts.append(fixScript(w3script, url))
    #print warning
  print("WARNING: You are about to run scan on the following URLs")
  for url in urls:
    print("   "+url.strip('\n'))
  engage = raw_input("Are you prepared? Type engage if so:")
  if not engage.lower() == "engage":
    print("You are weak! Have a nice day.")
    sys.exit()
  

  for script in autoscripts:
    try:
      p = subprocess.Popen(('./w3af_console', 
      '-s', script, '-n'))
      p.wait()
    except OSError:
      print("W3af not found. Make sure you're running this inside the w3af dir")
      sys.exit()
     
    
def fixScript(script, url):
  #parse input script
  #search for target and replace with line input

  #strip url
  name = url.partition('/')[2][1:].strip()

 
  #set target
  for line in script:
    #find target selection
    found = re.search("set target.+", line)
    if found:
      index = script.index(line)
      script[index] = "set target %s\n" % url
      print("generated custom target for %s" % url)
    
    #find text output names
    found = re.search("set fileName.+txt$", line)
    if found:
      index = script.index(line)
      script[index] = "set fileName %s.txt\n" % name
    
    #find xml output names
    found = re.search("set fileName.+xml$", line)
    if found:
      index = script.index(line)
      script[index] = "set fileName %s.xml\n" % name
    
    #find html output names
    found = re.search("set fileName.+html$", line)
    if found:
      index = script.index(line)
      script[index] = "set fileName %s.html\n" % name

  #rewrite scripts
  filename = name + ".w3af"
  f = open(filename, 'w')
  f.writelines(script)
  f.close()
  return filename 


if __name__ == "__main__":
  main()
