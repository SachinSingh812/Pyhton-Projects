


def frame2():
    root.destroy()
    def frame3():
        f2.destroy()
        
        third=tkinter.Tk()
        third.title('Picture Game:Quiz Your Knowledge')
        third.geometry('1000x800+150+0')
        third.maxsize(width=1000,height=695)
        third.minsize(width=1000,height=695)
        third.configure(bg='white')

        photo7=tkinter.PhotoImage(file="line.png")
        label7=tkinter.Button(third,image=photo7,borderwidth='0').place(x=70,y=380)

        photo8=tkinter.PhotoImage(file="load.png")
        label8=tkinter.Button(third,image=photo8,borderwidth='0',highlightthickness='0').place(x=60,y=180)

        photo9=tkinter.PhotoImage(file="load.png")
        label9=tkinter.Button(third,image=photo9,borderwidth='0',highlightthickness='0').place(x=270,y=180)

        photo10=tkinter.PhotoImage(file="load.png")
        label10=tkinter.Button(third,image=photo10,borderwidth='0',highlightthickness='0').place(x=60,y=410)

        photo11=tkinter.PhotoImage(file="load.png")
        label11=tkinter.Button(third,image=photo11,borderwidth='0',highlightthickness='0').place(x=270,y=410)

        photo12=tkinter.PhotoImage(file="load.png")
        label12=tkinter.Button(third,image=photo12,borderwidth='0',highlightthickness='0').place(x=490,y=180)

        photo13=tkinter.PhotoImage(file="load.png")
        label13=tkinter.Button(third,image=photo13,borderwidth='0',highlightthickness='0').place(x=490,y=410)

        total = tkinter.IntVar()

        def correct():
            l4=tkinter.Label(third,width=2,height=5,bg='green').place(x=750,y=300)
            counter()

        def incorrect():
            l3=tkinter.Label(third,width=2,height=5,bg='red').place(x=750,y=300)
    
        def counter():
            total.set(total.get() + 20)
            
        def disable3():
            b3.config(state=DISABLED)
        def disable4():
            b4.config(state=DISABLED)
        def disable7():
            b7.config(state=DISABLED)
        def disable8():
            b8.config(state=DISABLED)
        def disable9():
            b9.config(state=DISABLED)
        def disable10():
            b10.config(state=DISABLED)
            
        

   
        def level1():
    
 
            l1 =["snake.png", "shark.png","skull.png","banana.png","car.png","boy.png"]
            ph3.configure(file=l1[0])
            ph4.configure(file=l1[1])
            ph5.configure(file=l1[2])
            ph6.configure(file=l1[3])
            ph7.configure(file=l1[4])
            ph8.configure(file=l1[5])
            
            l1=tkinter.Label(third, text="Score:",width=10,height=2,bg='blue',fg='white',font=('none',12,'bold')).place(x=350,y=40)
            l2=tkinter.Label(third, textvariable=total,width=5,height=2,font=('none',12,'bold')).place(x=450,y=40)

        def enable():
            b1.config(state=ACTIVE)
            b2.config(state=ACTIVE)
            b3.config(state=ACTIVE)
            b4.config(state=ACTIVE)
            b5.config(state=ACTIVE)
            b6.config(state=ACTIVE)
            b7.config(state=ACTIVE)
            b8.config(state=ACTIVE)
            b9.config(state=ACTIVE)
            b10.config(state=ACTIVE)


        

        p1=tkinter.PhotoImage(file='wtr.png')    
        b1=tkinter.Button(third,image=p1,borderwidth=0,highlightthickness=0,command=incorrect,state=DISABLED)
        b1.place(x=800,y=80)
        p2=tkinter.PhotoImage(file='cld.png')
        b2=tkinter.Button(third,image=p2,borderwidth=0,highlightthickness=0,command=incorrect,state=DISABLED)
        b2.place(x=800,y=140)
        p3=tkinter.PhotoImage(file='skl.png')
        b3=tkinter.Button(third,image=p3,borderwidth=0,highlightthickness=0,command=lambda:[correct(),disable3()],state=DISABLED)
        b3.place(x=800,y=200)
        p4=tkinter.PhotoImage(file='bna.png')
        b4=tkinter.Button(third,image=p4,borderwidth=0,highlightthickness=0,command=lambda:[correct(),disable4()],state=DISABLED)
        b4.place(x=800,y=260)
        p5=tkinter.PhotoImage(file='tbl.png')
        b5=tkinter.Button(third,image=p5,borderwidth=0,highlightthickness=0,command=incorrect,state=DISABLED)
        b5.place(x=800,y=320)
        p6=tkinter.PhotoImage(file='chr.png')
        b6=tkinter.Button(third,image=p6,borderwidth=0,highlightthickness=0,command=incorrect,state=DISABLED)
        b6.place(x=800,y=380)
        p7=tkinter.PhotoImage(file='srk.png')
        b7=tkinter.Button(third,image=p7,borderwidth=0,highlightthickness=0,command=lambda:[correct(),disable7()],state=DISABLED)
        b7.place(x=800,y=440)
        p8=tkinter.PhotoImage(file='cr.png')
        b8=tkinter.Button(third,image=p8,borderwidth=0,highlightthickness=0,command=lambda:[correct(),disable8()],state=DISABLED)
        b8.place(x=800,y=500)
        p9=tkinter.PhotoImage(file='by.png')
        b9=tkinter.Button(third,image=p9,borderwidth=0,highlightthickness=0,command=lambda:[correct(),disable9()],state=DISABLED)
        b9.place(x=800,y=560)
        p10=tkinter.PhotoImage(file='snk.png')
        b10=tkinter.Button(third,image=p10,borderwidth=0,highlightthickness=0,command=lambda:[correct(),disable10()],state=DISABLED)
        b10.place(x=800,y=620)


        ph3=tkinter.PhotoImage()    
        label3=tkinter.Label(third,image=ph3,borderwidth='0')
        label3.place(x=60,y=180)

        ph4=tkinter.PhotoImage()    
        label4=tkinter.Label(third,image=ph4,borderwidth='0')
        label4.place(x=270,y=180)

        ph5=tkinter.PhotoImage()    
        label5=tkinter.Label(third,image=ph5,borderwidth='0')
        label5.place(x=60,y=410)

        ph6=tkinter.PhotoImage()    
        label6=tkinter.Label(third,image=ph6,borderwidth='0')
        label6.place(x=270,y=410)

        ph7=tkinter.PhotoImage()    
        label7=tkinter.Label(third,image=ph7,borderwidth='0')
        label7.place(x=490,y=180)

        ph8=tkinter.PhotoImage()    
        label8=tkinter.Label(third,image=ph8,borderwidth='0')
        label8.place(x=490,y=410)

        
        
        photo=tkinter.PhotoImage(file="gi.png")
        gi=tkinter.Button(third,image=photo,borderwidth='0',highlightthickness='0',command=lambda:[level1(),enable()]).place(x=50,y=40)
        
        photo2=tkinter.PhotoImage(file="s.png")
        s=tkinter.Button(third,image=photo2,borderwidth='0',highlightthickness='0',command=scr).place(x=600,y=40)


        third.mainloop()

    import tkinter
    from tkinter import ttk
    f2=tkinter.Tk()
    f2.title('Picture Game:Quiz Your Knowledge')
    f2.geometry('701x264+300+200')
    f2.maxsize(width=701,height=280)
    f2.minsize(width=701,height=280)
    photo=PhotoImage(file="second.png")
    label=Label(f2,image=photo,borderwidth='0')
    label.pack()
    pb = ttk.Progressbar(f2, orient="horizontal", length=701, mode="determinate")
    pb.pack(side=BOTTOM)
    pb.start()
    f2.after(5000,frame3)
    f2.mainloop()
    
