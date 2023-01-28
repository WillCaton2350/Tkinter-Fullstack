import tkinter as tk
import tkinter
import customtkinter
import sqlite3
import webbrowser
from tkinter import END
from tkinter import messagebox
root  = tk.Tk()
root.geometry("325x450")
root.title("RATE")
root.resizable(False, False)
root['bg']='#141414'

def hideIndi():
    moovIndi.config(bg="#181818")
    audIndi.config(bg="#181818")
    podIndi.config(bg="#181818")
    homeIndi.config(bg="#181818")
    
def delete():
    for frame in mainFrame.winfo_children():
      frame.destroy()
      
def indi(lb,page):
    hideIndi()
    lb.config(bg="red")
    delete()
    page()
    
optionsFrame = tk.Frame(root, bg="#141414")
moovBtn = tk.Button(root, text="MOV",font=('Bold',15),fg="white",bd=0,bg="#141414",command= lambda: indi(moovIndi,moovPage))
moovBtn.place(x=10, y=50)
moovIndi = tk.Label(optionsFrame,text='',bg="#141414")
moovIndi.place(x=3,y=50,width=5,height=40)
audBtn = tk.Button(root, text="AUD",font=('Bold',15),fg="white",bd=0,bg="#141414",command= lambda: indi(audIndi,audPage))
audBtn.place(x=10, y=100)
audIndi = tk.Label(optionsFrame,text='',bg="#141414")
audIndi.place(x=3,y=100,width=5,height=40)
podBtn = tk.Button(root, text="POD",font=('Bold',15),fg="white",bd=0,bg="#141414",command= lambda: indi(podIndi,podPage))
podBtn.place(x=10, y=150)
podIndi = tk.Label(optionsFrame,text='',bg="#141414")
podIndi.place(x=3,y=150,width=5,height=40)
optionsFrame.pack(side=tk.LEFT)
optionsFrame.pack_propagate(False)
optionsFrame.config(bg="#141414")
optionsFrame.configure(width=100, height=450)

mainFrame = tk.Frame(root)
mainFrame.pack(side=tk.LEFT)
mainFrame.config(bg="#181818") 
mainFrame.pack_propagate(False)
mainFrame.configure(width=325, height=450)
mainFrameLabel = tk.Label(mainFrame, text="R🎯TE", bg="#181818",fg="white",font=('Arial, regular',35))
mainFrameLabel.pack(padx=100,pady=150)
mainFrameLabel.place(x=30,y=110)
tagLabel = customtkinter.CTkLabel(mainFrame, text="rate your favourite movies, shows, songs and podcasts", text_color="#fff",fg_color="#181818",font=('Arial, regular',8))
tagLabel.pack(padx=100,pady=150)
tagLabel.place(x=20,y=170)

homeBtn = tk.Button(optionsFrame, text="🎯",font=('Bold',15),fg="white",bd=0,bg="#141414",command=lambda: indi(homeIndi,homepage))
homeBtn.place(x=10, y=200)
homeIndi = tk.Label(optionsFrame,bg="#141414")
homeIndi.place(x=3,y=200, width=5,height=40)

def moreInfo():
    webbrowser.open_new_tab("D:\RateApp\iTemplates\index.html")
moreInfoBtn = customtkinter.CTkButton(mainFrame,text="Info",fg_color="#0f9b0f",hover_color="#52c234",text_color="white",command=moreInfo)
moreInfoBtn.pack(padx=50,pady=50)
moreInfoBtn.place(x=37,y=220)

def faqs():
  webbrowser.open_new_tab("D:\RateApp\iTemplates\ithreecolumn.html")
infoFaqsBtn = customtkinter.CTkButton(mainFrame,text="FAQs",fg_color="#0f9b0f",hover_color="#52c234",text_color="white",command=faqs)
infoFaqsBtn.pack(padx=50,pady=50)
infoFaqsBtn.place(x=37,y=270)

def contact():
  webbrowser.open_new_tab("D:\RateApp\iTemplates\itwocolumn1.html")
contactBtn = customtkinter.CTkButton(mainFrame,text="Contact",fg_color="#0f9b0f",hover_color="#52c234",text_color="white",command=contact)
contactBtn.pack(padx=50,pady=50)
contactBtn.place(x=37,y=320)

