import tkinter as tk
from tkinter import filedialog
from multiprocessing import Process
from multiprocessing import Pool
import os 


root = tk.Tk()

MainFrame = tk.Frame(root, width=385, height=460, relief='raised', borderwidth=5)
LabelFrame = tk.Frame(MainFrame, width=375, height=115, relief='raised', borderwidth=5)
ButtonFrame = tk.Frame(MainFrame, width=375, height=330, relief='raised', borderwidth=5)


choosen = tk.Label(LabelFrame, text=' ',font=25,fg="Green")
q_button = tk.Button(ButtonFrame, text='Quitter',font=25 , command=root.destroy)


def getpath():
   file_path = filedialog.askopenfilename()
   text = choosen.cget("text") + file_path + "\n"
   choosen.configure(text=text)
   print(file_path)
B = tk.Button(ButtonFrame, text ="Choisissez les fichiers csc",font=25, command = getpath)


def runDockerGUI():
   p = os.system('sudo docker run -it --rm -e DISPLAY --net=host -v "$HOME:$HOME" sbungartz/cooja ant run')
runDockerGUIbutton = tk.Button(ButtonFrame, text ="Lancer Cooja GUI ",font=25 ,command = runDockerGUI)



def runMuptipleCSC():
   def runcsc( nom ):
   	 command = "sudo docker run -it --rm -v '$HOME:$HOME' -e RUNDIR='$PWD'  sbungartz/cooja ant run -Dargs='-nogui=$PWD/"+nom+"' > "+nom+".res "
   	 print(command)
   	 p = os.system("gnome-terminal -e 'bash -c \" "+command+" ; exec bash\"'")
   a = choosen.cget("text")
   # a c'est tout les fichiers selectionnés dans une seul string
   last = []
   p1 = Pool()
   for i in a.splitlines():
   	   # i c'est une line c a dire un chemain un fichier a executé
   	   print(i.split("/")[-1])
   	   last.append(i.split("/")[-1])
   	   # -1 veut dire le dernier element 
   for i in range(len(last)):
	   p1=Process(target=runcsc,args=(last[i],))
	   p1.start()
	   p1.join()


runMuptipleCSCbutton = tk.Button(ButtonFrame, text ="Lancer l'enssemble CSC",font=22, command = runMuptipleCSC)

for frame in [MainFrame, LabelFrame, ButtonFrame, B, choosen, runDockerGUIbutton, runMuptipleCSCbutton]:
    frame.pack(expand=True, fill='both')
    frame.pack_propagate(0)

for widget in [ q_button, choosen]:
    widget.pack(expand=True, fill='x', anchor='s')





root.mainloop()

