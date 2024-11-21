#part time point is to create a task that will take from 1-3 steps to complete rewards gained also scale from 1-3
#Currently not used, will be improved upon for the final product later this year!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import random

def part_time():
        task_list = {"help janitor mop floor" : 1 , 
                
                "Help old lady carry luggage" : 1, 
                
                "Gently flip over loud crying baby's in trolleys at the airport" : 2,
                
                "smuggle some illicit peruvian imports" : 3,
              
                "help sausage fanatic dumpster dive for sausages" : 3  
                }
        random_task = random.choice(list(task_list.keys()))
        print(f"your part-time task is {random_task}")

        if random_task ==  "help janitor mop floor":
            print("Would you mind mopping one of those bathroom stalls floors? \n the cleanliness may vary, but don't let that fool you")
            stall_choices = ["stinky stall","normal stall", "premium stall"]

            
            for i, stalls in enumerate(stall_choices, 1):
                 print(f"{i}. {stalls}")
            stall_choice = int(input("which stall are you choosing? 1, 2 or 3: "))
            if stall_choice == 1:
                print("you find used toilet paper on the floor")
            elif stall_choice == 2:
                print("you find someones soiled underwear")
            elif stall_choice == 3:
                print("You find a clean bathroom \n Janitor: thanks for nothing")
            return
    
        if random_task ==  "Gently flip over loud crying baby's in trolleys at the airport":
            baby_choices = ["loud couple's baby", "quiet couple's baby", "single parent's baby"]
            for i, baby in enumerate(baby_choices, 1):
                print(f"{i}. {baby}")
            baby_choice = int(input("pick a baby to flip over gently? 1, 2 or 3: "))
            if baby_choice== 1:
                 print("Loud couple: what the hell are you doing!! \n Loud wife: honey do something!! \n Loud husband: Why do i always have to do something!!\n couple's arguing intensifies and you get away with it ")
                 print("baby's crying intensifies")
            elif baby_choice == 2:
                 print("Baby quiets down. \n quiet couple: thank god finally peace.")
            elif baby_choice == 3:
                print("flipped baby crying intensifies!!" )
            return


       
             
        if random_task == "smuggle some illicit peruvian imports":
            import_choices = ["socks", "floppy disk", "where the sun don't shine"]
            for i, imp in enumerate(import_choices, 1):
                print(f"{i}. {imp}")
            import_choice = int(input("choose where you want to hide imports! 1, 2 or 3: "))
            if import_choice== 1:
                print("TSA Worker: Why are you trying to smuggle cigars and in your socks of all places \n They are legal! are you stupid??")
            elif import_choice == 2:
                 print("TSA Worker: why are you trying to smuggle cigars in a floppy disc? \n They are perfectly legal! are you stupid??")
            elif import_choice == 3:
                 print("TSA Worker: Sir why do you have cigar in your ass?!! \n TSA Worker's brain shuts down")
            return
        
        
        if random_task == "Help old lady carry luggage" :
            print("pick an item to carry. 1, 2 or 3: " )
            luggage_choices = [" heavy luggage", "medium luggage","her purse"] 
            for i, luggage in enumerate(luggage_choices, 1):
                 print(f"{i}. {luggage}")
            luggage_choices = int(input("pick a piece of luggage? 1, 2, or 3 : "))
            if luggage_choices == 1:
                print("old lady: well aren't you a sweet young man \n thank you for sparing my back by carrying the heavy luggage. ")
            elif luggage_choices == 2:
                print("old lady: Well atleast you didn't pick my purse ")
            elif luggage_choices == 3:
                 print("old lady: chivalry must be dead")
            return

            
    
        if random_task ==  "help sausage fanatic dumpster dive for sausages":
            
            sausage_choices = ["finnair sausage", "black sausage","HK sininen"] 
            
            
            for i, sausage in enumerate(sausage_choices, 1):
                 print(f"{i}. {sausage}")
            sausage_choice = int(input("Fanatic: Thanks for the help earlier.\n Pick a sausage for the help now won't you? 1, 2, or 3 : "))
            if sausage_choice == 1:
                    print("fine choice quite the rare on you chose.")
            elif sausage_choice == 2:
                print("You have quite the discerning eye for sausages \n were you sausage maker in your past life")
            elif sausage_choice == 3:
                print("you really don't know anything about sausages do you? \n you're a heretic! but to each their own i guess")
            return

                
                
        

#Monke

part_time()
