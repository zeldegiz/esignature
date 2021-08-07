import rsa
def generator():
  e,n,d = rsa.generator(1024)
  privatesign = [e,n]
  publicsign = [d,n]
  return (privatesign,publicsign)
  