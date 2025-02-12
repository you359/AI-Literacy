import cv2
import matplotlib.pyplot as plt

# Lenna 이미지를 RGB로 읽기
image = cv2.imread('Lenna.png')

# 이미지 읽기가 성공적이지 못한 경우 처리
if image is None:
    print("이미지를 열 수 없습니다. 파일 경로를 확인하세요.")
else:
    # 이미지 색상 체계 변환 (OpenCV는 기본적으로 BGR로 읽으므로 RGB로 변환)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 히스토그램 계산 및 시각화
    colors = ['Red', 'Green', 'Blue']
    plt.figure()
    plt.title("RGB Histogram")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")

    for i, color in enumerate(colors):
        hist = cv2.calcHist([image_rgb], [i], None, [256], [0, 256])
        plt.plot(hist, label=color, color=color.lower())  # 색상 이름에 맞는 라벨 추가
        plt.xlim([0, 256])

    plt.legend()
    plt.show()

    # RGB 이미지 출력
    cv2.imshow('RGB Image', image_rgb)

    # 키 입력 대기 후 창 닫기
    cv2.waitKey(0)
    cv2.destroyAllWindows()