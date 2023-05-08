questions=[["python is an ","interpreted language","assembly language","machine language","both 2 and 3",1],["which of the skill required for the front end","html","css","both and b","none of the above",3],
["operating system can be defined as","hardware component","intermediato b/w hard. and soft.","language","None of the above",2],
["A process executes the code for fork();,fork();,fork(); Number of child process complete","2","3","7","none of the above",3],
["What is the capital city of France?","Paris", "Madrid", "Rome", "Berlin",1],["What is the largest planet in our solar system?","Venus", "Jupiter", "Saturn", "Mars",2],
["Who is the current President of the United States?","Joe Biden", "Donald Trump", "Barack Obama", "George W. Bush",1],
["What is the currency of Japan?","Yen", "Dollar", "Euro", "Pound",1],
         
["What is the smallest continent in the world?","Asia", "Africa", "Australia", "Europe",3],
["Who invented the telephone?","Thomas Edison", "Alexander Graham Bell", "Nikola Tesla", "Albert Einstein",2]]
level=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
money=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"\n\nQ.{i+1}-{question[0]}       ->[for Rs. {level[i]}]\n")
    print(f"[1]. {question[1]}          [2]. {question[2]}\n")
    print(f"[3]. {question[3]}          [4]. {question[4]}\n")
    reply= int(input("Enter the option( 1-4 ): "))
    if(reply==question[-1]):
        print(f"you have won {level[i]}")
        if(i==4):
            money=5000
        elif(i==9):
            money=9000
        
    else:
        print("wrong answer")
        break    
print(f"your take home money is Rs-{money}")