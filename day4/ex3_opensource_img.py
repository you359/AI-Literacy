from deepface import DeepFace

objs = DeepFace.analyze(
  img_path ="face.jpg",
  actions = ['age', 'gender', 'race', 'emotion'],
)

print(objs)