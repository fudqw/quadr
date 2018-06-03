# -*- coding: utf-8 -*-
import tkinter as tk
import sys
import glob
import serial as serial
import time
import tensorflow as tf
import threading
import camtest


class Thread(threading.Thread):
  
  def __init__(self,st,high):
         super(Thread, self).__init__()
          
         self.high=high
         self.total=0

  def getst(self):
    return st
         
  def run(self):
    st=camtest.Stream(2,2)
    self.st=st
    st.run()
    
#thread1 = Thread(0,500000)
#try:
#  thread1.start() # This actually causes the thread to run
#except:
#   print ("Error: unable to start thread")


walking=0

RightLeftCounter = 370
FL1=350
FL2=350
FR1=350
FR2=350
BL1=350
BL2=350
BR1=350
BR2=350
CHT=350
WST=350
delay=0.5

FL1min=130
FL1max=650
FL2min=130
FL2max=650
FR1min=130
FR1max=650
FR2min=130
FR2max=650
BL1min=130
BL1max=650
BL2min=130
BL2max=650
BR1min=130
BR1max=650
BR2min=130
BR2max=650
CHTmin=130
CHTmax=650
WSTmin=200
WSTmax=650

FL1av=350
FL2av=350
FR1av=350
FR2av=350
BL1av=350
BL2av=350
BR1av=350
BR2av=350
CHTav=350
WSTav=350

##FL1=FL1av
##FL2=FL2av
##FR1=FR1av
##FR2=FR2av
##BL1=BL1av
##BL2=BL2av
##BR1=BR1av
##BR2=BR2av
##CHT=CHTav
##WST=WSTav


stepsize=4


class App:
  def __init__(self, master, ser):
 
    self.ser  = ser
    self.button = tk.Button(master, 
                         text="QUIT", fg="red",
                         command=quit)
    self.num = FL1av
    self.button.grid(row=11, column=8, padx=0, pady=0, sticky="nw")

    ####LABELS
    self.label = tk.Label(master, 
                         text="FL1", fg="red")

    self.label.grid(row=1, column=0, padx=0, pady=0, sticky="nw")

    self.label = tk.Label(master, 
                         text="FL2", fg="red")
    self.label.grid(row=2, column=0, padx=0, pady=0, sticky="nw")

    self.label = tk.Label(master, 
                         text="FR1", fg="red")
    self.label.grid(row=1, column=7, padx=0, pady=0, sticky="nw")
    self.label = tk.Label(master, 
                         text="FR2", fg="red")
    self.label.grid(row=2, column=7, padx=0, pady=0, sticky="nw")
    self.label = tk.Label(master, 
                         text=" ", fg="red")
    self.label.grid(row=4, column=0, padx=0, pady=0, sticky="nw")
    
    self.label = tk.Label(master, 
                         text="BL1", fg="red")
    
    self.label.grid(row=5, column=0, padx=0, pady=0, sticky="nw")
    self.label = tk.Label(master, 
                         text="BL2", fg="red")
    self.label.grid(row=6, column=0, padx=0, pady=0, sticky="nw")
    self.label = tk.Label(master, 
                         text="BR1", fg="red")
    self.label.grid(row=5, column=7, padx=0, pady=0, sticky="nw")
    self.label = tk.Label(master, 
                         text="BR2", fg="red")
    self.label.grid(row=6, column=7, padx=0, pady=0, sticky="nw")


    self.label = tk.Label(master, 
                         text=" ", fg="red")
    self.label.grid(row=8, column=0, padx=0, pady=0, sticky="nw")
    
    self.label = tk.Label(master, 
                         text="CHEST", fg="red")
    self.label.grid(row=9, column=0, padx=0, pady=0, sticky="nw")
    self.label = tk.Label(master, 
                         text="WAIST", fg="red")
    self.label.grid(row=10, column=0, padx=0, pady=0, sticky="nw")
    ###############################################


    #self.entry = tk.Entry(master, 
    #                     text="0.5", fg="black")
    #self.entry.grid(row=1, column=8, padx=0, pady=0, sticky="nw")

  ###############################################
