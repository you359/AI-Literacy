import cv2
import numpy as np
import matplotlib.pyplot as plt

# Lenna 이미지를 Grayscale로 읽기
image = cv2.imread('Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

# 이미지 읽기가 성공적이지 못한 경우 처리
if image is None:
    print("이미지를 열 수 없습니다. 파일 경로를 확인하세요.")
else:
    # 이미지 정규화
    normalized_image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)

    cv2.imshow('Original Image', image)
    cv2.imshow('Normalized Image', normalized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 히스토그램 계산
    original_hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    normalized_hist = cv2.calcHist([normalized_image], [0], None, [256], [0, 256])

    # 히스토그램 시각화
    plt.figure(figsize=(10, 5))

    # 원본 이미지 히스토그램 출력
    plt.subplot(1, 2, 1)  # 1행 2열에서 첫 번째
    plt.title("Original Image Histogram")
    plt.plot(original_hist, color='blue')
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.grid()

    # 정규화된 이미지 히스토그램 출력
    plt.subplot(1, 2, 2)  # 1행 2열에서 두 번째
    plt.title("Normalized Image Histogram")
    plt.plot(normalized_hist, color='green')
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.grid()

    # 그래프 나타내기
    plt.tight_layout()
    plt.show()