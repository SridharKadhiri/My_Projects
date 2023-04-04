import json
def ques():
    import json
    print("Welcome to Dictionary app")
    print("Please select your choice")
    print("1. Add a word")
    print("2. Find the meaning")
    print("3. Update the word")
    print("4. Exit")
    print("*"*60)
    
    
def update():
    f = open('word.txt','w')
    word = input('Enter the word to add to dictionary :')
    meaning=input('enter its meaning :')
    words_collected[word] = meaning
    json.dump(words_collected,f)
    f.close()

def getmeaning():
    f  = open("word.txt" ,"r")
    word = input("Enter the word : ")
    if word in words_collected:
        print('The meaning is : ', words_collected.get(word))
        f.close()
    else :
        print("no such word exists")

def update_word():
    f  = open("word.txt" ,"r")
    word = input("Enter the word : ")
    if word in words_collected:
        meaning=input('enter its meaning :')
        words_collected[word] = meaning
        f.close()
    else :
        print("no such word exists")
        

            
f = open('word.txt','w')
words_collected = {}
json.dump(words_collected,f)
f.close()   
    

while True:
    
    ques()
    x = input("Enter your option : ")  
    
    if x == "1":        
        update()
        print("*"*60)    
        
    elif x == "2" :
        getmeaning()
        print("*"*60)    
        
    elif x == "3":      
        update_word
        print("*"*60)    
    
    elif x=="4":
        print("Exit")
        print("*"*60)            
        break        
    else:       
        print("no option selected ! ")
        print("*"*60)           
        break 
    