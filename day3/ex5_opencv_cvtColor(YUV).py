import cv2

# 이미지를 읽기
image = cv2.imread('Lenna.png')

# 이미지 읽기가 성공적이지 못한 경우 처리
if image is None:
    print("이미지를 열 수 없습니다. 파일 경로를 확인하세요.")
else:
    # BGR에서 YUV 색 공간으로 변환
    yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

    # YUV 성분 분리
    y, u, v = cv2.split(yuv_image)

    # 각각의 성분 출력
    print("Y(Luma) Component:")
    print(y)
    print("\nU Component:")
    print(u)
    print("\nV Component:")
    print(v)

    # 이미지 윈도우로 확인 (필요할 경우 사용)
    cv2.imshow('Original Image', image)
    cv2.imshow('Y Component', y)
    cv2.imshow('U Component', u)
    cv2.imshow('V Component', v)

    # 키 입력 대기 후 닫기
    cv2.waitKey(0)
    cv2.destroyAllWindows()