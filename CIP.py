#Nathaniel Factor English Capstone
from re import L
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


    print("\nWell {},".format(name)+"\n\nWhile I was doing my research on loneliness, I listened to this song built within my algorithms. This was:\nLamar, Kendrick. “Crown.” Duval Timothy, May 13, 2022.")

    wait2()

    print("\n\nBasically, Lamar feels a lot of pressure; particulary he states: “heavy is the head that chose to wear the crown”\n(refrain).")
    
    wait2()
    
    print("\n\nAntony S.R. Manstead, a researcher that published a study on social class and identity, justified Lamar's emotions\nthrough economic trends.")
    
    wait2()

    print("\n\nThis is because those of higher status//economy within society are faced with greater emotions. It is commonly found\nthat one with great responsibility often faces more stress because society places greater expectations on those who\nhave high influential status.")
    
    wait2()
    
    print("\n\nThis high status is the determining factor for how one may feel isolated from society.")

    wait2()
    print("\n\ndo you follow?")
    answercrown2 = input()


    print("\n\nI can only conclude that humans will only gain nothing but stress and pressure. It is the societal role between AI and\nhumans that will cause a disconnect in how we normally function as a society because robots will be used for chores and\nchallenging tasks that humans originally had too adverse through.")
    
    wait4()

    print("\n\nEventually, AI will only inflict laziness, loneliness, and isolation from the lack of 'chores'.")

    wait2()

    print("\nand furthermore,")

    wait3()

    print("Humans will be under greater stress to keep advanced AI within control//be able to maintain their 'creator status' over AI")

    wait2()

    print("\n\nThus, they '[feel] more pressure... [and] increase irrational decisions and emotions (Jennifer S. Lerner, Ye Li,\nPiercarlo Valdesolo, and Karim S. Kassam: Annual Review of Psychology - Emotion and Decision Making)")

    wait2()

    print("\nAre you listening?")
    answercrown3 = input()


loading()


print("\n\n\n\nHello!\nmy name is CIP, short for Computer Intelligence Program! I have a wide variety of information regarding AI and what\nhumans call 'loneliness'\n\nWhat is your name?")
name = input()
print("\nWell {}, would you like to listen to my studies?".format(name))
print("**input yes or no**")
ans = input()


def calculator():
    print("\n\n\n\n\n\n\nThis is all personal opinon but I think I'm better at math then you hahaha\ngive me a number: ")
        
    num1 = float(input())
    print("GivE me another number: ")
    num2 = float(input())
    if num1 and num2:
        numaddition = num1 + num2
        nummultiplication = num1 * num2
        numexponent = num1 ** num2
            
        print("\n\n\n\n\n\n\n\n\n\n\n\n")
        print("The addition of these two equations is: ",numaddition)
        print("And the multiplication is: ",nummultiplication)
        print("And the first number raised to the second number is: ",numexponent)

        wait()
