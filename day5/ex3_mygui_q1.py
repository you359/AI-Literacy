import sys
import cv2
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap


class CameraApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.capture = cv2.VideoCapture(0)  # Open the default camera (0번째 카메라)

        # QTimer 설정 (주기적으로 프레임 업데이트)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # 30ms마다 update_frame 호출

    def init_ui(self):
        # QLabel을 이용한 영상 표출
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText("카메라를 준비 중...")

        # 종료 버튼 추가
        self.quit_button = QPushButton("종료", self)
        self.quit_button.clicked.connect(self.close_app)

        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.quit_button)

        self.setLayout(layout)
        self.setWindowTitle("PyQt + OpenCV 카메라 앱")
        self.setGeometry(200, 200, 800, 600)

    def update_frame(self):
        ret, frame = self.capture.read()  # 프레임 캡처
        if ret:
            # OpenCV는 기본적으로 BGR로 이미지를 생성 -> 이를 RGB로 변환
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # numpy 배열을 QImage로 변환
            height, width, channel = rgb_frame.shape
            bytes_per_line = channel * width
            qimage = QImage(rgb_frame.data, width, height, bytes_per_line, QImage.Format_RGB888)

            # QImage를 QLabel에 QPixmap으로 설정
            self.label.setPixmap(QPixmap.fromImage(qimage))

    def close_app(self):
        self.capture.release()  # 카메라 리소스 해제
        self.close()  # 창 닫기


if __name__ == "__main__":
    # QApplication 생성
    app = QApplication(sys.argv)

    # CameraApp 인스턴스 생성 및 실행
    camera_app = CameraApp()
    camera_app.show()

    # QApplication 실행
    sys.exit(app.exec_())