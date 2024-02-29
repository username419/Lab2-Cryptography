import requests
import csv

targetGroup = 2 #A=1, B=2, C=3              ~~~~~~TO TEST~~~~~~~ input 1, 2, or 3 and ensure the IP addresses are up to date
teamAIP = "35.89.191.113:9090"
teamBIP = "35.86.110.53:12345"
teamCIP = "54.201.228.71:12345"

cipherIt = 0                                # no touch

if targetGroup == 1:                        # sets variables up for target group's server
    ourIP = teamAIP
    ourFile = "TeamA.csv"
elif targetGroup == 2:
    ourIP = teamBIP
    ourFile = "TeamB.csv"
elif targetGroup == 3:
    ourIP = teamCIP
    ourFile = "TeamC.csv"


# this is a brute force attack that writes to CSV file
# will obtain result from API for every ascii character
# pass an int as a parameter to save repeat sequences to look for homophonic characters
# ie 0 -> a, 2 -> aa, 5 -> aaaaa
def determine_indexer(iterations):
    for i in range(26):
        i += 97                             #the loop from 0-26 and +97 puts this in the ascii range of "a" through "z"
        cipher = hitAPI(chr(i), 0, ourIP)
        if iterations > 1:                  # if searching for homophonic characters, effectively against our codebook but not others.
            cipherIt = hitAPI(chr(i)*iterations, 0, ourIP)
        writeToCSV(chr(i), cipher, cipherIt)


# repeatedly encodes the encoded result of a passed string, breaks after 58 passes or if the repeatedly
# encoded message returns to the original, passed string
def findExplicitString(name):
    newIt = name
    for i in range(58):
        newIt = hitAPI(newIt, 0, ourIP)
        print(newIt)
        if newIt == name:
            return i


# this code hits the target's API, parameters:
# {string to encode/decode}
# {0=encode, 1 = decode}
# {IP address of target as string}
def hitAPI(ele, code, target):
    if code == 0:               #determines encode or decode
        to_code = "encode"
    elif code == 1:
        to_code = "decode"
    else:
        return "Invalid"

    passedPhrase = "http://" + target + "/" + to_code + "?text=" + str(ele)         #actually builds the URL string
    response = requests.get(passedPhrase)                                           #hits

    # each of the following groups implemented encode/decode return values slightly differently. This accounts for it.
    if targetGroup == 1:
        if code == 0:
            substrings = (str(response.json()).split(",")[2]).split("'")[3]  # divies up return value to only get what we want
        elif code == 1:  # need if/else because of formatting, check other projects
            substrings = (str(response.json()).split(",")[2]).split("'")[3]
    elif targetGroup == 2:
        if code == 0:
            substrings = (str(response.json()).split(",")[0]).split("'")[3]  # divies up return value to only get what we want
        elif code == 1:  # need if/else because of formatting, check other projects
            substrings = (str(response.json()).split(",")[2]).split("'")[3]
    elif targetGroup == 3:
        if code == 0:
            substrings = (str(response.json()).split(",")[0]).split("'")[
                3]  # divies up return value to only get what we want
        elif code == 1:  # need if/else because of formatting, check other projects
            substrings = (str(response.json()).split(",")[2]).split("'")[3]

    print(response.json())
    print(ele + "\t" + substrings)                                                  #unnecessary print to console
    return substrings


# simple function to see what all ascii inputs will return an output
def allChar():
    for i in range(255):
        print(chr(i) + "\t" + hitAPI(i,0,ourIP))


# writes to a csv file so we can analyze it better
# 'private' class, doesn't really need user input
def writeToCSV(ele, ele2, ele3):
    with open(ourFile, 'a', encoding='UTF8', newline='') as g:   #sets up a file in append mode ('a'), configure name up top for each group
        writer = csv.writer(g, escapechar="\\")                         # i do not know why it needs 'escapechar="\\", just keep it
        # write the header
        writer.writerow([ele, ele2, ele3])                                    #actually appends in two columns plaintext|ciphertext


# this code created the original files and set them up, but keep commented so it doesn't erase all of the data. again.
# header = ['Plaintext', 'CipherText', 'MultiMono']                                    # just sets up the initial file we want
# with open(ourFile, 'w', encoding='UTF8', newline='') as f:       # this functionally resets the CSV every time this code is run, take care
#    writer = csv.writer(f)
#    # write the header
#    writer.writerow(header)


# various tests of the above code.
# hitAPI("abcd", 0, ourIP)          # demonstration of a single encode against targeted team
# hitAPI("sljopy", 1, ourIP)        # demonstration of a single decode against targeted team
                                    # next line is a longer text for frequency analysis.
# hitAPI("The Industrial Revolution and its consequences have been a disaster for the human race. They have greatly increased the life-expectancy of those of us who live in “advanced” countries, but they have destabilized society, have made life unfulfilling, have subjected human beings to indignities, have led to widespread psychological suffering (in the Third World to physical suffering as well) and have inflicted severe damage on the natural world. The continued development of technology will worsen the situation. It will certainly subject human beings to greater indignities and inflict greater damage on the natural world, it will probably lead to greater social disruption and psychological suffering, and it may lead to increased physical suffering even in “advanced” countries.", 0, ourIP)
# print(findExplicitString("hayden"))       # demonstration of repeated encoding results
# determine_indexer(2)                      # Checks all letters and their repeats (aaaaa...) and writes out to a csv file.


