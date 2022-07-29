from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton ,QPlainTextEdit ,QLabel
from PySide2.QtCore import *
import numpy as np
from PySide2.QtGui import QPixmap ,QImage
import cv2

def handleCalc():
    print("统计按钮被点击了")

app = QApplication([])
window = QMainWindow()
window.resize(500,400)
window.move(300,310)
window.setWindowTitle("薪资统计")

textEdit = QPlainTextEdit()
textEdit.setPlaceholderText("请输入薪资表")
textEdit.move(10,25)
textEdit.resize(300,350)

button = QPushButton("统计",window)
button.move(380,80)
button.clicked.connect(handleCalc)

cSamW = 200
cSamH = 200
def ShowSample(npImg, label):
    showImg = QImage(npImg.data, cSamW, cSamH, cSamW * 8, QImage.Format_RGB888)
    label.setPixmap(QPixmap.fromImage(showImg))



label = QLabel(window)
label.resize(200,200)
img = np.zeros((cSamW,cSamH,3),dtype=np.uint8)
for i in range(cSamW):
    for j in range(cSamH):
        img[i][j] = (127,127,127)
print(img.shape)
print(img)

cv2.imshow("window",img)
cv2.waitKey(0)

cv2.imwrite("npimg.jpg",img)
img = cv2.imread("psimg.png",flags=cv2.IMREAD_COLOR)
ShowSample(img,label)
cv2.imshow("window",img)
cv2.waitKey(0)

cv2.destroyAllWindows()


window.show()

app.exec_()