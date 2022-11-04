# --- DataStructure | TowerOfHanoi GUI with pyqt5
# --- University of guilan

from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
import sys,os
from PyQt5.QtWidgets import QDialog , QApplication ,QLabel
from random import choice

num_of_disk = 4

class mainWindowUI(QDialog):
    disks_lbl = {}
    images = {}
    check_col = {
        'A' : 0,
        'B' : 0,
        'C' : 0
    }
    res_forward = []
    res_backward = []
    movement = 0
    def __init__(self):
        super().__init__()
        loadUi("main.ui", self)
        self.setWindowTitle("Tower of Hanoi GUI")
        self.setFixedSize(self.width(),self.height())
        self.create_disks(self)
        self.pushButton.clicked.connect(lambda x : self.goToNextRound(self.movement))
        self.pushButton_2.clicked.connect(lambda x : self.goToPerviousRound(self.movement))
        self.colorBtn.clicked.connect(self.goToChangeColor)
        self.pushButton_2.setHidden(True)
        self.check_col["A"] = num_of_disk
        self.TowerOfHanoi(num_of_disk,'A','C','B')
        self.show()
        
    def create_disks(self,instance):
        color_range = range(256)
        biggest = num_of_disk
        count = 0
        biggest_y = 480
        lowest_x = 100
        width = 240
        for i in range(num_of_disk):
            self.disks_lbl[biggest] = QLabel(instance)
            self.disks_lbl[biggest].setStyleSheet("background-color:rgb({},{},{};)".format(choice(color_range),choice(color_range),choice(color_range)))
            self.disks_lbl[biggest].setText(f"{biggest}")
            if(biggest < 6):
                count += 1
                width -= 30
                self.disks_lbl[biggest].setGeometry((lowest_x+(count*15)),biggest_y,width,20)
            else:
                self.disks_lbl[biggest].setGeometry((lowest_x),biggest_y,width,20)
            biggest -= 1
            biggest_y -= 20
            
    def goToChangeColor(self):
        color_range = range(256)
        for i in range(1,num_of_disk+1):
            self.disks_lbl[i].setStyleSheet("background-color:rgb({},{},{};)".format(choice(color_range),choice(color_range),choice(color_range))) 
    
    def goToPerviousRound(self,movement):
        li = self.res_backward[movement-1]
        # self.close()
        img_id = li[0]
        start = li[1]
        destention = li[2]
        check_col = self.check_col[destention]
        print(f"backward : move {img_id} from {start} to {destention} | round : {self.movement-1}")
        self.Details.setText(f"backward : move {img_id} from {start} to {destention} | round : {self.movement-1}")
        if(start == "A" and destention == "B"):
            x = self.disks_lbl[img_id].x() + 300
        elif(start == "A" and destention == "C"):
            x = self.disks_lbl[img_id].x() + 600
        elif(start == "B" and destention == "C"):
            x = self.disks_lbl[img_id].x() + 300
        elif(start == "B" and destention == "A"):
            x = self.disks_lbl[img_id].x() - 300
        elif(start == "C" and destention == "A"):
            x = self.disks_lbl[img_id].x() - 600
        elif(start == "C" and destention == "B"):
            x = self.disks_lbl[img_id].x() - 300
        if(check_col == 0):
            self.disks_lbl[img_id].setGeometry(x,480,self.disks_lbl[img_id].width(),20)
            self.check_col[destention] += 1
            self.check_col[start] -= 1
        else:
            self.disks_lbl[img_id].setGeometry(x,480-(check_col*20),self.disks_lbl[img_id].width(),20)
            self.check_col[destention] += 1
            self.check_col[start] -= 1
        # self.show()
        self.movement -= 1
        if(self.movement == 0):
            self.pushButton_2.setHidden(True)
            self.pushButton.setHidden(False)

    def goToNextRound(self,movement):
        li = self.res_forward[movement]
        # self.close()
        img_id = li[0]
        start = li[1]
        destention = li[2]
        check_col = self.check_col[destention]
        print(f"forward : move {img_id} from {start} to {destention} | round : {self.movement+1}")
        self.Details.setText(f"forward : move {img_id} from {start} to {destention} | round : {self.movement+1}")
        if(start == "A" and destention == "B"):
            x = self.disks_lbl[img_id].x() + 300
        elif(start == "A" and destention == "C"):
            x = self.disks_lbl[img_id].x() + 600
        elif(start == "B" and destention == "C"):
            x = self.disks_lbl[img_id].x() + 300
        elif(start == "B" and destention == "A"):
            x = self.disks_lbl[img_id].x() - 300
        elif(start == "C" and destention == "A"):
            x = self.disks_lbl[img_id].x() - 600
        elif(start == "C" and destention == "B"):
            x = self.disks_lbl[img_id].x() - 300
        if(check_col == 0):
            self.disks_lbl[img_id].setGeometry(x,480,self.disks_lbl[img_id].width(),20)
            self.check_col[destention] += 1
            self.check_col[start] -= 1
        else:
            self.disks_lbl[img_id].setGeometry(x,480-(check_col*20),self.disks_lbl[img_id].width(),20)
            self.check_col[destention] += 1
            self.check_col[start] -= 1
        # self.show()
        self.movement += 1
        self.pushButton_2.setHidden(False)
        if(self.movement == (2**num_of_disk)-1):
            self.pushButton.setHidden(True)


    def TowerOfHanoi(self,n=num_of_disk , source="A", destination="C", auxiliary="B"):
        if n==1:
            x = [1,source,destination]
            y = [1,destination,source]
            self.res_forward.append(x)
            self.res_backward.append(y)
            # print ("Move disk 1 from source",source,"to destination",destination)
            return  
        x = [n,source,destination]
        y = [n,destination,source]
        self.TowerOfHanoi(n-1, source, auxiliary, destination)
        # print ("Move disk",n,"from source",source,"to destination",destination)
        self.res_forward.append(x)
        self.res_backward.append(y)
        self.TowerOfHanoi(n-1, auxiliary, destination, source)
        
        
app = QApplication(sys.argv)
mainUI = mainWindowUI()
sys.exit(app.exec_())