#FRONT LEG L
  ###############################################


    

    self.slogan = tk.Button(master,
                         text="Reset",
                         command=self.writeFL1_reset)
    self.slogan.grid(row=1, column=4, padx=0, pady=0, sticky="nw")

    self.Left = tk.Button(master,
                         text="←",padx=10,
                         command=self.writeFL1_Left)
    self.Left.grid(row=1, column=1, padx=0, pady=0, sticky="nw")

    self.Right = tk.Button(master,
                         text="→",padx=10,
                         command=self.writeFL1_Right)
    self.Right.grid(row=1, column=6, padx=0, pady=0, sticky="nw")

    ###############################################


    self.button.grid(row=2, column=0, padx=0, pady=0, sticky="nw")

    self.slogan = tk.Button(master,
                         text="Reset",
                         command=self.writeFL2_reset)
    self.slogan.grid(row=2, column=4, padx=0, pady=0, sticky="nw")

    self.Left = tk.Button(master,
                         text="←",padx=10,
                         command=self.writeFL2_Left)
    self.Left.grid(row=2, column=1, padx=0, pady=0, sticky="nw")

    self.Right = tk.Button(master,
                         text="→",padx=10,
                         command=self.writeFL2_Right)
    self.Right.grid(row=2, column=6, padx=2, pady=0, sticky="nw")

    ###############################################
  ###############################################
#FRONT LEG R
  ###############################################

    self.button.grid(row=1, column=8, padx=0, pady=0, sticky="nw")

    self.slogan = tk.Button(master,
                         text="Reset",
                         command=self.writeFR1_reset)
    self.slogan.grid(row=1, column=9, padx=0, pady=0, sticky="nw")

    self.Left = tk.Button(master,
                         text="←",padx=10,
                         command=self.writeFR1_Left)
    self.Left.grid(row=1, column=8, padx=0, pady=0, sticky="nw")

    self.Right = tk.Button(master,
                         text="→",padx=10,
                         command=self.writeFR1_Right)
    self.Right.grid(row=1, column=10, padx=2, pady=0, sticky="nw")

    ###############################################


    self.button.grid(row=2, column=0, padx=0, pady=0, sticky="nw")

    self.slogan = tk.Button(master,
                         text="Reset",
                         command=self.writeFR2_reset)
    self.slogan.grid(row=2, column=9, padx=0, pady=0, sticky="nw")

    self.Left = tk.Button(master,
                         text="←",padx=10,
                         command=self.writeFR2_Left)
    self.Left.grid(row=2, column=8, padx=0, pady=0, sticky="nw")

    self.Right = tk.Button(master,
                         text="→",padx=10,
                         command=self.writeFR2_Right)
    self.Right.grid(row=2, column=10, padx=2, pady=0, sticky="nw")

    ###############################################

#BACK LEG L
    self.button.grid(row=5, column=0, padx=0, pady=0, sticky="nw")

    self.slogan = tk.Button(master,
                         text="Reset",
                         command=self.writeBL1_reset)
    self.slogan.grid(row=5, column=4, padx=0, pady=0, sticky="nw")

    self.Left = tk.Button(master,
                         text="←",padx=10,
                         command=self.writeBL1_Left)
    self.Left.grid(row=5, column=1, padx=0, pady=0, sticky="nw")

    self.Right = tk.Button(master,
                         text="→",padx=10,
                         command=self.writeBL1_Right)
    self.Right.grid(row=5, column=6, padx=2, pady=0, sticky="nw")

    ###############################################


    self.button.grid(row=6, column=0, padx=0, pady=0, sticky="nw")

    self.slogan = tk.Button(master,
                         text="Reset",
                         command=self.writeBL2_reset)
    self.slogan.grid(row=6, column=4, padx=0, pady=0, sticky="nw")

    self.Left = tk.Button(master,
                         text="←",padx=10,
                         command=self.writeBL2_Left)
    self.Left.grid(row=6, column=1, padx=0, pady=0, sticky="nw")

    self.Right = tk.Button(master,
                         text="→",padx=10,
                         command=self.writeBL2_Right)
    self.Right.grid(row=6, column=6, padx=2, pady=0, sticky="nw")

    ###############################################
