import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap


class ImageApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # QLabel을 생성하여 이미지를 출력
        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap("emoji/cry.png"))  # 이미지 경로를 설정
        self.image_label.setScaledContents(True)  # 이미지가 QLabel 안에 맞도록 크기 조정

        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)

        self.setLayout(layout)
        self.setWindowTitle("PyQt 이미지 출력")
        self.setGeometry(100, 100, 800, 600)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = ImageApp()
    main_window.show()
    sys.exit(app.exec_())