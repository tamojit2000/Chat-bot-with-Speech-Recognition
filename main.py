import speech_recognition as sr
from gtts import gTTS
import pyglet,os,time,datetime,sys,random
from nltk.tag import pos_tag
from textblob import TextBlob

def listen():
    print('Speak')
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
    text=r.recognize_google(audio)
    return text

def speak(text):
    try:
        f=gTTS(text=text,lang='en')
        fname='tmp.mp3'
        f.save(fname)
        music=pyglet.media.load(fname,streaming=False)
        print(text)
        music.play()
        time.sleep(music.duration)
        os.remove(fname)
    except:
        print(text)


now=datetime.datetime.now()

def polarity(sen):
    sentence=TextBlob(sen)
    
    p=sentence.sentiment.polarity
    return p

def subjectivity(sen):
    sentence=TextBlob(sen)
    s=sentence.sentiment.subjectivity
    return s
def check(sen):
    if(polarity(sen)<0 and subjectivity(sen)>=0.5):
        speak("Hey..you need to calm down..I just asked your name")
        speak("Come back when you are calm.. Byeee")
        sys.exit()

print('Lets get started.Use headphone.\n')

speak("Have you eaten yet? Its past " +str(now.hour))

Speech1=listen()

        

a=["Hey there. I couldn't recognize you. You are...??",
   "Hello there. May I know your name?",
   "Yoo.. You look cute ;). What's your name?"]
speak(random.choice(a))

sen=listen()
check(sen)
    
tagged_sent = pos_tag(sen.split())
name=[word for word,pos in tagged_sent if pos=='NNP']
speak(" ".join(str(word) for word in name)+ "?" )

flag=listen()
if (polarity(flag)<0.2):
    speak("Ohh sorry.. I'm not that smart I guess.. Please repeat.")
    
    name=listen()
    speak(name + " ..Got it.!! ")
speak("All right. Now what's your gender.Male or female?")

gender=listen()
gender=gender.upper()
if(gender != "MALE" and gender !="FEMALE"):
          speak("One word please.. Male or female?")
          
          gender=listen()  

check(gender)
a=["Great. Let's talk.",
   "Awesome. So let's get started "
   "Ok...So let's start talking"]
speak(random.choice(a))

speak("What was the last movie you watched?")

sen=listen()
speak("Oh wow.. I want to watch that movie too..!! How is it?")

sen=listen()
if(polarity(sen)>=0.7):
          speak("I knew it would be fantastic..Gotta watch it soon")
if(polarity(sen)>=0.5 and polarity(sen)<=0.7):
          speak("Hmmm...it is quite good according to you. Anyway..will watch it soon")
if(polarity(sen)>=0 and polarity(sen) <=0.4):
          speak("So it was a average movie according to you.. You got me thinking buddy")
if(polarity(sen)<0 and polarity(sen)>=-0.5):
          speak("Oh..so it was a quite bad movie")
if (polarity(sen)<-0.5):
          speak("Oh No...Was it that bad? I hope the tickets get refunded")

speak("Have you eaten yet? Its past " +str(now.hour))

sen=listen()
if(polarity(sen)>0.5):
    
    speak("Good. I haven't. Bye")
else:
    speak("So let's first eat then talk. Bye")













