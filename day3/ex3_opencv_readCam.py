import cv2

# 카메라 열기 (기본 카메라: ID 0)
cap = cv2.VideoCapture(0)

# 카메라 작동 확인
if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

# 영상 스트림 출력
while True:
    ret, frame = cap.read()  # 비디오 프레임 읽기
    if not ret:
        print("프레임을 읽을 수 없습니다. 카메라를 확인하세요.")
        break

    cv2.imshow('Camera', frame)  # 비디오 출력

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()  # 카메라 닫기
cv2.destroyAllWindows()  # 창 닫기