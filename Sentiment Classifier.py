projectTwitterDataFile = open("project_twitter_data.csv", "r")
resultingDataFile = open("resulting_data.csv", "w")

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(word):
    new_word = ""
    for ch in word:
        if ch in punctuation_chars:
            new_word += ""
        else:
            new_word += ch
    return new_word        

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
            
def get_pos(sentence):
    reqd_sentence = strip_punctuation(sentence)
    count = 0
    for word in reqd_sentence.split():
        if word in positive_words:
            count += 1
    return count        
            


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
def get_neg(sentence):
    reqd_sentence = strip_punctuation(sentence)
    count = 0
    for word  in reqd_sentence.split():
        if word in negative_words:
            count += 1
    return count        

def writeDataFile(resultingDataFile):
    resultingDataFile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    resultingDataFile.write("\n")
    
    linesPTDF = projectTwitterDataFile.readlines()
    headerNotUsed = linesPTDF.pop(0)
    for linesTD in linesPTDF:
        listTD = linesTD.strip().split(",")
        resultingDataFile.write("{},{},{},{},{}".format(listTD[1],listTD[2],get_pos(listTD[0]),get_neg(listTD[0]),(get_pos(listTD[0]) - get_neg(listTD[0]))))
        resultingDataFile.write("\n")
        
writeDataFile(resultingDataFile)
projectTwitterDataFile.close()
resultingDataFile.close()
                                

