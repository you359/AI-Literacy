import cv2

# 이미지를 읽기
image = cv2.imread('Lenna.png')  # 파일 경로에 맞게 수정 필요

# 이미지 읽기 확인
if image is None:
    print("이미지를 읽을 수 없습니다. 경로를 확인하세요.")
else:
    # 이미지를 출력
    cv2.imshow('Lenna', image)  # 'Lenna'는 윈도우 이름
    cv2.waitKey(0)  # 키 입력을 대기
    cv2.destroyAllWindows()  # 모든 창 닫기