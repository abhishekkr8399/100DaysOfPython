#|----------------------------------------------------------------|
#|Description    :    KBC Program
#|----------------------------------------------------------------|
#|Author         :    ABHISHEK KUMAR, Computer Science Student
#|----------------------------------------------------------------|
#|Organization   :    NMAMIT, Nitte
#|----------------------------------------------------------------|
#|E-Mail         :    abhishekkumar8399@gmail.com
#|----------------------------------------------------------------|
ques=[
        ["Which language was used to make chatgpt ?","Python","French","JavaScript","Php","None",4],
        ["Which language was used to make chatgpt ?","Python","French","JavaScript","Php","None",4],
        ["Which language was used to make chatgpt ?","Python","French","JavaScript","Php","None",4],
        ["Which language was used to make chatgpt ?","Python","French","JavaScript","Php","None",4]
    ]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money=0
for i in range(0,len(ques)):
    q=ques[i]
    print(f"\n\nQuestion for Rs.{levels[i]}")
    print(f"a. {q[1]}     b. {q[2]}")
    print(f"c. {q[3]}     d. {q[4]}")
    reply = int(input("Enter your answer [1-4] or 0 to quit:\n"))
    if(reply==0):
        money=levels[i-1]
        break
    if(reply==q[-1]):
        print(f"Correct Answer,You have won Rs.{levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==14):
            money=10000000
    else:
        print("Wrong Answer!")
        break

print(f"Your total winning amount:{money}")