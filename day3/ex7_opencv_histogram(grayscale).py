import cv2
import matplotlib.pyplot as plt

# Lenna 이미지를 그레이스케일로 읽기
image = cv2.imread('Lenna.png', cv2.IMREAD_GRAYSCALE)

# 이미지 읽기가 성공적이지 못한 경우 처리
if image is None:
    print("이미지를 열 수 없습니다. 파일 경로를 확인하세요.")
else:
    # 히스토그램 계산
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])

    # 원본 이미지 출력
    cv2.imshow('Grayscale Image', image)

    # 히스토그램 출력
    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()

    # 키 입력 대기 후 창 닫기
    cv2.waitKey(0)
    cv2.destroyAllWindows()