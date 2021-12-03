question1. thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
perform sorting without use sort()
{use this sample code:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
for i in range (len(thislist)):
  f=thislist[i]
  p=str(f)
  comp1=ord(p[0])
  for j in range(i+1,len(thislist)):
    s=thislist[j]
    q=str(s)
    comp2=ord(q[0])
    ####### need to do compare b/n comp1 comp2
    if comp1>comp2:
      thislist[i]=s
      thislist[j]=f

print(thislist)}