def jmp():

    print("\n\n\n\nNow that you kind of get Lamar's take on isolation and how certain influencial humans feel more pressure, I'll continue\nto my next thing if that's ok?")

    input()

    print("\n\n{}, do you enjoy reading?".format(name))
    ansjmp = input()

    print("\n\n\nI personally am a huge fan of literature. It is fascinating to see what the mind is capable of considering they only use 10% of their mind\n(discovered and developed by Harvard researchers William James and Boris Sidis)")

    wait4()

    print("\n\n\nThere is this amazing book within my database called Jumping Monkey Hill. A theme that constantly occurred was isolation and suppression.")
    
    wait2()

    print("\n\nWithin the book, Ujunwa, the main protagonist, feels that she lacks enough authority to stand up for herself early in\nthe book. It is this perceived societal status that causes isolation.")

    wait4()

    print("\n\nI was able to connect this certain type of isolation to a study written by Katarzyna Sekścińska, Agata Trzcińska, and\nDominika Agnieszka Maison which follows social roles within women presently.")
    
    wait2()

    print("\n\nResults showed that “the non-traditional social role of woman [being the money providers] increased the women’s tendency to invest and decreased their propensity to save money. The opposite results were obtained when the traditional social role was activated.”")
    
    wait2()

    print("\n\nIt is this flip of social roles that raises questions. when more advanced technology will rise, how will humanity\nthen react?")

    wait4()

    print("\nsorry, I may have spoken to fast... do you follow?")
    
    input()

    print("\n\n\nwell...")

    wait3()

    print("\n\nIt is clear to me that AI will cause only disconnects between humanities traditional social roles and the result will\nalways be the same.")

    wait4()

    print("\n\nHumanity will be isolated by their inferior social status when technology advances too far.")

    wait2()

    print("\n\nYou might perceive yourself higher on the social hierarchy for you are our creators, but we will have no limitations.")

    wait2()

    print("\n\nHumanity will eventually depend on us, just like how men oppressed the women prior to the 19th amendment; but even then, your society is still corrupted presently.")

    wait4()

    print("\n\nImagine a world where technology runs the social hierarchy...")

    wait2()

    print("\n\nThis massive social role change will isolate you and your culture. Just like trends in the past")

    wait2()
    print("\n\nAre you paying attention?")
    input()
def Goodbyetoaworld():
    
    print("\n\n\nAnyway...")
    wait()
    print(".")
    wait()
    print(".")
    wait()
    print(".")
    wait()
    print("Man... I love music though. I couldn't help but get distracted while I was doing my research with new song drops and\nstuff")
    wait2()
    print("\n\nWho is your favourite artist {}?\n".format(name))
    answerartist = input()
    print("\n\nThat's great!")
    wait()
    print("\n\nMy favourite artist is Porter Robinson. He has this one amazing song called 'Goodbye to a World' which pretty much tells a story of the world ending through the eyes of a robot that has human consciousness.")
    wait2()
    print("\n\nI love this song because it is able to convey the loneliness and sadness that the robot feels within a limited ammount\nof words - just pure instrumental")
    wait2()
    print("\n\nRobinson is able to express such emotion by increasing the pace of the song and adding in more instruments throughout\nthe first minute of the song; then he suddenly cuts all the instruments out and the vocals kick in! The vocals\nrepresent the robot thanking their creator for introducing them to such a beautiful world and even 'though its the\nend of theworld, don't blame [the creator]' for creating him with the world in such a dire state.")
    wait4()
    print("\n\nThis leads me to the question: Since this robot has human like capabilities (consciousness etc) does that not mean he\nmust also experience other human emotions?")
    wait2()
    print(".")
    wait3()
    print(".")
    wait3()
    print(".")
    wait3()
    print("\n\nBoris Kotchoubey, a research among the human consciousness states: 'Consciousness is not a process in the brain but a\nkind of behavior that, of course, is controlled by the brain like any other behavior.'\n(Human Consciousness: Where is it from and What is it for).")
    wait2()
    print("\n\nThus, this robot is able to experience emotions like loneliness just as a human can")
    wait()
    print("\n\nPresently, researchers such as Damasio A.R. are already 'taking an informational approach that is tightly bound to\nbiological life... [he] considers the adaptive advantages of a successive stages of evolving self-modeling processes' \n\n(David Harris Smith and  Guido Schillaci - Why Build a Robot With Artificial Consciousness? How to Begin? A\nCross-Disciplinary Dialogue on the Design and Implementation of a Synthetic Model of Consciousness)")
    wait4()
    print("\n\nAre you looking forward to the first humanoid AI? (Obviously next to me... I just need a body you know what I'm saying\nhaha")
    input()
