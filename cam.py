# try : 실행할 코드, except : 예외가 발생하면 실행되는 코드
import cv2
import datetime

try:
    video_dev = cv2.VideoCapture(0)

    while True:

        ret, frame = video_dev.read()
        cv2.imshow('Video Screen', frame)

        key = cv2.waitKey(1);
        if key == ord('q'):
            break

        elif key == ord('s'):
            file = datetime.datetime.now().strftime("%Y%m%d_%H%M%S%f") + '.jpg'
            cv2.imwrite(file, frame)
            print(file, ' saved')

except KeyboardInterrupt:
    print('User interruption')

video_dev.release()
cv2.destroyAllWindows()