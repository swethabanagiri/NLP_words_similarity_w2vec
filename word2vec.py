# -*- coding: utf-8 -*-
"""
Created on Sat Sep 03 11:24:55 2016

@author: Sai
"""
import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter
import math

#Short girl's code goes here 

#Count for one, two and three words

f1 = open("preprocessedtweet.txt","r")

#print f2.read()
vocabulary_uni = {}

vocab = 0.0
for word in f1:
    s = word.split(' ')
    for words in s:
    	tup_one = (words,)
    	if tup_one in vocabulary_uni:
        	vocabulary_uni[tup_one]+=1
        else:
        	vocabulary_uni[tup_one]=1
        vocab = vocab + 1

#print vocabulary_uni        
for word in vocabulary_uni:
    vocabulary_uni[word] = vocabulary_uni[word]/vocab
#print vocabulary_uni    

f3 = open("preprocessedtweet.txt","r")
vocabulary_bi = {}
for word in f3:
	s = word.split(' ')
	for i in range(len(s)-1):
		tup_two = (s[i], s[i+1])
		if tup_two in vocabulary_bi:
			vocabulary_bi[tup_two] +=1
		else:
			vocabulary_bi[tup_two]=1

     
for word in vocabulary_bi:
	if (word[0],) in vocabulary_uni:
		vocabulary_bi[word]= vocabulary_bi[word]/(vocabulary_uni[(word[0],)] * vocab)      
	else:
		print "bleh"

f3 = open("preprocessedtweet.txt","r")
vocabulary_tri = {}
for word in f3:
	s = word.split(' ')
	for i in range(len(s)-2):
		tup_tri = (s[i], s[i+1],s[i+2])
		if tup_tri in vocabulary_tri:
			vocabulary_tri[tup_tri] +=1
		else:
			vocabulary_tri[tup_tri]=1
vocabulary_tri_prob = {}
for word in vocabulary_tri:
	if (word[0],word[1]) in vocabulary_bi:
		vocabulary_tri_prob[word]= vocabulary_tri[word]/(vocabulary_bi[(word[0],word[1])] * vocabulary_uni[(word[0],)] * vocab)      
	else:
		print "bleh"
#print vocabulary_tri
word_pairs = [('modi','minister'), ('chaturvedi','modi'),('power','know')]

pair_count = {}
Z =0.0
D = 0.0

for pair in word_pairs:
	s1 = pair[0]
	s2 = pair[1]
	for tri in vocabulary_tri:
		if s1==tri[1]:
			left = tri[0]
			right = tri[2]
			#print left
			tup = tri
			for sec in vocabulary_tri:
				if s2==sec[1] and left==sec[0] and right==sec[2]:
					Z = Z+vocabulary_tri[tup]+vocabulary_tri[sec]
					d = abs(vocabulary_tri[tup] - vocabulary_tri[sec])
					#print vocabulary_tri[tup],vocabulary_tri[sec]
					D = D+d
	#print Z,D
	print "Score = ",str(1-D/Z)
