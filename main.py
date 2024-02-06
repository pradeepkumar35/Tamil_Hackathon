import sys,os
import random
import pyscript
from PyQt5.uic import loadUi
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent,QMediaPlaylist




op=''
anicount=0
modecount=0
mo=1
windowindex=0

class Output(QDialog):
    def __init__(self):
        global mo
        super(Output,self).__init__()
        loadUi("Output.ui",self)
        movie = QtGui.QMovie('Blue.gif')
        self.BG.setMovie(movie)
        movie.start()
        self.AO.addItem(op)
        self.finish.clicked.connect(self.gotoMenu)
        mo += 1


    def gotoMenu(self):
        global mo
        widget.addWidget(qlisttt)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Mode(QDialog):
    def __init__(self):
        super(Mode, self).__init__()
        print(widget.currentIndex())
        loadUi("Mode.ui",self)
        movie = QtGui.QMovie('Blue.gif')
        self.BG.setMovie(movie)
        movie.start()
        self.easy.clicked.connect(self.gotoeasy)
        self.intermediate.clicked.connect(self.gotointermediate)
        self.hard.clicked.connect(self.gotohard)

    def gotoeasy(self):
        global modecount
        modecount = 1
        A = Animals()
        widget.addWidget(A)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotointermediate(self):
        global modecount
        modecount = 2
        A = Animals()
        widget.addWidget(A)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotohard(self):
        global modecount
        modecount = 3
        A = Animals()
        widget.addWidget(A)
        widget.setCurrentIndex(widget.currentIndex() + 1)



class Menu(QDialog):
    def __init__(self):
        super(Menu,self).__init__()

        loadUi("Menu.ui",self)
        global anicount,mo
        movie = QtGui.QMovie('Blue.gif')
        self.BG.setMovie(movie)
        movie.start()
        self.mute.setIconSize(QtCore.QSize(51,41))
        self.mute.setIcon(QtGui.QIcon('thelast.png'))
        self.animals.clicked.connect(self.gotoAnimals)
        self.fruits.clicked.connect(self.gotoFruits)
        self.vegetables.clicked.connect(self.gotoVegetables)
        self.days.clicked.connect(self.gotoDays)
        self.planets.clicked.connect(self.gotoPlanets)
        self.months.clicked.connect(self.gotoMonths)
        self.colors.clicked.connect(self.gotoColors)
        self.action.clicked.connect(self.gotoAction)
        self.mute.clicked.connect(self.playMute)
        music_path=os.path.join(os.getcwd(),'test.mp3')
        url=QUrl.fromLocalFile(music_path)
        self.playlist = QMediaPlaylist()
        self.playlist.addMedia(QMediaContent(url))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.player = QMediaPlayer()
        self.player.setPlaylist(self.playlist)
        self.player.play()
    def playMute(self):
        self.player.setMuted(not self.player.isMuted())



    def gotoAnimals(self):
        global anicount,modecount
        anicount=1
        M = Mode()
        widget.addWidget(M)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def gotoFruits(self):
        global anicount
        anicount = 2
        M=Mode()
        widget.addWidget(M)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotoVegetables(self):
        global anicount
        anicount = 3
        M = Mode()
        widget.addWidget(M)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def gotoPlanets(self):
        global anicount
        anicount = 5
        M = Mode()
        widget.addWidget(M)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def gotoMonths(self):
        global anicount
        anicount = 6
        M = Mode()
        widget.addWidget(M)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def gotoDays(self):
        global anicount
        anicount = 4
        M = Mode()
        widget.addWidget(M)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def gotoColors(self):
        global anicount
        anicount = 7
        M = Mode()
        widget.addWidget(M)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def gotoAction(self):
        global anicount
        anicount = 8
        M = Mode()
        widget.addWidget(M)
        widget.setCurrentIndex(widget.currentIndex() + 1)



