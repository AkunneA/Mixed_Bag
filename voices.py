import speech_recognition as sr
import tkinter as tk
import tkinter.font

recog=sr.Recognizer()
mic=sr.Microphone(2) #2 is set for my microphone, if this is left blank it uses the default
#print(mic.list_microphone_names()) #choose a microphone to use
window= tk.Tk()

T=tk.Text(window, height=800, width=600)
with mic as source:
    audio=recog.listen(source)

T.pack()

font_set = tkinter.font.Font( family = "Impact",
                                 size = 45,
                                 weight = "bold")
T.configure(font=font_set)
T.insert(tk.END, recog.recognize_google(audio))

tk.mainloop()
