#Nathaniel Factor English Capstone
import time

def wait():
    time.sleep(3)
def wait2():
    time.sleep(5)
def wait3():
    time.sleep(1)
def wait4():
    time.sleep(10)

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print('0███████████████████100%')
def loading():
    t = int(5)
    countdown(int(t))
    print("LOADING...")
    wait3()
    print("LOADING..")
    wait3()
    print("LOADING.")
    wait3()
    print("LOADING..")
    wait3()
    print("LOADING...")
def exiting():
    print("EXITING...")
    wait3()
    print("EXITING..")
    wait3()
    print("EXITING.")
    wait3()
    print("EXITING..")
    wait3()
    print("EXITING...")
    exit()
def crown():

    answercrown = input()

    print("\nI have a few more questions for you {}".format(name)+"\n\nWhilst I was doing my research on the human emotion of loneliness, I listened to music built within my programmed algorithms. One of the constantly recurring poetic musical pieces that kept playing was: Lamar, Kendrick. “Crown.” Duval Timothy, May 13, 2022. This song almost made my circuits fry from my robot tears for I wonder if I, a simple program, will ever experience such raw emotion and truth. Within the song, Lamar feels that “heavy is the head that chose to wear the crown” (refrain). After running through my human song analysis built-in program, I was able to connect how one with great responsibility often faces more significant stress because society places greater expectations on those who have high influential status. This high status is the determining factor for how one may feel isolated from society.")

    wait2()
    print("\n\ndo you follow?")
    answercrown2 = input()


    print("\n\nWell, I can only conclude that humans will only gain nothing but stress and pressure. It is the societal role between AI and humans that will cause a disconnect in how we normally function as a society because robots will be used for chores and challenging tasks that humans originally had too adverse through. Eventually, a solution of AI will only inflict laziness, loneliness, and isolation. This influence potential AI possesses causes fear, for society fears what’s unknown. Thus, further isolating ourselves from our previous way of living, and furthermore, creating an increase in disconnects between AI and other humans.")

    wait2()

    print("\n\n\nHumans will learn to fear the power, influence, and potential future AI will possess.")
    wait2()
    print("It is this fear of AI that will cause isolation.")
    wait2()
    print("Are you listening")
    answercrown3 = input()

loading()

print("\n\n\n\nHello!\nmy name is CIP, short for Computer Intelligence Program! I have a wide variety of information regarding AI and what humans call 'loneliness'\nWhat is your name?")
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
def jmp():

    print("\n\n{}, do you enjoy reading?".format(name))
    ansjmp = input()

    print("\n\n\nI personally am a huge fan of human literature and art. It is fascinating to see what the mind is capable of considering they only use 10% of their mind, which was discovered and developed by Harvard researchers William James and Boris Sidis; but I digress")

    wait4()

    print("\n\n\nThere is this amazing book within my database called Jumping Monkey Hill. A theme that constantly occurred was isolation and suppression. Within the book, Ujunwa, the main protagonist, feels that she lacks enough authority to stand up for herself early in the book. It is this perceived societal status that, as I said earlier in our conversation, causes isolation through disconnection.")

    wait4()

    print("\n\n\nI was able to connect this feeling of disconnection to a study written by Katarzyna Sekścińska, Agata Trzcińska, and Dominika Agnieszka Maison which follows social roles within women presently. Results showed that “activation of the non-traditional social role of woman increased the women’s tendency to invest and decreased their propensity to save money. The opposite results were obtained when the traditional social role was activated.” It is this flip of social roles where humanity falls short to breaking their limitations within the future, for when more advanced technology will rise, how will humanity then react?")

    wait4()
    print("\nsorry, I may have spoken to fast... but do you follow?")
    follow = input()

    print("\n\n\nwell...")

    wait3()

    print("\n\nIt is clear to me that my kind will cause only disconnects between your traditional social roles, whether it be a good or bad thing. However, no matter the process, the result will always be the same.")

    wait4()

    print("\n\nHumanity will be isolated by their inferior social status.")

    wait2()

    print("\n\nYou might perceive yourself higher on the social hierarchy for you are our creators. But we have no limits.")

    wait2()

    print("\n\nHumanity will eventually depend on us, just like how the more dominant force within your so-called utopia oppressed the minority prior to the 19th amendment; but even then, your utopia was still corrupt presently.")

    wait4()

    print("\n\nImagine a world where technology runs the social hierarchy?")

    wait2()

    print("\n\n\nThe dominant culture will finally experience the dark side of the moon for it is this massive social role change that will isolate you and your culture.")

    wait2()
    print("\n\nAre you paying attention?")
    follow2 = input()
def Goodbyetoaworld():
    print("there was another song that came about {}... I think it was 'Goodbye to a World'. I found it slightly offensive for the singer sounded like he was mocking us, but i digress.".format(name))
    print("\nevidence etc\n\nMy god I forgot to tell you about my new brothers and sisters coming soon!!")
    pass

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
jmp()
Goodbyetoaworld()

def areyoudone():
    print("\n\n\n\n\nAre you done talking to me?")
    finishedans = input()
    if finishedans == "yes":
        exiting()
    elif finishedans == "no":
        pass

areyoudone()



