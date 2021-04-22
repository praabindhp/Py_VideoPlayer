import cv2

test_video = "videoplayback.mp4"
capture=cv2.VideoCapture(test_video)

if (capture.isOpened() == False):
    print("\nError Opening Video !\n")

while(capture.isOpened()):

    ret,frame = capture.read()
    if ret == True:
        cv2.imshow("Frame",frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break

capture.release()
cv2.destroyAllWindows()