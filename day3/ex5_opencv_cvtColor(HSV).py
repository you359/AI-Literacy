import cv2

# 이미지를 읽기
image = cv2.imread('Lenna.png')

# 이미지 읽기가 성공적이지 못한 경우 처리
if image is None:
    print("이미지를 열 수 없습니다. 파일 경로를 확인하세요.")
else:
    # BGR에서 HSV 색 공간으로 변환
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # HSV 성분 분리
    h, s, v = cv2.split(hsv_image)

    # 각각의 성분 출력
    print("Hue Component:")
    print(h)
    print("\nSaturation Component:")
    print(s)
    print("\nValue Component:")
    print(v)

    # 이미지 윈도우로 확인 (필요한 경우 사용)
    cv2.imshow('Original Image', image)
    cv2.imshow('Hue Component', h)
    cv2.imshow('Saturation Component', s)
    cv2.imshow('Value Component', v)

    # 키 입력 대기 후 닫기
    cv2.waitKey(0)
    cv2.destroyAllWindows()