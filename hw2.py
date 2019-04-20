# -*- coding: UTF-8 -*-
import nltk
import matplotlib
matplotlib.use('agg')
from nltk.book import *
import matplotlib.pyplot as plt
import numpy
g = open('/home/coyote/METU/4th Semester Thesis/Human factor in Cyber Physical systems/HW2/my codes/hackers2.txt')
graw = g.read()

f = open('/home/coyote/METU/4th Semester Thesis/Human factor in Cyber Physical systems/HW2/my codes/my55.txt')
fraw = f.read()

tokens = nltk.wordpunct_tokenize(graw)
tokens = tokens [1:]
hackers2 = nltk.Text(tokens)

tokens = nltk.wordpunct_tokenize(fraw)
tokens = tokens [1:]
my55 = nltk.Text(tokens)
'''
words = [w.lower() for w in my55]
vocab = sorted(set(words))
'''
##############
fdist1 = FreqDist(hackers2)
fp_list = ['i', 'mine', 'we', 'me', 'my', 'i’m', 'i’ll', 'i’ve', 'i’d', 'myself', 'our ours', 'ourselves']
exc_list = ['except', 'however', 'but', 'although', 'rather', 'unless', 'whereas', 'nor', 'without', 'besides', 'nonetheless']

print ("=====First-Person Words for hackers book ==========")

for word in fp_list:
	print((word),fdist1[(word)],"freq:",fdist1.freq(word))
	
print ("=====Exception Words for hackers book =============")
	
for word in exc_list:
	print((word),fdist1[(word)],"freq:",fdist1.freq(word))

#########

fdist2 = FreqDist(my55)
fp_list = ['i', 'mine', 'we', 'me', 'my', 'i’m', 'i’ll', 'i’ve', 'i’d', 'myself', 'our ours', 'ourselves']
exc_list = ['except', 'however', 'but', 'although', 'rather', 'unless', 'whereas', 'nor', 'without', 'besides', 'nonetheless']

print ("=====First-Person Words for reddit comments ==========")

for word in fp_list:
	print((word),fdist2[(word)],"freq:",fdist2.freq(word))
	
	
print ("=====Exception Words for reddit comments =============")
	
for word in exc_list:
	print((word),fdist2[(word)],"freq:",fdist2.freq(word))
	
	
print("word count of formal source is : ",len(hackers2),"\n")
print("word count of unformal source is: ",len(my55))

fdist1.plot()
fdist2.plot()
