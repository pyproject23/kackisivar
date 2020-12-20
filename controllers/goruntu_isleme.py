from PyQt5.QtCore import QThread, Qt, pyqtSignal
from PyQt5.QtGui import QImage
from controllers.person import Person
from models.ayarlar import Ayarlar
import numpy as np
import cv2


class GoruntuIsleme(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.cnt_up = 0
        self.cnt_down = 0
        self.count_up = 0
        self.count_down = 0
        self.sayim_tipi = ""
        self.ayarlar = Ayarlar.ayarlari_getir()
        self.cap = None

    changePixmap = pyqtSignal(QImage)

    def run(self):

        if self.sayim_tipi == "demo":
            video = self.ayarlar[7]
            self.cap = cv2.VideoCapture(video)
        elif self.sayim_tipi == "canli":
            cam_id = int(self.ayarlar[6])
            self.cap = cv2.VideoCapture(cam_id)

        for i in range(19):
            print(i, self.cap.get(i))

        w = self.cap.get(3)
        h = self.cap.get(4)
        frameArea = h * w
        areaTH = frameArea / 300
        print('Area Threshold', areaTH)

        line_up = int(1 * (h / 5))
        line_down = int(4 * (h / 5))

        up_limit = int(.5 * (h / 5))
        down_limit = int(4.5 * (h / 5))

        print("Red line y:", str(line_down))
        print("Blue line y:", str(line_up))
        line_down_color = (255, 0, 0)
        line_up_color = (0, 0, 255)
        pt1 = [0, line_down]
        pt2 = [w, line_down]
        pts_L1 = np.array([pt1, pt2], np.int32)
        pts_L1 = pts_L1.reshape((-1, 1, 2))
        pt3 = [0, line_up]
        pt4 = [w, line_up]
        pts_L2 = np.array([pt3, pt4], np.int32)
        pts_L2 = pts_L2.reshape((-1, 1, 2))

        pt5 = [0, up_limit]
        pt6 = [w, up_limit]
        pts_L3 = np.array([pt5, pt6], np.int32)
        pts_L3 = pts_L3.reshape((-1, 1, 2))
        pt7 = [0, down_limit]
        pt8 = [w, down_limit]
        pts_L4 = np.array([pt7, pt8], np.int32)
        pts_L4 = pts_L4.reshape((-1, 1, 2))

        fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)

        kernelOp = np.ones((3, 3), np.uint8)
        kernelCl = np.ones((11, 11), np.uint8)

        # font = cv2.FONT_HERSHEY_SIMPLEX
        persons = []
        # rect_co = []
        max_p_age = 1
        pid = 1
        # val = []

        while (self.cap.isOpened()):

            ret, frame = self.cap.read()

            fgmask = fgbg.apply(frame)
            fgmask2 = fgbg.apply(frame)

            try:
                ret, imBin = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)
                ret, imBin2 = cv2.threshold(fgmask2, 200, 255, cv2.THRESH_BINARY)
                # Opening (erode->dilate) to remove noise.
                mask = cv2.morphologyEx(imBin, cv2.MORPH_OPEN, kernelOp)
                mask2 = cv2.morphologyEx(imBin2, cv2.MORPH_OPEN, kernelOp)
                # Closing (dilate -> erode) to join white regions.
                mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernelCl)
                mask2 = cv2.morphologyEx(mask2, cv2.MORPH_CLOSE, kernelCl)
            except:
                print('SAYMA İŞİ BİTTİ')

                break

            # RETR_EXTERNAL returns only extreme outer flags. All child contours are left behind.
            contours0, hierarchy = cv2.findContours(mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours0:
                rect = cv2.boundingRect(cnt)
                area = cv2.contourArea(cnt)
                if area > areaTH:

                    M = cv2.moments(cnt)
                    cx = int(M['m10'] / M['m00'])
                    cy = int(M['m01'] / M['m00'])
                    x, y, w, h = cv2.boundingRect(cnt)

                    new = True
                    if cy in range(up_limit, down_limit):
                        for i in persons:
                            if abs(cx - i.getX()) <= w and abs(cy - i.getY()) <= h:

                                new = False
                                i.updateCoords(cx, cy)
                                if i.going_UP(line_down, line_up) == True:
                                    if w > 100:
                                        self.count_up = w / 60
                                        print()
                                    else:
                                        self.cnt_up += 1
                                    # print("ID:", i.getId(), 'crossed going up at', time.strftime("%c"))
                                elif i.going_DOWN(line_down, line_up) == True:
                                    if w > 100:
                                        self.count_down = w / 60
                                    else:
                                        self.cnt_down += 1
                                    # print("ID:", i.getId(), 'crossed going down at', time.strftime("%c"))
                                break
                            if i.getState() == '1':
                                if i.getDir() == 'down' and i.getY() > down_limit:
                                    i.setDone()
                                elif i.getDir() == 'up' and i.getY() < up_limit:
                                    i.setDone()
                            if i.timedOut():
                                # get out of the people list
                                index = persons.index(i)
                                persons.pop(index)
                                del i  # free the memory of i
                        if new is True:
                            p = Person(pid, cx, cy, max_p_age)
                            persons.append(p)
                            pid += 1

                    cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # for i in persons:
            #    cv2.putText(frame, str(i.getId()), (i.getX(), i.getY()), font, 0.3, i.getRGB(), 1, cv2.LINE_AA)

            frame = cv2.polylines(frame, [pts_L1], False, line_down_color, thickness=2)
            frame = cv2.polylines(frame, [pts_L2], False, line_up_color, thickness=2)

            frame = cv2.polylines(frame, [pts_L3], True, (255, 255, 255), thickness=1)
            frame = cv2.polylines(frame, [pts_L4], False, (255, 255, 255), thickness=1)

            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)

        #################
        self.cap.release()
        cv2.destroyAllWindows()
