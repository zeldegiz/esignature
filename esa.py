import rsa
def signing(hashvalue,privatesign):
  e = privatesign[0]
  n = privatesign[1]
  return rsa.encrypt(hashvalue,(e,n))
  
def signcheck(hashvalue,signhashvalue,publicsign):
  d = publicsign[0]
  n = publicsign[1]
  if(hashvalue==rsa.decrypt(signhashvalue,(d,n))):
    return True
  else:
    return False