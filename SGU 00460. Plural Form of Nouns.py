# ITNOA
t=int(input())
while t:
   t-=1
   s=input()
   n=len(s)
   if n>=2 and s[-2:]=='ch' or s[-1] in 'xso':
      print(s+'es')
   elif n>=2 and s[-2:]=='fe':
      print(s[:-2]+'ves')
   elif s[-1]=='f':
      print(s[:-1]+'ves')
   elif s[-1]=='y':
      print(s[:-1]+'ies')
   else:
      print(s+'s')