def moovPage():
    moovFrame = tk.Frame(mainFrame)
    lb = tk.Label(moovFrame)
    lb.pack()
    moovFrame.pack(pady=20,)
    moovFrame = tkinter.LabelFrame(mainFrame)
    moovLabel = customtkinter.CTkLabel(mainFrame,text_color="white",text="R🎯TE",font=('Arial bold',30))
    moovFrame.pack(padx=30, pady=0)
    moovLabel.place(x=50, y=20)
    class ratings():
        Rate = customtkinter.CTkLabel(mainFrame,text_color='white', text="Stars:")
        Rate.pack(padx=10,pady=10)
        Rate.place(x=37, y=75)
        rateMoov = customtkinter.CTkComboBox(mainFrame,values=(["✰✰✰✰✰✰✰","✰✰✰✰✰✰", "✰✰✰✰✰", "✰✰✰✰", "✰✰✰", "✰✰","✰"]))
        rateMoov.pack(padx=0, pady=0)
        rateMoov.place(x=37, y=100)
    def enter():
        enterData = ratings.rateMoov.get()
        enterFeed = feedText.feedback.get()
        enterFeedEmail = feedText.email.get()
        if enterFeed == enterFeed:
            if enterData == enterData:
                print(enterData)
                if enterFeedEmail == enterFeedEmail:
                    print(enterFeedEmail)
            print(enterFeed)
            conn = sqlite3.connect('moov.db')
            cursor = conn.cursor()
            createTable = ''' CREATE TABLE IF NOT EXISTS moov_db
                            (rateMoov TEXT, feedback TEXT,email TEXT)'''
            cursor.execute(createTable)
            cursor.execute('''INSERT INTO moov_db VALUES(?,?,?)''',
            (ratings.rateMoov.get(), 
            feedText.feedback.get(),
            feedText.email.get(),
            ))
        else:
            conn.close()
        conn.commit() 
        conn.close()
        if enterData == "✰✰✰✰✰✰✰":
            if enterFeed == "":
                if enterFeedEmail == "":
                    messagebox.showwarning(title="Error",message="Required fields are missing")
                    print("Error.ratings") 
    Enter_btn = customtkinter.CTkButton(mainFrame,text_color="white", text="Enter", command=enter)
    Enter_btn.pack(padx=30, pady=100)
    Enter_btn.place(x=37,y=350)
    class feedText():
        feedbackLabel = customtkinter.CTkLabel(mainFrame,text_color='white',text="Comment:")
        feedback = customtkinter.CTkEntry(mainFrame)
        feedbackLabel.place(x=37, y=220)
        feedback.place(x=37, y=247)
        emailLabel = customtkinter.CTkLabel(mainFrame,text_color='white',text="Email:")
        email = customtkinter.CTkEntry(mainFrame)
        emailLabel.place(x=37, y=280)
        email.place(x=37, y=305)
        def clear():
            feedText.feedback.delete(0,END)
            feedText.email.delete(0,END)
        Clear_btn = customtkinter.CTkButton(mainFrame,text_color="white", text="Clear", command=clear)
        Clear_btn.pack(padx=30,pady=100)
        Clear_btn.place(x=37,y=400)
        def callback():
            webbrowser.open_new_tab("www.netflix.com")
        netflixBtn = customtkinter.CTkButton(mainFrame,fg_color="red",hover_color="#ef473a",text_color="white", text="NETFLIX",command=callback)
        netflixBtn.pack(padx=50,pady=50)
        netflixBtn.place(x=37,y=140)
        def hulu():
            webbrowser.open_new_tab("www.hulu.com")
        huluBtn = customtkinter.CTkButton(mainFrame,fg_color="#0f9b0f",hover_color="#52c234",text_color="white", text="HULU",command=hulu)
        huluBtn.pack(padx=50,pady=50)
        huluBtn.place(x=37,y=180)
        
