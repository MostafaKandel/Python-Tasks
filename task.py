# to validate the Format of date and check if it's valied or no
def validate_date(date):
        day=date.split(".")
        if  int(day[0]) in range(1,32) and int(day[1]) in range(1,13) and int(day[2]) in range(1,2023)  :
                return True
        else:
                return False         
         
                 
         
        
               
# to validate the Format of time and check if it's valied or no

def validate_time(time):
        clock=time.split(":")
        if int(clock[0]) in range(1,25) and int(clock[1]) in range(1,61):
                return True
        else:
                return False        
         
                
if __name__ == '__main__':
        my_list=[]
        n= int(input("How much data do you want to enter? : "))
        
        for i in range(n):
                print("please enter a date : ",end=" ")
                date=input()
                if not validate_date(date):
                        print("Date is wrong ")
                        exit()
                print("please enter a time: ", end=" ")
                time=input()
                if not validate_time(time):
                        print("time is wrong")
                        exit()
                data=" ".join([date,time])
                data= date + " - " + time
                my_list.append(data)
        print("Thank you very much. I will notify them!")

        for i in range(n):
                print(f"The {i+1} data has been reached! ({my_list[i]})")
    

 
                
 

     
 