#BACK LEG R

    self.button.grid(row=5, column=0, padx=0, pady=0, sticky="nw")

    self.slogan = tk.Button(master,
                         text="Reset",
                         command=self.writeBR1_reset)
    self.slogan.grid(row=5, column=9, padx=0, pady=0, sticky="nw")

    self.Left = tk.Button(master,
                         text="←",padx=10,
                         command=self.writeBR1_Left)
    self.Left.grid(row=5, column=8, padx=0, pady=0, sticky="nw")

    self.Right = tk.Button(master,
                         text="→",padx=10,
                         command=self.writeBR1_Right)
    self.Right.grid(row=5, column=10, padx=2, pady=0, sticky="nw")

 ###############################################


    self.button.grid(row=6, column=0, padx=0, pady=0, sticky="nw")

    self.slogan = tk.Button(master,
                         text="Reset",
                         command=self.writeBR2_reset)
    self.slogan.grid(row=6, column=9, padx=0, pady=0, sticky="nw")

    self.Left = tk.Button(master,
                         text="←",padx=10,
                         command=self.writeBR2_Left)
    self.Left.grid(row=6, column=8, padx=0, pady=0, sticky="nw")

    self.Right = tk.Button(master,
                         text="→",padx=10,
                         command=self.writeBR2_Right)
    self.Right.grid(row=6, column=10, padx=2, pady=0, sticky="nw")

    ###############################################
#CHEST WAIST
    ###############################################


    self.button.grid(row=8, column=0, padx=0, pady=0, sticky="nw")

    self.slogan = tk.Button(master,
                         text="Reset",
                         command=self.writeCHT_reset)
    self.slogan.grid(row=9, column=4, padx=0, pady=0, sticky="nw")

    self.Left = tk.Button(master,
                         text="←",padx=10,
                         command=self.writeCHT_Left)
    self.Left.grid(row=9, column=1, padx=0, pady=0, sticky="nw")

    self.Right = tk.Button(master,
                         text="→",padx=10,
                         command=self.writeCHT_Right)
    self.Right.grid(row=9, column=6, padx=2, pady=0, sticky="nw")

    ###############################################


    self.button.grid(row=10, column=0, padx=0, pady=0, sticky="nw")

    self.slogan = tk.Button(master,
                         text="Reset",
                         command=self.writeWST_reset)
    self.slogan.grid(row=10, column=4, padx=0, pady=0, sticky="nw")

    self.Left = tk.Button(master,
                         text="←",padx=10,
                         command=self.writeWST_Left)
    self.Left.grid(row=10, column=1, padx=0, pady=0, sticky="nw")

    self.Right = tk.Button(master,
                         text="→",padx=10,
                         command=self.writeWST_Right)
    self.Right.grid(row=10, column=6, padx=2, pady=0, sticky="nw")

    ###############################################
    #self.button.grid(row=10, column=6, padx=0, pady=0, sticky="nw")

    #self.slogan = tk.Button(master,
    #                     text="Open Loop Pick",
    #                     command=self.Oloop_pick)
    #self.slogan.grid(row=10, column=8, padx=0, pady=0, sticky="nw")

    ###############################################

    ###############################################
    self.button.grid(row=11, column=15, padx=0, pady=0, sticky="nw")
    

    self.slogan = tk.Button(master,
                         text="Tracking",
                         command=self.tracking)
    self.slogan.grid(row=11, column=15, padx=0, pady=0, sticky="nw")

    ###############################################

     ###############################################
    self.button.grid(row=11, column=18, padx=0, pady=0, sticky="nw")
    

    self.toggleb = tk.Button(master,
                         text="WALK",
                         command=self.toggle)
    self.toggleb.grid(row=1, column=18, padx=0, pady=0, sticky="nw")

    ###############################################

  def toggle(self):
    '''
    use
    t_btn.config('text')[-1]
    to get the present state of the toggle button
    '''
    global walking
    if self.toggleb.config('text')[-1] == 'WALK':
        self.toggleb.config(text='STOP')
        walking=0
        
    else:
        self.toggleb.config(text='WALK')
        walking=1
        print('walking')

  def tracking(self):
    global CHT
    global WST
    xval=thread1.st.getY()
    print (xval)
    yval=thread1.st.getX()
    print (yval)
    if (xval>250):
      self.writeCHT_Left()
    else:
      if (xval<350):
        self.writeCHT_Right()

    if (yval<150):
      self.writeWST_Left()
    else:
      if (yval>250):
        self.writeWST_Right()

  def Oloop_pick(self):
    global FL1
    global FL2
    global FR1
    global FR2
    global BL1
    global BL2
    global BR1

     
      
      
    print(FL1)
    print (self.ser.readline())
 

    
  
    
  def write_Left(self):
    global RightLeftCounter
    if (RightLeftCounter>0):
      RightLeftCounter -=stepsize
    self.ser.write(bytearray(RightLeftCounter))
    print(RightLeftCounter)
    print (self.ser.readline())
 
  def write_Right(self):
    global RightLeftCounter
    if (RightLeftCounter<180):
      RightLeftCounter +=stepsize
    self.ser.write(bytearray(RightLeftCounter))
    print(RightLeftCounter)
    print (self.ser.readline())
    
  def write_reset(self):
    global RightLeftCounter
    RightLeftCounter = 90
    print(RightLeftCounter)
    self.ser.write(bytearray(RightLeftCounter))
    print (self.ser.readline())
 
  def write_sweep(self):
    global RightLeftCounter
    for RightLeftCounter in range(0,180):
      print(RightLeftCounter)
      self.ser.write(bytearray(RightLeftCounter))
      print (self.ser.readline())
      time.sleep(0.01) # delays for 1 seconds
    RightLeftCounter = 90
    self.ser.write(bytearray(RightLeftCounter))
    
