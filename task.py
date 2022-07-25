import datetime
import time
 
# to validate the Format of date  and check if it's valied or no
def validate_date(user_date):
        day=user_date.split(".")
        if  int(day[0]) in range(1,32) and int(day[1]) in range(1,13) and int(day[2]) in range(1,2023)  :
                return True
        else:
                return False         
         
# to validate the Format of time and check if it's valied or no

def validate_time(user_time):
        clock=user_time.split(":")
        if int(clock[0]) in range(0,24) and int(clock[1]) in range(0,60):
                return True
        else:
                return False   

# function of current date and time 
def validate_current_date_time():
        current = datetime.datetime.now()
        time_now = current.strftime("%H:%M")
        date = current.strftime("%d.%m.%Y")
        current_datetime=" ".join([date,time_now])
        current_datetime = date+ " - " +time_now
        return current_datetime   

#function to check which data is reached
def print_result(counter):
        if counter==1:
            return "The first data has been reached"
              
        elif counter==2:
               return "The second data has been reached"
        elif counter==3:
               return "The Third data has been reached"
        else:
               return "the {} date has been reached".format(counter)
        
                                    

         
                
if __name__ == '__main__':
        my_list=[]
        n= int(input("How much data do you want to enter? : "))
        
        for i in range(n):
                print("please enter a date : ", end=" ")
                user_date=input()
                if not validate_date(user_date):
                        print("Date is wrong ")
                        exit()
                print("please enter a time: ", end=" ")
                user_time=input()
                if not validate_time(user_time):
                        print("time is wrong")
                        exit()
                data=" ".join([user_date,user_time])
                data= user_date + " - " + user_time
                my_list.append(data)
        date_time_now =validate_current_date_time()
        
        if date_time_now < my_list[i]:
                        print("Thank you very much. I will notify them!")

                        for i in range(n):
                          date_time_now =validate_current_date_time()
                          if date_time_now < my_list[i]:
                                  while(date_time_now!=my_list[i]):
                                         time.sleep(1)
                                         date_time_now=validate_current_date_time()  
                                  message=print_result(i+1) 
                                  print(message)
        else:
                        print("the {} date is wrong".format(i+1))
                                   


                

        

    

 
                
 

     
 










