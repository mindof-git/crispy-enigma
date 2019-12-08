import io
text=""
def openfile(f_name):
    file=open(f_name,mode='r',encoding='utf-8')
    return file

def writefile(f_name):
    file=open(f_name,mode='w',encoding='utf-8')
    return file

def printLine(file):
    for line in file:
        print(line)


def checkSentiment(text,kword):
    flag=False
    for key in kword:
        if key in text:
            flag=True
            return flag
        else:
            flag=False
            continue
    return flag

            
#please insert the files in the folder to this place
negative=openfile("C:/Users/UX/Desktop/dtac/negative.txt")
positive=openfile("C:/Users/UX/Desktop/dtac/positive.txt")
neutral=openfile("C:/Users/UX/Desktop/dtac/Neutral.txt")
network=openfile("C:/Users/UX/Desktop/dtac/network.txt")
product=openfile("C:/Users/UX/Desktop/dtac/product.txt")
billing=openfile("C:/Users/UX/Desktop/dtac/billing.txt")
topup=openfile("C:/Users/UX/Desktop/dtac/Topup.txt")
customer=openfile("C:/Users/UX/Desktop/dtac/customerservice.txt")
device=openfile("C:/Users/UX/Desktop/dtac/device.txt")

def keylist1(file):
    klist1=[]
    for word in file:
        if "\n" in word:
            word=word.replace("\n","")
##        if "\u" in word:
##            ind=word.index("\u")
##            word=word.replace(word[ind:ind+6],"")
        if "\t" in word:
            word=word.replace("\t","")
        if word!="" and word!=" ":
            klist1.append(word)
    return klist1



neg=keylist1(negative)
pos=keylist1(positive)
nw=keylist1(network)
pro=keylist1(product)
bill=keylist1(billing)
top=keylist1(topup)
cs=keylist1(customer)
dev=keylist1(device)


def forProduct(text,pro,pos,neg):
    if checkSentiment(text,pro):
        if checkSentiment(text,neg):
            sentiFil.write(text+"*|Product|**|Negative|*")
        else:
            if checkSentiment(text,pos):
                sentiFil.write(text+"*|Product|**|Positive|*")
            else:
                sentiFil.write(text+"*|Product|**|Neutral|*")
    else:
        sentiFil.write(text+"*|Product|**|Unrelated|*")

def forNetwork(text,nw,pos,neg):
    if checkSentiment(text,nw):
        if checkSentiment(text,neg):
            sentiFil.write(text+"*|Network|**|Negative|*")
        else:
            if checkSentiment(text,pos):
                sentiFil.write(text+"*|Network|**|Positive|*")
            else:
                sentiFil.write(text+"*|Network|**|Neutral|*")
    else:
        sentiFil.write(text+"*|Network|**|Unrelated|*")
def forBilling(text,bill,pos,neg) :
    if checkSentiment(text,bill):
        if checkSentiment(text,neg):
            sentiFil.write(text+"*|Billing|**|Negative|*")
        else:
            if checkSentiment(text,pos):
                sentiFil.write(text+"*|Billing|**|Positive|*")
            else:
                sentiFil.write(text+"*|Billing|**|Neutral|*")
    else:
        sentiFil.write(text+"*|Billing|**|Unrelated|*")
def forTopup(text,top,pos,neg):
    if checkSentiment(text,top):
        if checkSentiment(text,neg):
            sentiFil.write(text+"*|TopUp|**|Negative|*")
        else:
            if checkSentiment(text,pos):
                sentiFil.write(text+"*|TopUp|**|Positive|*")
            else:
                sentiFil.write(text+"*|TopUp|**|Neutral|*")
    else:
        sentiFil.write(text+"*|TopUp|**|Unrelated|*")
def forDevice(text,dev,pos,neg):
    if checkSentiment(text,dev):
        if checkSentiment(text,neg):
            sentiFil.write(text+"*|Device|**|Negative|*")
        else:
            if checkSentiment(text,pos):
                sentiFil.write(text+"*|Device|**Positive||*")
            else:
                sentiFil.write(text+"*|Device|**|Neutral|*")
    else:
        sentiFil.write(text+"*|Device|**|Unrelated|*")
def forCS(text,cs,pos,neg):
    if checkSentiment(text,cs):
        if checkSentiment(text,neg):
            sentiFil.write(text+"*|CustomerService|**|Negative|*")
        else:
            if checkSentiment(text,pos):
                sentiFil.write(text+"*|CustomerService|**Positive||*")
            else:
                sentiFil.write(text+"*|CustomerService|**|Neutral|*")
    else:
        sentiFil.write(text+"*|CustomerService|**|Unrelated|*")
    


#insert file that you want to sentiment
filename=openfile("C:/Users/UX/Downloads/DTACCAMBODIA/DTACCAMBODIA/archive/DTACCAMBODIA_2017-07-04_feed_0.txt")
#save the finished file into location that you want to 
with io.open("C:/Users/UX/Downloads/DTACCAMBODIA/DTACCAMBODIA/archive/sentimentDTACCAMBODIA_2017-07-04_feed_0.txt",mode='w',encoding="utf-8") as sentiFil:
    for text in filename:
        if checkSentiment(text,pro):
            forProduct(text,pro,pos,neg)
        elif checkSentiment(text,nw):
            forNetwork(text,nw,pos,neg)
        elif checkSentiment(text,bill):
            forBilling(text,bill,pos,neg)
        elif checkSentiment(text,topup):
            forTopup(text,top,pos,neg)
        elif checkSentiment(text,device):
            forDevice(text,dev,pos,neg)
        elif checkSentiment(text,device):
            forCS(text,customer,pos,neg)
        else:
            sentiFil.write(text+"*|Others|**|Unrelated|*")
        
         
                
                
        


    #print(text)


