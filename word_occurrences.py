sentence={}
for word in input("Text:").split():
    if word in sentence:
        sentence[word]+=1
    else:
        sentence[word]=1
n=max(len(word) for word in sentence)
for key,value in sorted(sentence.items()):
    print("{:<{}}{}".format((key+':'),n,value))