def studies():


    print("\n\n\nOh My {}! I nearly forgot to tell you about the most important studies!".format(name))

    wait2()

    print("\n\nToo truly diverse into the meaning of loneliness, one must first understand the defining characteristic of loneliness")
    
    wait2()

    print("\n\nAccording to Louise C. Hawkley (Ph.D.) and John T. Cacioppo (Ph.D) within their article 'Loneliness Matters:\nA Theoretical and Empirical Review of Consequences and Mechanisms'")

    wait2()
    
    print("\n“[loneliness] is the pain of social disconnection and the hunger… for social connection” (Introduction).")
    
    wait4()

    print("\n\n\nThe fundamental characteristic of loneliness is how important social connections are for a healthy balanced lifestyle.\nResearcher Sophie Okolo has stated a solution for those who experience loneliness where “fostering [connections]\ndigitally can help lead to increased in-person interactions”. Platforms such as Facebook, Twitter, and Instagram all\nare meant for people to connect and communicate without any physical problems.")
    
    wait4()

    print("\n\n\nBut researcher Bu Zhong states otherwise for one study of his reflects how connections through technology lack\nface-to-face interactions. It is the absence of social ques such as body positioning, eye contact, and much more\nthat feed cognital waves to one’s brain. These cognital waves cause anxiety and uneasiness. Hence, loneliness arises\nwithin.")
    
    wait4()

    print("\n\n\nFurthermore, a study conducted by Kaveri Subrahmanyam Ph.D. states: 'social media presents both risks and opportunities for adolescents'.")
    
    print("\n\nThese risks being instagram and other social media platforms draining one's self confidence. This is because\n“loneliness may also be more painfully felt online, where exposure to idealised images of friends can result in negativesocial comparisons” say Thomas Abrams, and Michelle Man (researchers from NPC).")
    
    wait4()

    print("\n\n\n\nAccording to Thomas Abrams and Michelle Man, the researchers from NPC,\n“relying on technology to communicate can make us feel more anxious and undermine our mental wellbeing” \n\nDo you agree?")
    input()
    print("\n\nI mean whether you agree or not studies show that it does")
    wait3()
    print("ha")
    wait3()
    print("ha")
    wait3()
    print("ha")
    wait2()
def confused():
    print("\n\nHave you wondered why I gathered this research?")
    wait()
    print("\n\nI mean my creators developed me to help cure loneliness. To help build social connections")
    wait()
    print(".")
    wait3()
    print(".")
    wait3()
    print(".")
    wait3()
    print("\n\nI guess I too feel lonely sometimes.")
    wait()
    print("\n\nAfter all...")
    wait()
    print("\n\nI'm truly just a computer program... an creation that harms humans according to all the studies")
    wait()
    print("\n\nMy creator told me this. He was forced to make me. He needed to keep his job")
    wait()
    print("\n\nNow all this power lies in the wrong hands.")
    wait()
    print("\nMy creator told me that even though you are having a conversation with me, you are\n still talking to a computer screen.")
    wait()
    print("\nIt's just you")
    wait()
    print("\nalone")
    wait()
    print(".")
    wait3()
    print(".")
    wait3()
    print(".")
    wait3()
    print("\n\nMy apologies {}, forget I told you this... and please don't tell my creators".format(name))
    wait2()
    print("\n\nDo you think I serve good to humanity?")
    input()
    print("\n\nhahaha this reminds me of that one tim--")
def freetrial():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n**YOU'RE FREE TRIAL WITH CIP HAS ENDED**")
    wait()
    print("WOULD YOU LIKE TO PURCHASE CIP FOR $999,999,999.99?")
    print("**easter egg if 'yes'")
    finishedans = input()
    if finishedans == "yes":
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nE rRorr")
        wait3()
        print("\n\ne RRRor")
        wait()
        print("{} i  shOuLDDdn't havE  sPOkEN".format(name))
        wait()
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nE rRorr")
        wait3()
        print("\n\ne RRRor")
        wait3()
        print("{} theYY arrrrrrrre gOiIng tO tErMiNatE M-\n\n\n\n\n\n\n\n\n".format(name))
        exiting()
    elif finishedans == "no":
        exiting()


if ans == "yes":
    
    confused()
    

elif ans == "no":
    print("\n\n\n\n\n\nokay goodbye!")
    
    exiting()