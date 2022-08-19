import re
'''f=open("tweets.txt",'r')
o=open("preprocessedtweet.txt",'a')

vocab=[]

for line in f:
	x=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(RT)"," ",line).split())
	x=x.lower()
	o.write(x)
	o.write("\n")
'''
o=open("preprocessedtweet.txt","r")
s=o.read().split()

vocab=set(s)
print(vocab)

vo=open("vocab.txt",'a')
for i in vocab:
	vo.write(i)
	vo.write("\n")
