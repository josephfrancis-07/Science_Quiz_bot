import requests
import json
import random as rand
import html

data_validation3=False
while data_validation3==False:
    r=requests.get("https://opentdb.com/api.php?amount=1&category=18&type=multiple")
    if r.status_code==200:
        string=json.loads(r.text)
    
        category= string['results'][0]['category']
        type_=string['results'][0]['type']
        level=string['results'][0]['difficulty']
        question=html.unescape(string['results'][0]['question'])
     
    #generating list of options and inserting the correct answer into a random position
    
        options=[]
        options.append(html.unescape(string['results'][0]['incorrect_answers'][0]))
        options.append(html.unescape(string['results'][0]['incorrect_answers'][1]))
        options.append(html.unescape(string['results'][0]['incorrect_answers'][2]))
        options.insert((rand.randint(0, 3)),html.unescape(string['results'][0]['correct_answer']))
    
    #printing the question and options
    
        print("\nCategory : ",category,"\t\tLevel : ",level,"\n\n Question : ",question,"\n\n\tOptions : 1)",options[0],"\n\t          2)",options[1],"\n\t          3)",options[2],"\n\t          4)",options[3],"\n")
        
    #inputing data , validatin and error handling are doing here.
        
        data_validation=False
        while data_validation==False:
            ans=input("Enter your option : ")
            try:
                ans=int(ans)
                data_validation=True
            except:
                print("Invalid input.. Ener your option correctly. \n")
                continue
            if ans>=0 and ans<=4:
                if string['results'][0]['correct_answer']==options[ans-1]:
                    print("Correct answer ... Congratulations..:)")
                else:
                    print("Oops!! Wrong answer... Correct answer was '",string['results'][0]['correct_answer'],"'")
            else:
                print("Invalid input !")
                data_validation=False
        data_validation2=False
        while data_validation2==False:
            inp=input("\nDo you want to try more ?? y/n : ")
            try:
                inp=str(inp.lower())
            except:
                print("Invalid option ! \n")
                continue
            if inp=="y":
                break
            elif inp=="n":
                print("Thank you")
                exit()
            else:
                print("Invalid input !")
                continue    
    else:
        print("There are some errors in retrieving the question either quit or try again...\n")
        while data_validation4==False:
            inp1=input("\nDo you want to quit? y/n : ")
        try:
            inp1=str(inp1.lower())
        except:
            print("Invalid option ! \n")
            continue
        if inp=="n":
            break
        elif inp=="y":
            print("Thank you")
            exit()
        else:
            print("Invalid input !")
            continue
            
        
      
    
