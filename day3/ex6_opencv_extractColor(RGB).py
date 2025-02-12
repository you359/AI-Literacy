import cv2
import numpy as np

# 이미지 읽기
image = cv2.imread('Candies.png')

# 이미지 읽기가 성공적이지 못한 경우 처리
if image is None:
    print("이미지를 열 수 없습니다. 파일 경로를 확인하세요.")
else:
    # BGR 채널 분리
    blue, green, red = cv2.split(image)

    # Red 성분이 50 이상인 영역(마스크) 생성
    red_mask = cv2.inRange(red, 150, 255)

    # 마스크를 적용하여 원래 이미지의 해당 영역 추출
    filtered_image = cv2.bitwise_and(image, image, mask=red_mask)

    # 결과 이미지와 마스크 출력
    cv2.imshow('Original Image', image)
    cv2.imshow('Red >= 150 Mask', red_mask)
    cv2.imshow('Filtered Image', filtered_image)

    # 키 입력 대기 후 창 닫기
    cv2.waitKey(0)
    cv2.destroyAllWindows()