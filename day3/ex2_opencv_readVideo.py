import cv2

# 동영상 파일 열기
video_path = "test_video.mp4"
cap = cv2.VideoCapture(video_path)

# 동영상 파일 열기 확인
if not cap.isOpened():
    print(f"동영상 파일을 열 수 없습니다: {video_path}")
    exit()

# 동영상 프레임 읽고 출력
while True:
    ret, frame = cap.read()  # 동영상 프레임 읽기
    if not ret:
        print("동영상 재생이 끝났습니다.")
        break

    cv2.imshow('Video Playback', frame)  # 프레임 출력

    # 'q' 키를 누르면 종료
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()  # 비디오 캡처 객체 닫기
cv2.destroyAllWindows()  # 모든 창 닫기