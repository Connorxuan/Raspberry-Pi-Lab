import cv2
cap=cv2.VideoCapture(0)
i=0
while(1):
    ret ,frame = cap.read()
    k=cv2.waitKey(1)
    if k==27:           #按下ESC退出窗口
        break
    elif k==ord('s'):   #按下s保存图片
        cv2.imwrite('./'+str(i)+'.jpg',frame)
        i+=1
    cv2.imshow("capture", frame)
cap.release()
