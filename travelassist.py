
from  chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *                                                                                                               #for creating GUI
import webbrowser

chats=[
      
      "Hi i need your help planning my vacation.",

      "Where would u like to go?",

      "Malaysia.",

      "How many days?",

      "A week.",

      "I see.When?",

      "On 20th december.",

      "How many people?",

      "Four.",

      "How do u wish to travel?",

      "By plane.",

      "What kind of accommodation would u like?",

      "I'd like a 3 star hotel.",


      "Hilton holidays is a nice hotel.",

      "Can u send me the details?",

      "https://www.hilton.com/en/hotels/kulhihi-hilton-kuala-lumpur/",

      "Nice.I will take it.Thank u.",

      "Wish u a good journey.",

      "Thanks.",

      "Bye."


    ]

mybot=ChatBot("AI_BOT")                                                                                                              #chatbot object creation
trainer=ListTrainer(mybot)                                                                                                           #to train chatbot  
trainer.train(chats)



def talk_bot():
    request=input_area.get()
    ans=mybot.get_response(request)
    chat_area.insert(END,"You : "+request+"\n\n")
    chat_area.insert(END,"Bot : "+str(ans)+"\n\n") 
    input_area.delete(0,END)                                                                                                          #to delete input from start till end
    chat_area.yview(END)                                                                                                              #to scrollup previous chats when new chat comes.

   
    sentence="Can u send me the details"

    if sentence in request:
       
       url="https://www.hilton.com/en/hotels/kulhihi-hilton-kuala-lumpur/"
       print(url)
       webbrowser.get().open(url)
    else:

        pass



screen=Tk()                                                                                                                             #object of tk class
screen.geometry('600x780')                                                                                                              #window size
screen.title("I'm your Travel Assistant")
screen.config(bg="light blue")                                                                                                          #to add background color


img=PhotoImage(file="bot1.png")                                                                                                         #to import image                                                     
label_img=Label(screen,image=img,bg="white",border=20)                                                                                  #create image as label
label_img.pack(pady=15)                                                                                                                 #add image at top


frame=Frame(screen)                                                                                                                     #for adding contents on screen
frame.pack()                                                                                                                            #add frame below image


scr_bar=Scrollbar(frame)                                                                                                                #scrollbar inside frame
scr_bar.pack(side=RIGHT)                                                                                                                #scrollbar on rhs


chat_area=Text(frame,font=("Arial Black",15,"bold"),width=37,height=12,fg="black",wrap='word',border=3,yscrollcommand=scr_bar.set)      #chat area inside frame
chat_area.pack()
scr_bar.config(command=chat_area.yview)                                                                                                 #to move scrollbar vertically


input_area=Entry(screen,font=("Arial Black",15),border=3,width=41,bg="silver")                                                          #input area on main
input_area.pack(pady=15)

#creating send button
buttn=Button(screen,bg="green",text="Send>",command=talk_bot)
buttn.pack(pady=10,side=RIGHT,padx=25)

screen.mainloop()                                                                                                                        #keeping window on loop to see it continuously
  