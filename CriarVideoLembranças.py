import os
import cv2


path = "Imagens"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width, height)
print(size)
videomaneiro = cv2.VideoWriter('lembrancas.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 2, size)
for i in range(count-1, 0, -1):
    frame = cv2.imread(images[i])
    videomaneiro.write(frame)
videomaneiro.release()
print('video encerrado')