class Animals(QDialog):
    def __init__(self):
        super(Animals,self).__init__()
        loadUi("Animals.ui",self)
        global anicount,modecount
        movie = QtGui.QMovie('Blue.gif')
        self.BG.setMovie(movie)
        movie.start()
        self.dict ={"விலங்குகள்":["ஒட்டகம்","கரடி","குதிரை","சிங்கம்","நரி","நாய்","பசு","மான்","யானை","பூனை",],
      "கிரகங்கள்":["சனி","செவ்வாய்","நெப்டியூன்","புதன்","பூமி","யுரேனஸ்","வியாழன்","வெள்ளி"],
      "காய்கறிகள்":["அவரைக்காய்","கத்தரிக்காய்","காரட்","கோவைக்காய்","தக்காளி","புடலங்காய்","பூசணிக்காய்","மாங்காய்","முருங்கைக்காய்","பாகற்காய்"],
      "வண்ணங்கள்":["ஆரஞ்சு","ஊதா","கருப்பு","சிவப்பு","தங்க","நீலம்","மஞ்சள்","பச்சை","வெள்ளி","வெள்ளை"],
      "பழங்கள்":["அன்னாசிப்பழம்","ஆப்பிள்","எலுமிச்சை்ப்பழம்","தர்பூசணி","பசிப்பாழம்","பப்பாளி","பேரிக்காய்","மாதுளம் பழம்","வாழைப்பழம்","வுெண்ணைப்பழம்"],
      "கிழமைகள்":["சனிக்கிழமை","செவ்வாய் கிழமை","ஞாயிற்றுக்கிழமை","திங்கட்கிழமை","வியாழன்","வெள்ளி","புதன்"],
      "மாதங்கள்":["ஐப்பாசி","ஆடி","ஆணி","ஆவணி","கார்த்திகை","சித்திரை","பங்குனி","புரட்டாசி","மாசி","மார்கழி","வைகாசி"],
      "செயல்":["விளையாடு","குதி","சாப்பிடு","வேலை","படிப்பு","ஓட்டு","நடை","எழுது","படி","பேசு"]}
        if anicount== 1:
            Alist=self.dict.get("விலங்குகள்")
            daycount=0
        if anicount == 2:
                Alist = self.dict.get("பழங்கள்")
                daycount = 0
        if anicount == 3:
            Alist = self.dict.get("காய்கறிகள்")
            daycount = 0
        if anicount == 4:
                Alist = self.dict.get("கிழமைகள்")
                daycount = 1
        if anicount == 5:
            Alist = self.dict.get("கிரகங்கள்")
            daycount=1
        if anicount == 6:
                Alist = self.dict.get("மாதங்கள்")
                daycount = 0
        if anicount == 7:
            Alist = self.dict.get("வண்ணங்கள்")
            daycount = 0
        if anicount == 8:
            Alist = self.dict.get("செயல்")
            daycount = 0
        list = []
        self.Rlist=[]
        if modecount == 1:
          list = random.sample(Alist, 5)
          self.Rlist = list
          item1 = QListWidgetItem(list[0])
          self.A1.addItem(item1)
          item2 = QListWidgetItem(list[1])
          self.A2.addItem(item2)
          item3 = QListWidgetItem(list[2])
          self.A3.addItem(item3)
          item4 = QListWidgetItem(list[3])
          self.A4.addItem(item4)
          item5 = QListWidgetItem(list[4])
          self.A5.addItem(item5)

          for i in range(0, len(self.Rlist) - 1):
              for j in range(len(self.Rlist) - 1):
                  if (self.Rlist[j] > self.Rlist[j + 1]):
                      temp = self.Rlist[j]
                      self.Rlist[j] = self.Rlist[j + 1]
                      self.Rlist[j + 1] = temp
          self.A = [self.A1, self.A2, self.A3, self.A4, self.A5]
          self.R = [self.R1, self.R2, self.R3, self.R4, self.R5]
          self.Output = []
          self.dec = ["சிறந்த பதில்!!!", "தொடர்ந்து முயற்சி செய்யுங்கள்!!!"]
          self.j = 0
          self.k = 0
          f = 0
          self.count = 1
          for i in range(0, 5):
              self.A[i].itemPressed.connect(self.res1)
          anicount = 0
        if modecount == 2:
            list = random.sample(Alist, 7)
            self.Rlist = list
            item1 = QListWidgetItem(list[0])
            self.A1.addItem(item1)
            item2 = QListWidgetItem(list[1])
            self.A2.addItem(item2)
            item3 = QListWidgetItem(list[2])
            self.A3.addItem(item3)
            item4 = QListWidgetItem(list[3])
            self.A4.addItem(item4)
            item5 = QListWidgetItem(list[4])
            self.A5.addItem(item5)
            item6 = QListWidgetItem(list[5])
            self.A6.addItem(item6)
            item7 = QListWidgetItem(list[6])
            self.A7.addItem(item7)

            for i in range(0, len(self.Rlist) - 1):
                for j in range(len(self.Rlist) - 1):
                    if (self.Rlist[j] > self.Rlist[j + 1]):
                        temp = self.Rlist[j]
                        self.Rlist[j] = self.Rlist[j + 1]
                        self.Rlist[j + 1] = temp
            self.A = [self.A1, self.A2, self.A3, self.A4, self.A5,self.A6,self.A7]
            self.R = [self.R1, self.R2, self.R3, self.R4, self.R5,self.R6,self.R7]
            self.Output = []
            self.dec = ["சிறந்த பதில்!!!", "தொடர்ந்து முயற்சி செய்யுங்கள்!!!"]
            self.j = 0
            self.k = 0
            f = 0
            self.count = 1
            print(self.Rlist)
            for i in range(0, 7):
                self.A[i].itemPressed.connect(self.res2)
            anicount = 0
        if modecount == 3:
            if(daycount!=1):
                        list = random.sample(Alist, 10)
                        self.Rlist = list
                        item1 = QListWidgetItem(list[0])
                        self.A1.addItem(item1)
                        item2 = QListWidgetItem(list[1])
                        self.A2.addItem(item2)
                        item3 = QListWidgetItem(list[2])
                        self.A3.addItem(item3)
                        item4 = QListWidgetItem(list[3])
                        self.A4.addItem(item4)
                        item5 = QListWidgetItem(list[4])
                        self.A5.addItem(item5)
                        item6 = QListWidgetItem(list[5])
                        self.A6.addItem(item6)
                        item7 = QListWidgetItem(list[6])
                        self.A7.addItem(item7)
                        item8 = QListWidgetItem(list[7])
                        self.A8.addItem(item8)
                        item9 = QListWidgetItem(list[8])
                        self.A9.addItem(item9)
                        item10 = QListWidgetItem(list[9])
                        self.A10.addItem(item10)

                        for i in range(0, len(self.Rlist) - 1):
                            for j in range(len(self.Rlist) - 1):
                                if (self.Rlist[j] > self.Rlist[j + 1]):
                                    temp = self.Rlist[j]
                                    self.Rlist[j] = self.Rlist[j + 1]
                                    self.Rlist[j + 1] = temp
                        self.A = [self.A1, self.A2, self.A3, self.A4, self.A5, self.A6, self.A7,self.A8,self.A9,self.A10]
                        self.R = [self.R1, self.R2, self.R3, self.R4, self.R5, self.R6, self.R7,self.R8,self.R9,self.R10]
                        self.Output = []
                        self.dec = ["சிறந்த பதில்!!!", "தொடர்ந்து முயற்சி செய்யுங்கள்!!!"]
                        self.j = 0
                        self.k = 0
                        f = 0
                        self.count = 1
                        print(self.Rlist)
                        for i in range(0, 10):
                            self.A[i].itemPressed.connect(self.res3)
                        anicount = 0
            else:
                list = random.sample(Alist, 7)
                self.Rlist = list
                item1 = QListWidgetItem(list[0])
                self.A1.addItem(item1)
                item2 = QListWidgetItem(list[1])
                self.A2.addItem(item2)
                item3 = QListWidgetItem(list[2])
                self.A3.addItem(item3)
                item4 = QListWidgetItem(list[3])
                self.A4.addItem(item4)
                item5 = QListWidgetItem(list[4])
                self.A5.addItem(item5)
                item6 = QListWidgetItem(list[5])
                self.A6.addItem(item6)
                item7 = QListWidgetItem(list[6])
                self.A7.addItem(item7)

                for i in range(0, len(self.Rlist) - 1):
                    for j in range(len(self.Rlist) - 1):
                        if (self.Rlist[j] > self.Rlist[j + 1]):
                            temp = self.Rlist[j]
                            self.Rlist[j] = self.Rlist[j + 1]
                            self.Rlist[j + 1] = temp
                self.A = [self.A1, self.A2, self.A3, self.A4, self.A5, self.A6, self.A7]
                self.R = [self.R1, self.R2, self.R3, self.R4, self.R5, self.R6, self.R7]
                self.Output = []
                self.dec = ["சிறந்த பதில்!!!", "தொடர்ந்து முயற்சி செய்யுங்கள்!!!"]
                self.j = 0
                self.k = 0
                f = 0
                self.count = 1
                print(self.Rlist)
                for i in range(0, 7):
                    self.A[i].itemPressed.connect(self.res2)
                anicount = 0


    def res1(self,im):
        global op
        if self.j<5:
            op = str(self.count)
            self.Attempts.clear()
            op=str(self.count)
            self.Decision.clear()
            self.R[self.j].addItem(im.text())
            if im.text()==self.Rlist[self.j]:
                 self.Decision.addItem(self.dec[0])
                 self.j += 1
            else:
                self.Decision.addItem(self.dec[1])
                self.R1.clear()
                self.R2.clear()
                self.R3.clear()
                self.R4.clear()
                self.R5.clear()
                self.j=0
                self.count+=1
            self.Attempts.addItem(op)
        if self.j>=5:
            output=Output()
            widget.addWidget(output)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            #menu = Menu()
            #widget.addWidget(menu)
            #widget.setCurrentIndex(widget.currentIndex() + 1)

    def res2(self, im):
                    global op
                    if self.j < 7:
                        op = str(self.count)
                        self.Attempts.clear()
                        op = str(self.count)
                        self.Decision.clear()
                        self.R[self.j].addItem(im.text())
                        if im.text() == self.Rlist[self.j]:
                            self.Decision.addItem(self.dec[0])
                            self.j += 1
                        else:
                            self.Decision.addItem(self.dec[1])
                            self.R1.clear()
                            self.R2.clear()
                            self.R3.clear()
                            self.R4.clear()
                            self.R5.clear()
                            self.R6.clear()
                            self.R7.clear()
                            self.j = 0
                            self.count += 1
                        self.Attempts.addItem(op)
                    if self.j >= 7:

                        output = Output()
                        widget.addWidget(output)
                        widget.setCurrentIndex(widget.currentIndex() + 1)
    def res3(self, im):

                    global op
                    if self.j < 10:
                        op = str(self.count)
                        self.Attempts.clear()
                        op = str(self.count)
                        self.Decision.clear()
                        self.R[self.j].addItem(im.text())
                        if im.text() == self.Rlist[self.j]:
                            self.Decision.addItem(self.dec[0])
                            self.j += 1
                        else:
                            self.Decision.addItem(self.dec[1])
                            self.R1.clear()
                            self.R2.clear()
                            self.R3.clear()
                            self.R4.clear()
                            self.R5.clear()
                            self.R6.clear()
                            self.R7.clear()
                            self.R8.clear()
                            self.R9.clear()
                            self.R10.clear()
                            self.j = 0
                            self.count += 1
                        self.Attempts.addItem(op)
                    if self.j >= 10:

                        output = Output()
                        widget.addWidget(output)
                        widget.setCurrentIndex(widget.currentIndex() + 1)
                #main
app=QApplication(sys.argv)
menu=Menu()
widget = QStackedWidget()
widget.addWidget(menu)
qlisttt=widget.currentWidget()
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("EXITING")
