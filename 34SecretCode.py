#|----------------------------------------------------------------|
#|Description    :    Secret Code Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
st=input("Enter The Message: ")
words=st.split(" ")
coding=input("1 For coding and 0 for decoding: ")
coding=True if(coding=="1") else False
if(coding):
    nwords=[]
    for word in words:
        if(len(word)>=3):
            r1="dsf"
            r2="jkr"
            stnew=r1+word[1:]+word[0]+r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords=[]
    for word in words:
        if(len(word)>=3):
            stnew=word[3:-3]
            stnew=stnew[-1]+stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))