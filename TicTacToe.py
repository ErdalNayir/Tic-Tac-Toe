
from PyQt5.QtCore import* # QApplication oluşturmak için
import sys # sayfanın oluşması ve kapatılması için
from PyQt5 import*
from PyQt5.QtWidgets import*  # tableWidgetin kullanılması için
from PyQt5.QtGui import*


class Game(QWidget):
    def __init__(self):
        super().__init__()

        self.width = 565
        self.height = 296
        self.qtRectangle = self.frameGeometry()
        self.centerPoint=QDesktopWidget().availableGeometry().center()
        self.msg= QMessageBox()

        self.initUI()

    def initUI(self):

        self.setWindowTitle("Tic Tac Toe")
        self.setFixedSize(self.width, self.height)

        self.qtRectangle.moveCenter(self.centerPoint)
        self.move(self.qtRectangle.topLeft())

        self.Buttons=[]

        for i in range(3):
            row=[]

            for j in range(3):

                row.append((QPushButton(self)))

            self.Buttons.append(row)

        y=-80
        
        for i in range(3):
            y+=90
            x=-80
            for j in range(3):
                
                x+=90

                self.Buttons[i][j].setGeometry(x,y,81,81)

                self.Buttons[i][j].setFont(QFont(QFont('Times', 17)))

                self.Buttons[i][j].clicked.connect(self.ButtonClicked)


        self.myFont=QFont('Times', 15)
        self.myFont.setBold(True)


        self.label_1= QLabel(self)
        self.label_1.setText("Tic-Tac-Toe")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setFont(self.myFont)
        self.label_1.setFixedSize(241,41)
        self.label_1.move(304,30)
        self.label_1.setStyleSheet("""
                                      background-color: rgba(0,0,0,0%);
                                   """)

        self.label_2= QLabel(self)
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setFont(self.myFont)
        self.label_2.setFixedSize(231,41)
        self.label_2.move(305,120)
        self.label_2.setStyleSheet("""
                                      background-color: white;
                                      border: 1px solid black;
                                   """)


        self.RestartButton = QPushButton("Restart Game",self)
        self.RestartButton.setFont(QFont("Times"))
        self.RestartButton.clicked.connect(self.RestartGame)
        self.RestartButton.setGeometry(350,220,151,41)

        self.WhichOne=0
        self.Turn=0

        self.show()

    def ButtonClicked(self):

        button=self.sender()

        button.setEnabled(False)

        if self.WhichOne==0:
            button.setText("X")
            self.WhichOne=1
            self.Turn+=1
        else:
            button.setText("O")
            self.WhichOne=0
            self.Turn+=1

        winnerIs = self.Winner()

        if winnerIs==True:

            if self.WhichOne ==0:

                self.label_2.setText("O Won!")
            else:
                self.label_2.setText("X Won!")

            for buttons in self.Buttons:
                for push in buttons:
                    push.setEnabled(False)

        elif winnerIs==False:
            self.label_2.setText("Draw")

    def RestartGame(self):

        self.Turn=0

        for i in range(3):
            for j in range(3):

                self.Buttons[i][j].setEnabled(True)
                self.Buttons[i][j].setText("")
                self.Buttons[i][j].setStyleSheet("background-color:none;")

        self.label_2.setText("")

    def Winner(self):

        if self.Turn<9:
            #for columns
            for i in range(3):
                if self.Buttons[0][i].text() == self.Buttons[1][i].text() \
                        and self.Buttons[0][i].text() == self.Buttons[2][i].text() \
                        and self.Buttons[0][i].text() != "":

                    self.Buttons[0][i].setStyleSheet("background-color:rgba(0, 255, 255, 50)")
                    self.Buttons[1][i].setStyleSheet("background-color:rgba(0, 255, 255, 50)")
                    self.Buttons[2][i].setStyleSheet("background-color:rgba(0, 255, 255, 50)")
                    return True
            #for rows
            for i in range(3):
                if self.Buttons[i][0].text() == self.Buttons[i][1].text() \
                        and self.Buttons[i][0].text() == self.Buttons[i][2].text() \
                        and self.Buttons[i][0].text() != "":

                    self.Buttons[i][0].setStyleSheet("background-color:rgba(0, 255, 255, 50)")
                    self.Buttons[i][1].setStyleSheet("background-color:rgba(0, 255, 255, 50)")
                    self.Buttons[i][2].setStyleSheet("background-color:rgba(0, 255, 255, 50)")
                    return True
            #for first diagonal
            if self.Buttons[0][0].text() == self.Buttons[1][1].text() \
                    and self.Buttons[0][0].text() == self.Buttons[2][2].text() \
                    and self.Buttons[0][0].text() != "":

                self.Buttons[0][0].setStyleSheet("background-color:rgba(0, 255, 255, 50)")
                self.Buttons[1][1].setStyleSheet("background-color:rgba(0, 255, 255, 50)")
                self.Buttons[2][2].setStyleSheet("background-color:rgba(0, 255, 255, 50)")

                return True
            #for other diagonal
            if self.Buttons[0][2].text() == self.Buttons[1][1].text() \
                    and self.Buttons[1][1].text() == self.Buttons[2][0].text() \
                    and self.Buttons[0][2].text() != "":

                self.Buttons[0][2].setStyleSheet("background-color:rgba(0, 255, 255, 50)")
                self.Buttons[1][1].setStyleSheet("background-color:rgba(0, 255, 255, 50)")
                self.Buttons[2][0].setStyleSheet("background-color:rgba(0, 255, 255, 50)")
                return True

        elif self.Turn==9:
            return False


def main():
    app = QApplication(sys.argv)
    ary = Game()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
