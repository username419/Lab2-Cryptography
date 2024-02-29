#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Frequency Finder
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

message = "hsle\u2019d sp esle htdspd dz? xj nzfdty hpdexzcpwlyo? yz, xj qltc nzfdty: tq hp lcp xlcv\u2019o ez otp, hp lcp pyzh ez oz zfc nzfyecj wzdd; lyo tq ez wtgp, esp qphpc xpy, esp rcplepc dslcp zq szyzfc. rzo\u2019d htww! t aclj espp, htds yze zyp xly xzcp. mj uzgp, t lx yze nzgpezfd qzc rzwo, yzc nlcp t hsz ozes qppo fazy xj nzde; te jplcyd xp yze tq xpy xj rlcxpyed hplc; dfns zfehlco estyrd ohpww yze ty xj opdtcpd: mfe tq te mp l dty ez nzgpe szyzfc, t lx esp xzde zqqpyotyr dzfw lwtgp. yz, qltes, xj nzk, htds yze l xly qczx pyrwlyo: rzo\u2019d aplnp! t hzfwo yze wzdp dz rcple ly szyzfc ld zyp xly xzcp, xpestyvd, hzfwo dslcp qczx xp qzc esp mpde szap t slgp. z, oz yze htds zyp xzcp! clespc acznwltx te, hpdexzcpwlyo, esczfrs xj szde, esle sp hstns sles yz dezxlns ez estd qtrse, wpe stx opalce; std alddazce dslww mp xlop lyo nczhyd qzc nzygzj afe tyez std afcdp: hp hzfwo yze otp ty esle xly\u2019d nzxalyj esle qplcd std qpwwzhdsta ez otp htes fd. estd olj td nlwwpo esp qplde zq nctdatly: sp esle zfewtgpd estd olj, lyo nzxpd dlqp szxp, htww delyo l eta-ezp hspy esp olj td ylxpo, lyo czfdp stx le esp ylxp zq nctdatly. sp esle dslww wtgp estd olj, lyo dpp zwo lrp, htww jplcwj zy esp gtrtw qplde std yptrsmzfcd, lyo dlj \u2018ez-xzcczh td dltye nctdatly:\u2019 espy htww sp decta std dwppgp lyo word9 std dnlcd. lyo dlj \u2018espdp hzfyod t slo zy nctdaty\u2019d olj.\u2019 zwo xpy qzcrpe: jpe lww dslww mp qzcrze, mfe sp\u2019ww cpxpxmpc htes loglyelrpd hsle qpled sp oto esle olj: espy dslww zfc ylxpd. qlxtwtlc ty std xzfes ld szfdpszwo hzcod slccj esp vtyr, mpoqzco lyo pipepc, hlchtnv lyo elwmze, dlwtdmfcj lyo rwzfnpdepc, mp ty esptc qwzhtyr nfad qcpdswj cpxpxmpc\u2019o. estd dezcj dslww esp rzzo xly eplns std dzy; lyo nctdaty nctdatly dslww yp\u2019pc rz mj, qczx estd olj ez esp pyotyr zq esp hzcwo, mfe hp ty te dslww mp cpxpxmpc\u2019o; hp qph, hp slaaj qph, hp mlyo zq mczespcd; qzc sp ez-olj esle dspod std mwzzo htes xp dslww mp xj mczespc; mp sp yp\u2019pc dz gtwp, estd olj dslww rpyewp std nzyotetzy: lyo rpyewpxpy ty pyrwlyo yzh l-mpo dslww estyv espxdpwgpd lnnfcdpo espj hpcp yze spcp, lyo szwo esptc xlyszzod nspla hstwpd lyj daplvd esle qzfrse htes fd fazy dltye nctdaty\u2019d olj."

def getLetterCount(message):
    #Returns a dictionary with keys of single letters and values of the
    #count of how many times they appear in the message parameter:
    letterCount = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
    
    for letter in message.upper():
        if letter in LETTERS:
            letterCount[letter] += 1
    return letterCount

def getItemAtIndexZero(items):
    return items[0]

def getFrequencyOrder(message):
    #Returns a string of the alphabet letters arranged in order of most
    #frequently occurring in the message parameter.
    
    #First, get a dictionary of each letter and its frequency count:
    letterToFreq = getLetterCount(message)
    freqToLetter = {}
    
    #Second, make a dictionary of each frequency count to each letter(s)
    #with that frequency:
    for letter in LETTERS:
        if letterToFreq[letter] not in freqToLetter:
            freqToLetter[letterToFreq[letter]] = [letter]
        else:
            freqToLetter[letterToFreq[letter]].append(letter)
    
    #Third, put each list of letter in reverse "ETAOIN" order, and then
    #convert it to a string:
    for freq in freqToLetter:
        freqToLetter[freq].sort(key=ETAOIN.find, reverse=True)
        freqToLetter[freq] = ''.join(freqToLetter[freq])
    
    #Fourth, convert the freqToLetter dictionary to a list of
    #tuple pairs (key, value), then sort them:
    freqPairs = list(freqToLetter.items())
    freqPairs.sort(key=getItemAtIndexZero, reverse=True)
    
    #Fifth, now that the letters are ordered by frequency, extract all
    #the letters for the final string:
    freqOrder = []
    for freqPair in freqPairs:
        freqOrder.append(freqPair[1])
    
    return ''.join(freqOrder)

def englishFreqMatchScore(message):
    #Return the number of matches that the string in the message
    #parameter has when its letter frequency is compared to English
    #letter frequency. A "match" is how many of its six most frequent
    #and six least frequent letters is among the six most frequent and
    #six least frequent letters for English.
    freqOrder = getFrequencyOrder(message)
    
    matchScore = 0
    #Find how many matches for the six most common letters there are:
    for commonLetter in ETAOIN[:6]:
        if commonLetter in freqOrder[:6]:
            matchScore += 1
    #Find how many matches for the six least common letters there are:
    for uncommonLetter in ETAOIN[-6:]:
        if uncommonLetter in freqOrder[-6:]:
            matchScore += 1
    return matchScore


# In[10]:


getLetterCount(message)


# In[11]:


getFrequencyOrder(message)


# In[12]:


englishFreqMatchScore(message)


# In[ ]:




