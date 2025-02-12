from os import environ
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import uic
import cv2

import random

from deepface import DeepFace

environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '1'  # 모니터 해상도에 따른 폰트 및 컨트롤 크기 자동 조정

# UI파일 연결 (ex4_main.ui 파일과 같은 디렉토리에 위치해야 함)
form_class = uic.loadUiType("ex4_main.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # initialize UI
        self.GuideTextLabel.clear()
        self.referenceLabel.clear()
        self.labelPercentage.clear()
        self.labelCredits.setText("00:00.00")
        self.GuideTextLabel.setVisible(False) # QLabel (GuideText) 초기화, 시작 시 안보이게

        # game setting
        self.gametime = 0           # game 타이머 시간
        self.questions = []         # 랜덤 문제 리스트
        self.ongoing = False        # 게임 중 여부 확인 Flag
        self.current_question = 0   # 현재 문제 번호
        self.isOK = False           # 성공 여부
        self.max_question = 5       # 총 문제 개수

        # 감정 이미지 path 및 문제 식볇 번호 정의
        self.emoji = [
            "astonished.png",
            "cry.png",
            "grinning.png",
            "neutral_face.png",
            "rage.png"
        ]
        self.emotion = {
            "surprise": 0,
            "sad": 1,
            "happy": 2,
            "neutral": 3,
            "angry": 4
        }

        # OpenCV VideoCapture 객체 초기화
        self.cap = cv2.VideoCapture(0)  # 기본 카메라 (0번)
        if not self.cap.isOpened():
            QMessageBox.critical(self, "Camera Error", "Cannot access the camera.")
            sys.exit()

        # QPushButton 클릭 동작 연동
        self.startButton.clicked.connect(self.start_action)

        # QLabel에 카메라 프레임 표시하기 위한 설정
        self.cameratimer = QTimer(self)
        self.cameratimer.timeout.connect(self.update_frame)
        self.cameratimer.start(30)  # 30ms 간격으로 프레임 업데이트

        # game 타이머 설정
        self.gametimer = QTimer(self)
        self.gametimer.setInterval(10)  # 타이머 업데이트 간격: 10ms (0.01초)
        self.gametimer.timeout.connect(self.update_timer)  # QTimer가 호출할 슬롯 연결

        # guide 타이머 설정
        self.guidetimer = QTimer(self)
        self.guidetimer.timeout.connect(self.update_guide)
        self.guidetimer.start(1000)  # 500ms 간격으로 프레임 업데이트

        # 가이드 상태 변환을 위한 코드
        self.cnt = 1

    def start_action(self):
        self.gametime = 0
        self.questions = [random.randrange(0, len(self.emoji)) for i in range(self.max_question)]
        self.gametimer.start()
        self.update_reference()
        self.ongoing = True
        self.isOK = False

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            # OpenCV는 기본적으로 BGR로 표현되므로 RGB로 변환
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # QLabel 크기를 가져오기
            label_width = self.cameraLabel.width()
            label_height = self.cameraLabel.height()

            # OpenCV로 크기 조정 (QLabel 크기에 맞춤)
            frame = cv2.resize(frame, (label_width, label_height), interpolation=cv2.INTER_AREA)

            # OpenCV 프레임을 QImage로 변환
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            q_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)

            # QLabel에 표시
            self.cameraLabel.setPixmap(QPixmap.fromImage(q_img))
        else:
            self.cameraLabel.setText("Failed to read frame from camera.")

    def closeEvent(self, event):
        # 창 종료시 카메라 릴리즈
        if self.cap.isOpened():
            self.cap.release()
        event.accept()

    def update_timer(self):
        self.gametime += 10  # 10ms씩 증가
        minutes = self.gametime // 60000  # 총 밀리초에서 분 계산
        seconds = (self.gametime % 60000) // 1000  # 남은 밀리초에서 초 계산
        milliseconds = self.gametime % 1000 // 10  # 남은 밀리초

        # mm:ss.SS 형태로 포맷팅
        time_text = f"{minutes:02}:{seconds:02}.{milliseconds:02}"
        self.labelCredits.setText(time_text)  # QLabel 업데이트

    def update_guide(self):
        if self.ongoing:
            self.GuideTextLabel.setVisible(True)
            if self.cnt < 4:
                self.GuideTextLabel.setStyleSheet("color: black; background-color: rgba(100, 100, 100, 100);")
                self.GuideTextLabel.clear()
                self.GuideTextLabel.setText(str(4-self.cnt))
                self.cnt += 1

            elif self.cnt < 5:
                self.GuideTextLabel.setText("")
                self.GuideTextLabel.setVisible(False)
                self.cnt += 1

            elif self.cnt < 6:
                # TODO: face recognition
                ret, frame = self.cap.read()
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                objs = DeepFace.analyze(
                    img_path=image,
                    actions=['emotion'],
                )
                print(objs)
                ret = objs[0]['dominant_emotion']
                print(ret)
                print(self.emotion[ret])
                print(self.current_question)

                if self.emotion[ret] == self.current_question:
                    self.isOK = True
                else:
                    self.isOK = False

                self.cnt += 1

            elif self.cnt < 7:
                self.GuideTextLabel.clear()
                self.GuideTextLabel.setVisible(True)
                if self.isOK:
                    self.GuideTextLabel.setStyleSheet("color: green; background-color: rgba(100, 100, 100, 100);")
                    self.GuideTextLabel.setText("O")
                    self.update_reference()
                else:
                    self.GuideTextLabel.setStyleSheet("color: red; background-color: rgba(100, 100, 100, 100);")
                    self.GuideTextLabel.setText("X")
                self.cnt += 1
            else:
                self.cnt = 1

    def update_reference(self):
        self.setValue(self.max_question - len(self.questions),
                      self.max_question,
                      self.labelPercentage,
                      self.circularProgress)

        if len(self.questions) > 0:
            self.current_question = self.questions.pop()
            image_path = "emoji/" + self.emoji[self.current_question]
            pixmap = QPixmap(image_path)
            scaled_pixmap = pixmap.scaled(self.referenceLabel.size(), aspectRatioMode=True)  # QLabel 크기에 맞게 설정
            self.referenceLabel.setPixmap(scaled_pixmap)
            self.isOK = False
        else:
            self.gametimer.stop()
            minutes = self.gametime // 60000  # 총 밀리초에서 분 계산
            seconds = (self.gametime % 60000) // 1000  # 남은 밀리초에서 초 계산
            milliseconds = self.gametime % 1000 // 10  # 남은 밀리초
            # mm:ss.SSS 형태로 포맷팅
            time_text = f"{minutes:02}:{seconds:02}.{milliseconds:02}"
            QMessageBox.information(self,
                                    "Game Finished",
                                    "게임 종료! \n 걸린시간: " + time_text)

    ## ==> SET VALUES TO DEF progressBarValue
    def setValue(self, value, max_value, labelPercentage, progressBarName):
        # CONVERT VALUE TO INT
        sliderValue = int((value / max_value) * 100)

        # HTML TEXT PERCENTAGE
        htmlText = """<p align="center"><span style=" font-size:50pt;">{VALUE}</span><span style=" font-size:40pt; vertical-align:super;">%</span></p>"""
        labelPercentage.setText(htmlText.replace("{VALUE}", str(sliderValue)))

        # CALL DEF progressBarValue
        self.progressBarValue((value / max_value) * 100, progressBarName)

    ## DEF PROGRESS BAR VALUE
    ########################################################################
    def progressBarValue(self, value, widget):
        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
                QFrame{
                	border-radius: 110px;
                	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 255, 255, 0), stop:{STOP_2} rgba(85, 170, 255, 255));
                }
                """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # FIX MAX VALUE
        if value == 100:
            stop_1 = "1.000"
            stop_2 = "1.000"

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        # APPLY STYLESHEET WITH NEW VALUES
        widget.setStyleSheet(newStylesheet)

if __name__ == "__main__":
    # QApplication: 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    # 프로그램 화면 표시
    myWindow.show()

    # 프로그램 이벤트 루프 진입
    sys.exit(app.exec_())