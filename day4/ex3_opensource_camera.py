import cv2
from deepface import DeepFace

# 카메라 객체 생성 (기본 카메라는 index 0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
  print("카메라를 열 수 없습니다.")
  exit()

while True:
  # 카메라 프레임 읽기
  ret, frame = cap.read()

  if not ret:
    print("프레임을 가져올 수 없습니다. 종료합니다.")
    break

  image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

  objs = DeepFace.analyze(
    img_path =image,
    actions = ['age', 'gender', 'race', 'emotion'],
  )
  objs = objs[0]
  print(objs)

  # 출력할 텍스트 추가
  text = ("age: {}, gender: {}, race: {}, emotion: {}".format(
    objs['age'], objs['dominant_gender'], objs['dominant_race'], objs['dominant_emotion']))
  font = cv2.FONT_HERSHEY_SIMPLEX  # 폰트 종류
  font_scale = 0.7  # 폰트 크기
  color = (0, 0, 255)  # 초록색 (B, G, R 순)
  thickness = 2  # 두께
  org = (10, frame.shape[0] - 10)  # 텍스트 위치 (좌측 하단)

  # 텍스트를 프레임에 추가
  cv2.putText(frame, text, org, font, font_scale, color, thickness, cv2.LINE_AA)

  # 디스플레이 윈도우에 프레임 표시
  cv2.imshow('Camera Frame', frame)

  # 'q' 키를 누르면 종료
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# 자원 해제
cap.release()
cv2.destroyAllWindows()