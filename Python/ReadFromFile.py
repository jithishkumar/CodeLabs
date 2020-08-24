path = 'Text File with some texts in it'
dicti = {}
bigC = None
bigW = None

try:
    reader = open(path,'r')
except:
    print("file not found in the given directory")
    quit()
###For creating a dictionary and finding the most commonly used word and its occurance
for lines in reader:
    #print(lines.strip())
    words = lines.split()
    #print(words)
    for word in words:
        dicti[word] = dicti.get(word,0)+1
print(dicti)


for (val,key) in list(dicti.items()):
    if bigC is None or key > bigC:
        bigW = val
        bigC = key 
print(bigW, bigC)


### With method which creates instance and deletes it once completed
#From a given file, finds the character and and retruns a list of words
list_Conf = []

with open('Text File') as f:
    for lines in f:
        if lines.startswith('Starting letter or word you want to find'):
            Conf = lines.split(':')
            list_Conf.append(float(Conf[1].strip()))
print(list_Conf)

#Sorts the list

with open('D:\Learning\Python\Sample.txt') as f:
    for lines in f:
        for word in lines.split():
            if word in list_Conf:
                continue
            list_Conf.append(word)
print(sorted(list_Conf))

