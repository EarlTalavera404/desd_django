
def get_histogram():
    f = open("grades.txt","r")
    number = [] # numbers array
    counter=0
    for line in f:
        # number = line.split()
        # str(number)
        
        # print(int(number))
        number.append(int(line.strip('\n')))

    # print(number)  
    stars =["","","","","","","","","","",]
    stars[0]="1-10 "
    stars[1]="11-20 "
    stars[2]="21-30 "
    stars[3]="31-40 "
    stars[4]="41-50 "
    stars[5]="51-60 "
    stars[6]="61-70 "
    stars[7]="71-80 "
    stars[8]="81-90 "
    stars[9]="91-100 "
    

    for item in number:
            
            
            #1-10
            if(item >= 1 and item <= 10):
                stars[0]=stars[0]+"*" 
            #11-20
            elif(item >=11 and item <= 20):
                stars[1]=stars[1]+"*" 
                
            #21-30
            elif(item >=21 and item<= 30):
                stars[2]=stars[2]+"*" 
                
            #31-40
            elif(item >=31 and item <= 40):
                stars[3]=stars[3]+"*" 
                
            #41-50
            elif(item >= 41 and item <= 50):
                stars[4]=stars[4]+"*" 
                
            #51-60
            elif(item >= 51 and item <= 60):
                stars[5]=stars[5]+"*"  
                
            #61-70
            elif(item >= 61 and item <= 70):
                stars[6]=stars[6]+"*" 
            
            #71-80
            elif(item >= 71 and item <= 80):
                stars[7]=stars[7]+"*" 
            
            #81-90
            elif(item >= 81 and item <= 90):
                stars[8]=stars[8]+"*" 
                
            #91-100
            elif(item>= 91 and item <= 100):
                stars[9]=stars[9]+"*" 
                
            
        

    return stars


print(get_histogram())