####################################################
  def convstr(self,n):
    if (n<100):
      return ('0'+str(n))
    else:
      return str(n)

    
  def writeFL1_Left(self):
    global FL1
    if (FL1>FL1min):
      FL1 -=stepsize
    self.ser.write(bytearray('FL1'+self.convstr(FL1), 'utf8'))
    print(FL1)
    print (self.ser.readline())
 
  def writeFL1_Right(self):
    global FL1
    if (FL1<FL1max):
      FL1 +=stepsize
    self.ser.write(bytearray('FL1'+self.convstr(FL1), 'utf8'))
    print(FL1)
    print (self.ser.readline())
  def writeFL1_reset(self):
    global FL1
    FL1 = FL1av
    self.ser.write(bytearray('FL1'+self.convstr(FL1), 'utf8'))
    print('FL1'+self.convstr(FL1))
    print (self.ser.readline())
 
  def writeFL1_sweep(self):
    global FL1
    for FL1 in range(0,180):
      print(FL1)
      self.ser.write(bytearray('FL1'+self.convstr(FL1), 'utf8'))
      print (self.ser.readline())
      time.sleep(0.01) # delays for 1 seconds
    FL1 = 90
    self.ser.write(bytearray('FL1'+self.convstr(FL1), 'utf8'))

    ####################################################

  def writeFL2_Left(self):
    global FL2
    if (FL2>FL2min):
      FL2 -=stepsize
    self.ser.write(bytearray('FL2'+self.convstr(FL2), 'utf8'))
    print(FL2)
    print (self.ser.readline())
 
  def writeFL2_Right(self):
    global FL2
    if (FL2<FL2max):
      FL2 +=stepsize
    self.ser.write(bytearray('FL2'+self.convstr(FL2), 'utf8'))
    print(FL2)
    print (self.ser.readline())
  def writeFL2_reset(self):
    global FL2
    FL2 = FL2av
    self.ser.write(bytearray('FL2'+self.convstr(FL2), 'utf8'))
    print('FL2'+self.convstr(FL2))
    print (self.ser.readline())
 
  def writeFL2_sweep(self):
    global FL2
    for FL2 in range(0,280):
      print(FL2)
      self.ser.write(bytearray('FL2'+self.convstr(FL2), 'utf8'))
      print (self.ser.readline())
      time.sleep(0.01) # delays for 1 seconds
    FL1 = 90
    self.ser.write(bytearray('FL2'+self.convstr(FL2), 'utf8'))


    ####################################################

  def writeFR1_Left(self):
    global FR1
    if (FR1>FR1min):
      FR1 -=stepsize
    self.ser.write(bytearray('FR1'+self.convstr(FR1), 'utf8'))
    print(FR1)
    print (self.ser.readline())
 
  def writeFR1_Right(self):
    global FR1
    if (FR1<FR1max):
      FR1 +=stepsize
    self.ser.write(bytearray('FR1'+self.convstr(FR1), 'utf8'))
    print(FR1)
    print (self.ser.readline())
  def writeFR1_reset(self):
    global FR1
    FR1 = FR1av
    self.ser.write(bytearray('FR1'+self.convstr(FR1), 'utf8'))
    print('FR1'+self.convstr(FR1))
    print (self.ser.readline())
 
  def writeFR1_sweep(self):
    global FR1
    for FR1 in range(0,380):
      print(FR1)
      self.ser.write(bytearray('FR1'+self.convstr(FR1), 'utf8'))
      print (self.ser.readline())
      time.sleep(0.01) # delays for 1 seconds
    FL1 = 90
    self.ser.write(bytearray('FR1'+self.convstr(FR1), 'utf8'))

    
    ####################################################

  def writeFR2_Left(self):
    global FR2
    if (FR2>FR2min):
      FR2 -=stepsize
    self.ser.write(bytearray('FR2'+self.convstr(FR2), 'utf8'))
    print(FR2)
    print (self.ser.readline())
 
  def writeFR2_Right(self):
    global FR2
    if (FR2<FR2max):
      FR2 +=stepsize
    self.ser.write(bytearray('FR2'+self.convstr(FR2), 'utf8'))
    print(FR2)
    print (self.ser.readline())
  def writeFR2_reset(self):
    global FR2
    FR2 = FR2av
    self.ser.write(bytearray('FR2'+self.convstr(FR2), 'utf8'))
    print('FR2'+self.convstr(FR2))
    print (self.ser.readline())
 
  def writeFR2_sweep(self):
    global FR2
    for FR2 in range(0,480):
      print(FR2)
      self.ser.write(bytearray('FR2'+self.convstr(FR2), 'utf8'))
      print (self.ser.readline())
      time.sleep(0.01) # delays for 1 seconds
    FL1 = 90
    self.ser.write(bytearray('FR2'+self.convstr(FR2), 'utf8'))

    
    ####################################################

  def writeBL1_Left(self):
    global BL1
    if (BL1>BL1min):
      BL1 -=stepsize
    self.ser.write(bytearray('BL1'+self.convstr(BL1), 'utf8'))
    print(BL1)
    print (self.ser.readline())
 
  def writeBL1_Right(self):
    global BL1
    if (BL1<BL1max):
      BL1 +=stepsize
    self.ser.write(bytearray('BL1'+self.convstr(BL1), 'utf8'))
    print(BL1)
    print (self.ser.readline())
  def writeBL1_reset(self):
    global BL1
    BL1 = BL1av
    self.ser.write(bytearray('BL1'+self.convstr(BL1), 'utf8'))
    print('BL1'+self.convstr(BL1))
    print (self.ser.readline())
 
  def writeBL1_sweep(self):
    global BL1
    for BL1 in range(0,580):
      print(BL1)
      self.ser.write(bytearray('BL1'+self.convstr(BL1), 'utf8'))
      print (self.ser.readline())
      time.sleep(0.01) # delays for 1 seconds
    FL1 = 90
    self.ser.write(bytearray('BL1'+self.convstr(BL1), 'utf8'))

