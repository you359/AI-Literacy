from os import environ
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '1'  # 모니터 해상도에 따른 폰트 및 컨트롤 크기 자동 조정

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("ex2_pyqt_designer.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.pushButton_clicked)

    def pushButton_clicked(self):
        QMessageBox.information(self,
                                "푸시 버튼 클릭",
                                "푸시 버튼 클릭시 정보 출력.")

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()