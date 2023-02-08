
import speech_recognition as sr                                              #package for speech recognition   ,speech to text
import pyttsx3                                                               #package for text to speech
engine=pyttsx3.init()                                                        #initialize pyttsx3
engine.setProperty("rate",150)

recogniser=sr.Recognizer()                                                   #give i/p to recogniser
with sr.Microphone() as source:                                              #set microphone as source
    recogniser.adjust_for_ambient_noise(source,duration=0.1)                 #remove unwanted Noise present in the speech
    print("Speaking...")
    audio=recogniser.record(source,duration=5.0)                             #record audio 
    
    try:
        text=recogniser.recognize_google(audio)                             #this will return converted text from voice as string                       
        print(text)

    except:
        print("Sorry, i can't hear you")
        

answer=[int(i) for i in text.split() if i.isdigit()]
print("Number is = ",answer)

num1=int(answer[0])                                                         #to store first digit
num2=int(answer[1])                                                         #to store second digit

#calculation steps

if ("add" or "Add") in text:
    n=num1+num2
    print("Result= ",n)
    engine.say(int(n))  
    engine.runAndWait()
    


elif ("subtract" or "Subtract") in text:
    n=num1-num2
    print("Result= ",n)
    engine.say(int(n))
    engine.runAndWait()
    

elif ("multiply" or "Multiply") in text:
    n=num1*num2
    print("Result= ",n)
    engine.say(int(n))
    engine.runAndWait()
        

elif ("divide" or "Divide") in text:
    n=num1/num2
    print("Result= ",n)
    engine.say(str(n))
    engine.runAndWait()

else:
    s="Please specify the operator and retry"
    print(s)
    engine.say(s)
    engine.runAndWait()

print("calculation completed")
