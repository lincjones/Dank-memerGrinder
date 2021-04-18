import pyautogui, time

def main():
   menu()


def menu():
    print("************-_-Dank Memer Grinder-_-**************")
    print()

    choice = input("""
                      A: I have fishing, hunting, and postmeme abilities 
                      B: I have fishing and hunting
                      C: I have nothing

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        time.sleep(7)
        f = open("a", 'r')
        for word in f:
            pyautogui.typewrite(word)
            pyautogui.press('enter')
    if choice == "B" or choice =="b":
        time.sleep(10)
        f = open("b", 'r')
        for word in f:
            pyautogui.typewrite(word)
            pyautogui.press("enter")
    if choice == "C" or choice =="b":
        time.sleep(10)
        f = open("c", 'r')
        for word in f:
            pyautogui.typewrite(word)
            pyautogui.press("enter")
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()

def register():
   pass
    
def login():
   pass
    
#the program is initiated, so to speak, here
main()

