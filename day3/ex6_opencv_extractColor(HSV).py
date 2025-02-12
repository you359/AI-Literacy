import cv2
import numpy as np

# 이미지 읽기
image = cv2.imread('candies.png')
if image is None:
    print("이미지를 읽지 못했습니다. 파일 경로를 확인하세요.")
    exit()

# BGR 이미지를 HSV로 변환
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 붉은색의 HSV 범위 정의 (붉은색은 두 개의 범위를 가진다)
lower_red1 = np.array([0, 120, 70])  # 첫 번째 하한값
upper_red1 = np.array([10, 255, 255])  # 첫 번째 상한값
lower_red2 = np.array([170, 120, 70])  # 두 번째 하한값
upper_red2 = np.array([180, 255, 255])  # 두 번째 상한값

# 각 범위에 해당하는 마스크 생성
mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)

# 두 마스크를 합성
red_mask = cv2.bitwise_or(mask1, mask2)

# 붉은색 캔디만 추출
red_candies = cv2.bitwise_and(image, image, mask=red_mask)

# 결과 출력
cv2.imshow('Original Image', image)
cv2.imshow('Red Mask', red_mask)
cv2.imshow('Red Candies', red_candies)

# 키 입력 대기 후 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()