####################################################

  def writeBL2_Left(self):
    global BL2
    if (BL2>BL2min):
      BL2 -=stepsize
    self.ser.write(bytearray('BL2'+self.convstr(BL2), 'utf8'))
    print(BL2)
    print (self.ser.readline())
 
  def writeBL2_Right(self):
    global BL2
    if (BL2<BL2max):
      BL2 +=stepsize
    self.ser.write(bytearray('BL2'+self.convstr(BL2), 'utf8'))
    print(BL2)
    print (self.ser.readline())
  def writeBL2_reset(self):
    global BL2
    BL2 = BL2av
    self.ser.write(bytearray('BL2'+self.convstr(BL2), 'utf8'))
    print('BL2'+self.convstr(BL2))
    print (self.ser.readline())
 
  def writeBL2_sweep(self):
    global BL2
    for BL2 in range(0,680):
      print(BL2)
      self.ser.write(bytearray('BL2'+self.convstr(BL2), 'utf8'))
      print (self.ser.readline())
      time.sleep(0.01) # delays for 1 seconds
    FL1 = 90
    self.ser.write(bytearray('BL2'+self.convstr(BL2), 'utf8'))
    

    
    ####################################################

  def writeBR1_Left(self):
    global BR1
    if (BR1>BR1min):
      BR1 -=stepsize
    self.ser.write(bytearray('BR1'+self.convstr(BR1), 'utf8'))
    print(BR1)
    print (self.ser.readline())
 
  def writeBR1_Right(self):
    global BR1
    if (BR1<BR1max):
      BR1 +=stepsize
    self.ser.write(bytearray('BR1'+self.convstr(BR1), 'utf8'))
    print(BR1)
    print (self.ser.readline())
  def writeBR1_reset(self):
    global BR1
    BR1 = BR1av
    self.ser.write(bytearray('BR1'+self.convstr(BR1), 'utf8'))
    print('BR1'+self.convstr(BR1))
    print (self.ser.readline())
 
  def writeBR1_sweep(self):
    global BR1
    for BR1 in range(0,780):
      print(BR1)
      self.ser.write(bytearray('BR1'+self.convstr(BR1), 'utf8'))
      print (self.ser.readline())
      time.sleep(0.01) # delays for 1 seconds
    FL1 = 90
    self.ser.write(bytearray('BR1'+self.convstr(BR1), 'utf8'))
    ####################################################

  def writeBR2_Left(self):
    global BR2
    if (BR2>BR2min):
      BR2 -=stepsize
    self.ser.write(bytearray('BR2'+self.convstr(BR2), 'utf8'))
    print(BR2)
    print (self.ser.readline())
 
  def writeBR2_Right(self):
    global BR2
    if (BR2<BR2max):
      BR2 +=stepsize
    self.ser.write(bytearray('BR2'+self.convstr(BR2), 'utf8'))
    print(BR2)
    print (self.ser.readline())
  def writeBR2_reset(self):
    global BR2
    BR2 = BR2av
    self.ser.write(bytearray('BR2'+self.convstr(BR2), 'utf8'))
    print('BR2'+self.convstr(BR2))
    print (self.ser.readline())
 
  def writeBR2_sweep(self):
    global BR2
    for BR2 in range(0,780):
      print(BR2)
      self.ser.write(bytearray('BR2'+self.convstr(BR2), 'utf8'))
      print (self.ser.readline())
      time.sleep(0.01) # delays for 1 seconds
    FL1 = 90
    self.ser.write(bytearray('BR2'+self.convstr(BR2), 'utf8'))
    
    ####################################################
    ####################################################

  def writeCHT_Left(self):
    global CHT
    if (CHT>CHTmin):
      CHT -=stepsize
    self.ser.write(bytearray('CHT'+self.convstr(CHT), 'utf8'))
    print(CHT)
    print (self.ser.readline())
 
  def writeCHT_Right(self):
    global CHT
    if (CHT<CHTmax):
      CHT +=stepsize
    self.ser.write(bytearray('CHT'+self.convstr(CHT), 'utf8'))
    print(CHT)
    print (self.ser.readline())
  def writeCHT_reset(self):
    global CHT
    CHT = CHTav
    self.ser.write(bytearray('CHT'+self.convstr(CHT), 'utf8'))
    print('CHT'+self.convstr(CHT))
    print (self.ser.readline())
 
  def writeCHT_sweep(self):
    global CHT
    for CHT in range(0,1480):
      print(CHT)
      self.ser.write(bytearray('CHT'+self.convstr(CHT), 'utf8'))
      print (self.ser.readline())
      time.sleep(0.01) # delays for 1 seconds
    FL1 = 90
    self.ser.write(bytearray('CHT'+self.convstr(CHT), 'utf8'))

    
    ####################################################

  def writeWST_Left(self):
    global WST
    if (WST>WSTmin):
      WST -=stepsize
    self.ser.write(bytearray('WST'+self.convstr(WST), 'utf8'))
    print(WST)
    print (self.ser.readline())
 
  def writeWST_Right(self):
    global WST
    if (WST<WSTmax):
      WST +=stepsize
    self.ser.write(bytearray('WST'+self.convstr(WST), 'utf8'))
    print(WST)
    print (self.ser.readline())
  def writeWST_reset(self):
    global WST
    WST = WSTav
    self.ser.write(bytearray('WST'+self.convstr(WST), 'utf8'))
    print('WST'+self.convstr(WST))
    print (self.ser.readline())
 
  def writeWST_sweep(self):
    global WST
    for WST in range(0,1580):
      print(WST)
      self.ser.write(bytearray('WST'+self.convstr(WST), 'utf8'))
      print (self.ser.readline())
      time.sleep(0.01) # delays for 1 seconds
    FL1 = 90
    self.ser.write(bytearray('WST'+self.convstr(WST), 'utf8'))
    

  def updat():
    
    threading.Timer(1, updat()).start() #####
    #self.tracking()

def main():
  
  root = tk.Tk()
  root.title("TEST")
  root.geometry("800x500+100+100")
  

  
  #test=thread1.st.getY()
  #print (test)
  

  ser = serial.Serial()
  ser.port = 'COM5'
  ser.baudrate = 9600
  ser.timeout = 0
  # open port if not already open
  if ser.isOpen() == False:
    ser.open()
  app = App(root,ser)  
  root.mainloop()
  #app.updat
 
if __name__ == '__main__':
  main()