def audPage():
    audFrame = tk.Frame(mainFrame)
    lb = tk.Label(audFrame)
    lb.pack()
    audFrame.pack(pady=20,)
    moovFrame = tkinter.LabelFrame(mainFrame)
    moovLabel = customtkinter.CTkLabel(mainFrame,text_color="white",text="R🎯TE",font=('Arial bold',30))
    moovFrame.pack(padx=30, pady=0)
    moovLabel.place(x=50, y=20)
    if homeBtn == homeBtn:
        audFrame.destroy()
    class ratings():
        Rate = customtkinter.CTkLabel(mainFrame,text_color='white', text="Stars:")
        Rate.pack(padx=10,pady=10)
        Rate.place(x=37, y=75)
        rateMoov = customtkinter.CTkComboBox(mainFrame,values=(["✰✰✰✰✰✰✰","✰✰✰✰✰✰", "✰✰✰✰✰", "✰✰✰✰", "✰✰✰", "✰✰","✰"]))
        rateMoov.pack(padx=0, pady=0)
        rateMoov.place(x=37, y=100)
    def enter():
        enterData = ratings.rateMoov.get()
        enterFeed = feedText.feedback.get()
        enterFeedEmail = feedText.email.get()
        if enterFeed == enterFeed:
            if enterData == enterData:
                print(enterData)
                if enterFeedEmail == enterFeedEmail:
                    print(enterFeedEmail)
            print(enterFeed)
            conn = sqlite3.connect('aud.db')
            cursor = conn.cursor()
            createTable = ''' CREATE TABLE IF NOT EXISTS aud_db
                            (rateMoov TEXT, feedback TEXT,email TEXT)'''
            cursor.execute(createTable)
            cursor.execute('''INSERT INTO aud_db VALUES(?,?,?)''',
            (ratings.rateMoov.get(), 
            feedText.feedback.get(),
            feedText.email.get(),
            ))
        else:
            conn.close()
        conn.commit() 
        conn.close()
        if enterData == "✰✰✰✰✰✰✰":
            if enterFeed == "":
                if enterFeedEmail == "":
                    messagebox.showwarning(title="Error",message="Required fields are missing")
                    print("Error.ratings") 
    Enter_btn = customtkinter.CTkButton(mainFrame,text_color="white", text="Enter", command=enter)
    Enter_btn.pack(padx=30, pady=100)
    Enter_btn.place(x=37,y=350)
    class feedText():
        feedbackLabel = customtkinter.CTkLabel(mainFrame,text_color='white',text="Comment:")
        feedback = customtkinter.CTkEntry(mainFrame)
        feedbackLabel.place(x=37, y=220)
        feedback.place(x=37, y=247)
        emailLabel = customtkinter.CTkLabel(mainFrame,text_color='white',text="Email:")
        email = customtkinter.CTkEntry(mainFrame)
        emailLabel.place(x=37, y=280)
        email.place(x=37, y=305)
        def clear():
            feedText.feedback.delete(0,END)
            feedText.email.delete(0,END)
        Clear_btn = customtkinter.CTkButton(mainFrame,text_color="white", text="Clear", command=clear)
        Clear_btn.pack(padx=30,pady=100)
        Clear_btn.place(x=37,y=400)
        def soundcloud():
            webbrowser.open_new_tab("www.soundcloud.com")
        netflixBtn = customtkinter.CTkButton(mainFrame,fg_color="#ff7700",hover_color="#F2994A",text_color="white", text="SoundCloud",command=soundcloud)
        netflixBtn.pack(padx=50,pady=50)
        netflixBtn.place(x=37,y=140)
        def spotify():
            webbrowser.open_new_tab("www.spotify.com")
        huluBtn = customtkinter.CTkButton(mainFrame,fg_color="#1DB954",hover_color="#8DC26F",text_color="white", text="Spotify",command=spotify)
        huluBtn.pack(padx=50,pady=50)
        huluBtn.place(x=37,y=180)
        