def scr():
    import tkinter
    score=tkinter.Tk()
    score.title("Score Board")
    score.geometry('394x297+500+300')
    score.maxsize(width=394,height=297)
    score.minsize(width=394,height=297)
    pscr=tkinter.PhotoImage(file='scr.png')
    s=tkinter.Label(score,image=pscr,text='SCORE',font=('none',12,'bold')).pack()      
    score.mainloop()


from tkinter import*
root=Tk()
root.title('Picture Game:Quiz Your Knowledge')
root.geometry('275x422+500+100')
root.maxsize(width=275,height=422)
root.minsize(width=275,height=422)
root.configure(bg='white')
b1=Label(root,text=" PICTURE GAME",font=('calibri','13'),bg="white").place(x=10,y=10)   

b2=Label(root,text=" QUIZ YOUR KNOWLEDGE.",font=('calibri','10'),bg="white").place(x=10,y=30)   

photo=PhotoImage(file="1st.png")
label=Label(root,image=photo,borderwidth='0').place(x=168)

photo2=PhotoImage(file="u.png")
play=Button(root,image=photo2,borderwidth='0',highlightthickness='0',command=frame2).place(x=80,y=110)

photo3=PhotoImage(file="p1.png")
label3=Label(root,image=photo3,borderwidth='0').place(x=50,y=250)

photo4=PhotoImage(file="p2.png")
label4=Label(root,image=photo4,borderwidth='0').place(x=110,y=250)

photo5=PhotoImage(file="p3.png")
label5=Label(root,image=photo5,borderwidth='0').place(x=170,y=250)

photo1=PhotoImage(file="bot.png")
label1=Label(root,image=photo1,borderwidth='0').place(y=335)
root.mainloop()


