from  aes import *

def encryptor(text,password):
  text = str.encode(text)
  password = str.encode(password)
  crypt = encrypt(text,password)
  kdfSalt = crypt[0].decode()
  ciphertext = crypt[1].decode()
  nonce = crypt[2].decode()
  authTag = crypt[3].decode()
  returnstring = kdfSalt+":"+ciphertext+":"+nonce+":"+authTag
  return returnstring
  
def decryptor(ciphertext,password):
  ciphertextlist = list(ciphertext.split(":"))
  password = str.encode(password)
  kdfSalt = str.encode(ciphertextlist[0])
  ciphertext = str.encode(ciphertextlist[1])
  nonce = str.encode(ciphertextlist[2])
  authTag = str.encode(ciphertextlist[3])
  plaintext = decrypt([kdfSalt,ciphertext,nonce,authTag],password)
  return plaintext.decode()
  
