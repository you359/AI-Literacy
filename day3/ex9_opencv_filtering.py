import cv2
import numpy as np

# 이미지 읽기
image = cv2.imread("Lenna.png")

if image is None:
    print("이미지를 읽을 수 없습니다. 파일이 존재하는지 확인하세요.")
    exit()

# 1. 평균 값 필터(3x3)
average_filter = np.ones((3, 3), np.float32) / 9.0

# 2. 샤프닝 필터(3x3)
sharpening_filter = np.array([[0, -1, 0],
                              [-1, 5, -1],
                              [0, -1, 0]], np.float32)

# 3. 라플라시안 필터(3x3)
laplacian_filter = np.array([[0, 1, 0],
                             [1, -4, 1],
                             [0, 1, 0]], np.float32)


# 2D 필터 적용 함수
def apply_filter(image, kernel, filter_name):
    filtered_image = cv2.filter2D(image, -1, kernel)
    cv2.imshow(f"{filter_name}", filtered_image)
    return filtered_image


# 평균 값 필터 적용
apply_filter(image, average_filter, "Average Filter")

# 샤프닝 필터 적용
apply_filter(image, sharpening_filter, "Sharpening Filter")

# 라플라시안 필터 적용
apply_filter(image, laplacian_filter, "Laplacian Filter")

# 원본 이미지 보기
cv2.imshow("Original Image", image)

# 키 입력 대기 후 종료
cv2.waitKey(0)
cv2.destroyAllWindows()