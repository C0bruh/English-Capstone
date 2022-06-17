#Nathaniel Factor English Capstone
import time

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print('0███████████████████100%')
    
t = int(5)
countdown(int(t))

def wait():
    time.sleep(3)

def wait2():
    time.sleep(5)

def crown():

    answercrown = input()

    print("\nI have a few more questions for you {}".format(name)+"\n\nWhilst I was doing my research on the human emotion of loneliness, I listened to music built within my programmed algorithms. One of the constantly recurring poetic musical pieces that kept playing was: Lamar, Kendrick. “Crown.” Duval Timothy, May 13, 2022. This song almost made my circuits fry from my robot tears for I wonder if I, a simple program, will ever experience such raw emotion and truth. Within the song, Lamar feels that “heavy is the head that chose to wear the crown” (refrain). After running through my human song analysis built-in program, I was able to connect how one with great responsibility often faces more significant stress because society places greater expectations on those who have high influential status. This high status is the determining factor for how one may feel isolated from society.")

    wait2()
    print("\n\ndo you follow?")
    answercrown2 = input()


    print("\n\nWell, I can only conclude that humans will only gain nothing but stress and pressure. It is the societal role between AI and humans that will cause a disconnect in how we normally function as a society because robots will be used for chores and challenging tasks that humans originally had too adverse through. Eventually, a solution of AI will only inflict laziness, loneliness, and isolation. This influence potential AI possesses causes fear, for society fears what’s unknown. Thus, further isolating ourselves from our previous way of living, and furthermore, creating an increase in disconnects between AI and other humans.")

    wait2()

    print("\n\n\nHumans will learn to fear the power potential future AI will possess.")
    wait2()
    print("It is this fear of AI that will cause isolation")
    wait2()
    print("Are you listening")
    answercrown3 = input()


print("Hello...\nmy name is CAL, I have a wide variety of information regarding AI and what humans call 'loneliness'\nWhat is your name?")
name = input()
print("Well {}, would you like to listen to my studies?".format(name))
print("**input yes or no**")
ans = input()

def calculator():
    print("\n\n\n\n\n\n\nThere is another study (still have to find) of how since mathematics within robots surpass human capabilities, they believe robots are even more superior...!\ngive me a number:")
        
    num1 = float(input())
    print("GIvE me another number:")
    num2 = float(input())
    if num1 and num2:
        numaddition = num1 + num2
        nummultiplication = num1 * num2
        numexponent = num1 ** num2
            
        print("\n\n\n\n\n\n\n\n\n\n\n\n")
        print("The addition of these two equations is: ",numaddition)
        print("And the multiplication is: ",nummultiplication)
        print("And the first number raised to the second number is: ",numexponent)
        print("\nI have the capabilities to do even more advanced theoretically based math!")

        wait()

        print("hey {}, sorry to spring this on you, but even though you are talking to me, do you feel like you're alone; you are just talking to a computer screen after all.".format(name))
        dyans1 = input()

'''
if ans == "yes":
        
    calculator()
        
    print("\ni guess it is always just you and your thoughts\nonly you are with yourself 24/7\nhumans think love can fill the void\nit cant\nnothing can\nfor you will always be alone")
    print("\n do you agree?")

    ans3 = str(input())
    print("have you ever listened to porter robinson etc\nexplanation quote etc")
    print("nOW tell m e {}, is loneliness like this?".format(name))
    ans2 = str(input())
    if ans2 == "no":
        print("Even if I am a computer, you feel as if you are talking to a human? I was programmed to say these characters in a fashion that would make sense to you.")


    print("Have you eVer rEad JuMPiNg Monkey Hill? I found that this specific story written by ... expresses a multitude of different isolation environments.")
    jmpans = str(input())
    if jmpans == "yes":
        print("evidence quote etc")
        print("nOW tell m e {},  do you think loneliness like this?".format(name))
    else:
        print("evidence quote etc")
        print("nOW tell m e {},  do you think loneliness is like this?".format(name))  


elif ans == "no":
    print("\n\n\n\n\n\nokay goodbye!")
    
    t = int(5)
    countdown(int(t))
    
    exit()
'''


crown()

def Goodbyetoaworld():
    print("there was another song that came about {}... I think it was 'Goodbye to a World'. I found it slightly offensive for the singer sounded like he was mocking us, but i digress.".format(name))
    print("\nevidence etc\n\nMy god I forgot to tell you about my new brothers and sisters coming soon!!")
    pass

Goodbyetoaworld()

def areyoudone():
    print("\n\n\n\n\nAre you done talking to me?")
    finishedans = input()
    if finishedans == "yes":
        pass
    elif finishedans == "no":
        pass

areyoudone()

