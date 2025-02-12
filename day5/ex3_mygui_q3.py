import sys
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPainter, QPen, QFont
from PyQt5.QtWidgets import QApplication, QWidget


class CircularProgressBar(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Circular Progress Bar")
        self.resize(300, 300)
        self.progress = 0  # Progress 값 (0~100)

    def setProgress(self, value):
        """Progress 값을 설정합니다."""
        self.progress = value
        self.update()  # 다시 그리기

    def paintEvent(self, event):
        """현재 Progress Bar를 그리기 위한 페인팅 로직"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 원형 Progress Bar의 중심 및 반지름 계산
        rect = QRectF(50, 50, 200, 200)  # 중심 사각형
        start_angle = -90 * 16  # 초기 각도 (12시 방향)
        span_angle = int(-self.progress / 100 * 360 * 16)  # 진행 각도

        # 배경 원
        pen = QPen(Qt.gray, 20)  # 너비가 20인 회색 원
        painter.setPen(pen)
        painter.drawArc(rect, 0, 360 * 16)

        # 진행 원
        pen.setColor(Qt.blue)  # 진행 부분은 파란색
        painter.setPen(pen)
        painter.drawArc(rect, start_angle, span_angle)

        # 텍스트 추가 (Progress 값)
        painter.setPen(Qt.black)
        painter.setFont(QFont("Arial", 16, QFont.Bold))
        painter.drawText(rect, Qt.AlignCenter, f"{self.progress}%")

        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = CircularProgressBar()
    window.show()

    # 예제: 값을 업데이트
    import time


    def update_progress():
        for i in range(101):
            time.sleep(0.05)  # 업데이트 간격
            window.setProgress(i)
            app.processEvents()


    update_progress()
    sys.exit(app.exec_())