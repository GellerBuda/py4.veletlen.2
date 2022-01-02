'''
2. Feladat
A program a pénzfeldobást modellezi. Kérdezze meg a felhasználótól a választását (fej vagy írás), majd adjon tájékoztatást, hogy eltalálta-e!
'''
kérdés = input('Fej vagy írás? ')
fej = 1
írás = 2

import random
random_érme = random.randint(1,2)

if random_érme == fej :
  print ('Talált')
elif random_érme != fej :
  print ('Nem talált')

elif random_érme == írás :
  print ('Talált')
elif random_érme != írás :
  print ('Nem talált')