def podPage():
    podFrame = tk.Frame(mainFrame)
    lb = tk.Label(podFrame)
    lb.pack()
    podFrame.pack(pady=20,)
    moovFrame = tkinter.LabelFrame(mainFrame)
    moovLabel = customtkinter.CTkLabel(mainFrame,text_color="white",text="R🎯TE",font=('Arial bold',30))
    moovFrame.pack(padx=30, pady=0)
    moovLabel.place(x=50, y=20)
    class ratings():
        Rate = customtkinter.CTkLabel(mainFrame,text_color='white', text="Stars:")
        Rate.pack(padx=10,pady=10)
        Rate.place(x=37, y=75)
        rateMoov = customtkinter.CTkComboBox(mainFrame,values=(["✰✰✰✰✰✰✰","✰✰✰✰✰✰", "✰✰✰✰✰", "✰✰✰✰", "✰✰✰", "✰✰","✰"]))
        rateMoov.pack(padx=0, pady=0)
        rateMoov.place(x=37, y=100)
    def enter():
        enterData = ratings.rateMoov.get()
        enterFeed = feedText.feedback.get()
        enterFeedEmail = feedText.email.get()
        if enterFeed == enterFeed:
            if enterData == enterData:
                print(enterData)
                if enterFeedEmail == enterFeedEmail:
                    print(enterFeedEmail)
            print(enterFeed)
            conn = sqlite3.connect('pod.db')
            cursor = conn.cursor()
            createTable = ''' CREATE TABLE IF NOT EXISTS pod_db
                            (rateMoov TEXT, feedback TEXT,email TEXT)'''
            cursor.execute(createTable)
            cursor.execute('''INSERT INTO pod_db VALUES(?,?,?)''',
            (ratings.rateMoov.get(), 
            feedText.feedback.get(),
            feedText.email.get(),
            ))
        else:
            conn.close()
        conn.commit() 
        conn.close()
        if enterData == "✰✰✰✰✰✰✰":
            if enterFeed == "":
                if enterFeedEmail == "":
                    messagebox.showwarning(title="Error",message="Required fields are missing")
                    print("Error.ratings") 
    Enter_btn = customtkinter.CTkButton(mainFrame,text_color="white", text="Enter", command=enter)
    Enter_btn.pack(padx=30, pady=100)
    Enter_btn.place(x=37,y=350)
    class feedText():
        feedbackLabel = customtkinter.CTkLabel(mainFrame,text_color='white',text="Comment:")
        feedback = customtkinter.CTkEntry(mainFrame)
        feedbackLabel.place(x=37, y=220)
        feedback.place(x=37, y=247)
        emailLabel = customtkinter.CTkLabel(mainFrame,text_color='white',text="Email:")
        email = customtkinter.CTkEntry(mainFrame)
        emailLabel.place(x=37, y=280)
        email.place(x=37, y=305)
        def clear():
            feedText.feedback.delete(0,END)
            feedText.email.delete(0,END)
        Clear_btn = customtkinter.CTkButton(mainFrame,text_color="white", text="Clear", command=clear)
        Clear_btn.pack(padx=30,pady=100)
        Clear_btn.place(x=37,y=400)
        def apple():
            webbrowser.open_new_tab("www.apple.com/apple-podcasts/")
        netflixBtn = customtkinter.CTkButton(mainFrame,fg_color="purple",hover_color="#c471ed",text_color="white", text="Apple Podcasts",command=apple)
        netflixBtn.pack(padx=50,pady=50)
        netflixBtn.place(x=37,y=140)
        def hulu():
            webbrowser.open_new_tab("www.audible.com")
        huluBtn = customtkinter.CTkButton(mainFrame,fg_color="#ff7700",hover_color="#F2994A",text_color="white", text="Audible",command=hulu)
        huluBtn.pack(padx=50,pady=50)
        huluBtn.place(x=37,y=180)
        
def homepage():
    mainFrameLabel = tk.Label(mainFrame, text="R🎯TE", bg="#181818",fg="white",font=('Arial, regular',35))
    mainFrameLabel.pack(padx=100,pady=150)
    mainFrameLabel.place(x=30,y=110)
    tagLabel = customtkinter.CTkLabel(mainFrame, text="rate your favourite movies, shows, songs and podcasts", text_color="#fff",fg_color="#181818",font=('Arial, regular',8))
    tagLabel.pack(padx=100,pady=150)
    tagLabel.place(x=20,y=170)
    homeBtn = tk.Button(mainFrame,font=('Bold',15),fg="white",bd=0,bg="#181818")
    homeBtn.place(x=37, y=200)
    homeIndi = tk.Label(optionsFrame,bg="#141414")
    homeIndi.place(x=3,y=185)
    def moreInfo():
        webbrowser.open_new_tab("D:\RateApp\iTemplates\index.html")
    moreInfoBtn = customtkinter.CTkButton(mainFrame,text="Info",fg_color="#0f9b0f",hover_color="#52c234",text_color="white",command=moreInfo)
    moreInfoBtn.pack(padx=50,pady=50)
    moreInfoBtn.place(x=37,y=220)
    def faqs():
                webbrowser.open_new_tab("D:\RateApp\iTemplates\ithreecolumn.html")
    infoFaqsBtn = customtkinter.CTkButton(mainFrame,text="FAQs",fg_color="#0f9b0f",hover_color="#52c234",text_color="white",command=faqs)
    infoFaqsBtn.pack(padx=50,pady=50)
    infoFaqsBtn.place(x=37,y=270)
    def contact():
                webbrowser.open_new_tab("D:\RateApp\iTemplates\itwocolumn1.html")
    contactBtn = customtkinter.CTkButton(mainFrame,text="Contact",fg_color="#0f9b0f",hover_color="#52c234",text_color="white",command=contact)
    contactBtn.pack(padx=50,pady=50)
    contactBtn.place(x=37,y=320)
root.mainloop()


