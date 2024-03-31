import tkinter as tk
from tkinter import*
import time
chatbot=tk.Tk()
entry=tk.Entry(chatbot)
chatbot.geometry("500x500")
chatbot.title("Chatbot")
chatbot.iconbitmap("chatbot icon.ico")
entry.pack()
hello = [("hello")]
question_1 = [("who are you")]
question_2 = [("tell me time")]
question_3 = [("tell me physical education exercises")]
bye = [("bye")]
def CHATBOT():
    if (entry.get()) in hello:
        label_1 = tk.Label (chatbot, text="Hi ask what you want")
        label_1["compound"] = tk.LEFT,
        label_1["image"] = bot_icon
        label_1.pack()
        return hello
    if (entry.get()) in question_1:
        label_1 = tk.Label (chatbot, text="I am python chatbot")
        label_1["compound"] = tk.LEFT,
        label_1["image"] = bot_icon
        label_1.pack()
        return question_1 
    if (entry.get()) in question_2:
        time_object = time.localtime()
        local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
        label_1 = tk.Label (chatbot, text=local_time)
        label_1["compound"] = tk.LEFT,
        label_1["image"] = bot_icon
        label_1.pack()
        return question_2 
    if (entry.get()) in question_3:
        label_1 = tk.Label(chatbot, text="Some examples of physical education activities include running,playing ball.")
        label_1["compound"] = tk.LEFT,
        label_1["image"] = bot_icon
        label_1.pack()
        return question_3
    if (entry.get()) in bye:
        label_1 = tk.Label(chatbot, text="Have a nice day bye.")
        label_1["compound"] = tk.LEFT,
        label_1["image"] = bot_icon
        label_1.pack()
        return bye
bot_icon = tk.PhotoImage(file="chatbot.png")
Send_image=PhotoImage(file="send.png")
image_label = Label(image=Send_image)
Send=Button(chatbot,image=Send_image, command=CHATBOT).pack()
chatbot.mainloop()