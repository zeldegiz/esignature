from esa import signing , signcheck
from file_module import hashgenerator , string2int , filelister , filereader , filewriter
from sign_generator import generator
import datetime
from Color_Console import *
from aes_module import *
from getpass import getpass
ctext("------------------Electronic Signature System for AzTu Master------------------","white","blue")
print("1 . Signature Generation")
print("2 . Signing")
print("3 . Sign Verification")
x0 = input("Please Select : ")

if(x0=="1"):
  print("------------------Signature Generation------------------")
  name = input("Please Enter Your Name : ")
  password = getpass('Please Enter Your Password :')
  date = str(datetime.datetime.now())
  privatesign , publicsign = generator()
  namehash = string2int(hashgenerator(name,1))
  passwordhash = str(string2int(hashgenerator(password,1)))
  namesign = signing(namehash,privatesign)
  privatekeyname = "generated_keys/private_"+hashgenerator(date,1)+".key"
  publickeyname = "generated_keys/public_"+hashgenerator(date,1)+".key"
  filewriter(privatekeyname,[name,encryptor(str(privatesign[0]),password),encryptor(str(privatesign[1]),password),passwordhash,str(namesign)])
  filewriter(publickeyname,[name,str(namesign),str(publicsign[0]),str(publicsign[1])])

if(x0=="2"):
  print("------------------Signing------------------")
  print("1 . Text Signing")
  print("2 . File Signing")
  x1=input("Please Select : ")
  if(x1 == "1"):
    txt = input("Enter Your Text : ")
  elif(x1 == "2"):
    txt = input("Enter Your File Location : ")
  print("------------------Please Select Private Sign------------------")
  keylist = filelister("generated_keys","private")
  x2 = input("Select Private Key : ")
  filename = keylist[int(x2)-1]
  password = getpass('Please Enter Your Password :')
  private_keys = filereader(filename)
  date = str(datetime.datetime.now())
  name = private_keys[0][:-1]
  passwordhash = private_keys[-2][:-1]
  namesign = private_keys[-1][:-1]
  
  if(str(string2int(hashgenerator(password,1)))!=passwordhash):
    print("Password Incorrect")
  else:
    privatekeys = [int(decryptor(private_keys[1][:-1],password)),int(decryptor(private_keys[2][:-1],password))]
    namehash = string2int(hashgenerator(name,1))
    datehash = string2int(hashgenerator(date,1))
    namesign = signing(namehash,privatekeys)
    datesign = signing(datehash,privatekeys)
    txtfilehash = string2int(hashgenerator(txt,int(x1)))
    txtfilesign = signing(txtfilehash,privatekeys)
    signlocation = "signs/sign_"+hashgenerator(date,1)+".sign"
    filewriter(signlocation,[date,str(datesign),str(txtfilesign)])

if(x0=="3"):
  print("------------------Sign Verification------------------")
  print("1 . Text Sign Verification")
  print("2 . File Sign Verification")
  x1=input("Please Select : ")
  if(x1 == "1"):
    txt = input("Enter Your Text : ")
  elif(x1 == "2"):
    txt = input("Enter Your File Location : ")
  print("------------------Please Select Public Sign------------------")
  txtfilehash = string2int(hashgenerator(txt,int(x1)))
  signlocation = input("Please Enter Sign File Location : ")
  signature = filereader(signlocation)
  keylist = filelister("public_keys","public")
  x2 = input("Select Public Key : ")
  filename = keylist[int(x2)-1]
  public_keys = filereader(filename)
  signdate = signature[0]
  signdatesign = signature[1]
  signtxtfilesign = signature[2]
  publicname = public_keys[0]
  publicnamesign = public_keys[1]
  publicsign = [int(public_keys[2]),int(public_keys[3])]
  ctext("Please wait for Public Sign Verification","white","blue")
  rt = 0
  if(signcheck(string2int(hashgenerator(publicname[:-1],1)),int(publicnamesign[:-1]),publicsign)):
    ctext("Public Sign Verified","white","green")
    rt = rt+1
  else:
    ctext("Public Sign NOT Verified","white","red")
  ctext("Please wait for Signature Date Verification","white","blue")
  if(signcheck(string2int(hashgenerator(signdate[:-1],1)),int(signdatesign[:-1]),publicsign)):
    ctext("Sign Date Verified","white","green")
    rt = rt+1
  else:
    ctext("Sign Date NOT Verified","white","red")
  ctext("Please wait for Text/File Verification","white","blue")
  if(signcheck(txtfilehash,int(signtxtfilesign[:-1]),publicsign)):
    ctext("Text/File Verified","white","green")
    rt = rt+1
  else:
    ctext("Text/File NOT Verified","white","red")
  print("------------------Conclusion------------------")
  if(rt == 3):
    ctext("This Text/File Signed by "+publicname[:-1]+" and Signed  Date is "+signdate[:-1],"white","green")
  else:
    ctext("This Signature or Public Sign is incorrect . Please Check from above","white","red")