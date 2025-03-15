#THIS RIGHT HERE IS MEANT TO CAPTURE FRAMES FROM A MOVIE
#FOR USE AS TRAINING DATA.

import cv2 as cv

video = cv.VideoCapture("C:/Users/anang/OneDrive/Desktop/The Equalizer 3 (2023) [1080p] [WEBRip] [5.1] [YTS.MX]/The.Equalizer.3.2023.1080p.WEBRip.x264.AAC5.1-[YTS.MX].mp4")
num = 0

while True:
    ret, frame = video.read()
    num += 1

    frame = cv.resize(frame, (1366, 680))

    cv.imshow('frame', frame)

    if num % 2 == 0:
        cv.imwrite(f'frames/frame{num}.jpg', frame)
    else:
        cv.imwrite(f'labels/frame{num}.jpg', frame)

    if num == 3347:
        break

    # print('something')

    if cv.waitKey(20) & 0xFF==ord('d'):
        break


video.release()
cv.destroyAllWindows()