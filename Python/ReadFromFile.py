path = 'Text File with some texts in it'
dicti = {}
bigC = None
bigW = None

try:
    reader = open(path,'r')
except:
    print("file not found in the given directory")
    quit()

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
