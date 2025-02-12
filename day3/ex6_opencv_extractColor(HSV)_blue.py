import cv2
import numpy as np

# 이미지 읽기
image = cv2.imread('candies.png')
if image is None:
    print("이미지를 읽지 못했습니다. 파일 경로를 확인하세요.")
    exit()

# BGR 이미지를 HSV로 변환
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 파란색의 HSV 범위 정의
lower_blue = np.array([100, 50, 50])  # 하한값
upper_blue = np.array([140, 255, 255])  # 상한값

# 파란색 범위에 해당하는 마스크 생성
blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

# 파란색 캔디만 추출
blue_candies = cv2.bitwise_and(image, image, mask=blue_mask)

# 결과 출력
cv2.imshow('Original Image', image)
cv2.imshow('Blue Mask', blue_mask)  # 흰색 영역이 파란색 캔디만 표시
cv2.imshow('Blue Candies', blue_candies)  # 파란색 캔디만 추출된 이미지

# 키 입력 대기 후 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()