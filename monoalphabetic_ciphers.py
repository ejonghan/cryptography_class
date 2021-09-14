def additive(plain_message):
  e = ""
  for c in plain_message:
    n = s.find(c)
    n = (n + 20) % 26
    e = e + s[n]
  print(e)

def de_additive(plain_message):
  e = ""
  for c in plain_message:
    n = s.find(c)
    n = (n - 20) % 26
    e = e + s[n]
  print(e)

def multiplicative(plain_message):
    e = ""
    for c in plain_message:
        n = s.find(c)
        n = (n * 15) % 26
        e = e + s[n]
    print(e)

def de_multiplicative(plain_message):
    e = ""
    for c in plain_message:
        n = s.find(c)
        n = (n * 7) % 26
        e = e + s[n]
    print(e)
    
def affine(plain_message):
    e = ""
    for c in plain_message:
        n = s.find(c)
        n = (n * 15 + 20) % 26
        e = e + s[n]
    print(e)

def de_affine(plain_message):
    e = ""
    for c in plain_message:
        n = s.find(c)
        n = ((n - 20) * 7) % 26
        e = e + s[n]
    print(e)