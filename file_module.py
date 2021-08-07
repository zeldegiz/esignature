import hashlib
import os
def hashgenerator(s,i):
  if(i==1):
    file_hash = hashlib.sha256()
    file_hash.update(s.encode("utf-8"))
    return file_hash.hexdigest()
  elif(i==2):
    file_hash = hashlib.sha256()
    BLOCK_SIZE = 65536
    with open(s, 'rb') as f:
      fb = f.read(BLOCK_SIZE)
      while len(fb) > 0:
        file_hash.update(fb)
        fb = f.read(BLOCK_SIZE)
    return file_hash.hexdigest()
    
def string2int(s):
  m=""
  for i in s:
    if(ord(i)<100):
      m=m+"0"+str(ord(i))
    else:
      m=m+str(ord(i))
    m = "1"+m
  return int(m)
  
def filelister(folderlocation,prefix):
  filenames=[]
  i=1
  for root, dirs, files in os.walk(folderlocation,):
    for j in files :
      if(prefix in j):
        filenames.append(folderlocation+"/"+j)
        prf = open(folderlocation+"/"+j)
        first_line = prf.readline()
        print(str(i)+" . "+first_line,end = '')
        i+=1
  return filenames
  
def filereader(filelocation):
  prf = open(filelocation)
  file = prf.readlines()
  prf.close()
  return file
  
def filewriter(filelocation,data):
  f= open(filelocation,"w+")
  for i in data:
    f.write(i+"\n")
  f.close()
