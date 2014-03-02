from __future__ import division
import nltk, re, pprint
from nltk import bigrams
import urllib,urllib2
import copy
from nltk.collocations import *
from nltk.tokenize import word_tokenize
import nltk.data
import urllib
import json
from math import log


list=[]
newlist=[]
newlist1=[]
ct=0

def hits(word1,word2=""):
    query = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=%s"
    if word2 == "":
        results = urllib.urlopen(query % word1)
    else:
        results = urllib.urlopen(query % word1+" "+"AROUND(10)"+" "+word2)
    json_res = json.loads(results.read())
    google_hits=int(json_res['responseData']['cursor']['estimatedResultCount'])
    return google_hits


def so(phrase):
    num = hits(phrase,"excellent")
    #print num
    den = hits(phrase,"poor")
    #print den
    ratio = num / den
    #print ratio
    sop = log(ratio)
    return sop

def check(newl,spl1):
    print newl
    print spl1
    for k in range(0,len(newl)):
        if(k!=len(newl)-1):
            if( newl[k]=="JJ" and newl[k+1]=="JJ" and newl[k+2]!="NN" and newl[k+2]!="NNS"):
                return "".join(spl1[k])+" "+"".join(spl1[k+1])
            if( newl[k]=="JJ" and newl[k+1]=="NN" ) or ( newl[k]=="JJ" and newl[k+1]=="NNS" ):
                return "".join(spl1[k])+" "+"".join(spl1[k+1])
            if( newl[k]=="RB" and newl[k+1]=="VB" ) or ( newl[k]=="RB" and newl[k+1]=="VBD" ) or ( newl[k]=="RB" and newl[k+1]=="VBN" ) or ( newl[k]=="RB" and newl[k+1]=="VBG" ) or ( newl[k]=="RBR" and newl[k+1]=="VB" ) or ( newl[k]=="RBR" and newl[k+1]=="VBD" )or ( newl[k]=="RBR" and newl[k+1]=="VBN" )or ( newl[k]=="RBR" and newl[k+1]=="VBG" )or ( newl[k]=="RBS" and newl[k+1]=="VB" )or ( newl[k]=="RBS" and newl[k+1]=="VBD" )or ( newl[k]=="RBS" and newl[k+1]=="VBN" )or ( newl[k]=="RBS" and newl[k+1]=="VBG" ):
                return "".join(spl1[k])+" "+"".join(spl1[k+1])
            if( newl[k]=="NN" and newl[k+1]=="JJ" and newl[k+2]!="NN" and newl[k+2]!="NNS") or ( newl[k]=="NNS" and newl[k+1]=="JJ" and newl[k+2]!="NN" and newl[k+2]!="NNS"):
                return "".join(spl1[k])+" "+"".join(spl1[k+1])
            if( newl[k]=="RB" and newl[k+1]=="JJ" and newl[k+2]!="NN" and newl[k+2]!="NNS") or ( newl[k]=="RBR" and newl[k+1]=="JJ" and newl[k+2]!="NN" and newl[k+2]!="NNS") or ( newl[k]=="RBS" and newl[k+1]=="JJ" and newl[k+2]!="NN" and newl[k+2]!="NNS"):
                return "".join(spl1[k])+" "+"".join(spl1[k+1])

def text_pos(raw):
    global list,newlist,newlist1,ct
    print "raw input:",raw
    spl=raw.split()
    print "\n"
    print "split version of input:",spl
    pos=nltk.pos_tag(spl)
    print "\n"
    print "POS tagged text:",""
    for iter in pos:
        print iter,""
    for i in range(0,len(pos)):
        if(i!=len(pos)-1):
            list.append(pos[i])
            list.append(pos[i+1])
            t1 = list[0]
            t2 = list[1]
            newlist.append(t1[1])
            newlist.append(t2[1])
            list=[]
    print "\n"
    print "Extracting the tags alone:",""
    print newlist
    for j in range(0,len(newlist)):
        if((j%2!=0) and (j!=len(newlist)-1)):
            newlist[j]=0
            
    newlist = [x for x in newlist if x != 0]
    print "Checking whether the tags conform to the required pattern..."
    print "\n"
    print spl
    print newlist
    print "The extracted two-word phrases which satisfy the required pattern are:"
    strr1=check(newlist,spl)
    return strr1

print "PMI - Pointwise Mutual Information"
print "\n"
strr = text_pos("Nokia is a amazing phone")
print strr
x = so(strr)
print x

