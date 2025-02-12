import cv2
import numpy as np
import matplotlib.pyplot as plt

# Lenna 이미지를 Grayscale로 읽기
image = cv2.imread('Lenna.png', cv2.IMREAD_GRAYSCALE)

# 이미지 읽기가 성공적이지 못한 경우 처리
if image is None:
    print("이미지를 열 수 없습니다. 파일 경로를 확인하세요.")
else:
    # 명암비 조정
    alpha = 1.0  # 명암비 조정 계수
    func = (1 + alpha) * image - (alpha * 128)
    dst = np.clip(func, 0, 255).astype(np.uint8)

    # 히스토그램 계산
    original_hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    adjusted_hist = cv2.calcHist([dst], [0], None, [256], [0, 256])

    # 이미지를 출력
    cv2.imshow('Original Grayscale Image', image)
    cv2.imshow('Contrast Adjusted Image', dst)

    # 이미지 창 닫기
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 히스토그램 출력
    plt.figure(figsize=(12, 6))

    # 원본 이미지 히스토그램
    plt.subplot(1, 2, 1)
    plt.plot(original_hist, color='blue')
    plt.title('Histogram of Original Image')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.grid()

    # 명암비 조정 이미지 히스토그램
    plt.subplot(1, 2, 2)
    plt.plot(adjusted_hist, color='red')
    plt.title('Histogram of Contrast Adjusted Image')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.grid()

    plt.tight_layout()
    plt.show()
