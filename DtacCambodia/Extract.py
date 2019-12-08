import io,re

patt_u4 = re.compile(u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
patt_u2 = re.compile(u'([\u2600-\u27BF])|([\uD83C][\uDF00-\uDFFF])|([\uD83D][\uDC00-\uDE4F])|([\uD83D][\uDE80-\uDEFF])')

sentences=[]

#insert file that you want to extract
filename="C:/Users/UX/Downloads/DTACCAMBODIA/DTACCAMBODIA/DTACCAMBODIA_2017-04-30_feed_1.txt"
with io.open(filename,mode='r',encoding='utf-8') as f:
   for  mod in f:
        buffer=mod.split("\", \"")
        for b in buffer:
            b+="\","
            message=""

            if "message\": \"" in b:
                message=b.replace("message\": \"","")
                message=message.replace("\",","")
                ##message=re.search("message\": \"(.+?)\",",b)
                message=patt_u4.sub(r'',str(message))
                message=patt_u2.sub(r'',str(message))

            if message!="":
                try:
                    sentences.append(message)
                    ##sentence=message.group(1)
                    #sentence=message
                    #print(sentence)
                    #sentences.append(sentence)

                except AttributeError:
                    print("AttributeError: Message isn't taken into account.")
                    sentence=message
print(sentences)
#to save file within your the same name, location or as you wish
with io.open("C:/Users/UX/Downloads/DTACCAMBODIA/DTACCAMBODIA/DTACCAMBODIA_2017-04-30_feed_1.txt", mode='w', encoding='utf-8') as f:
    for sentence in sentences:
        f.write(sentence+"*||**||*"+"\n")
                    
