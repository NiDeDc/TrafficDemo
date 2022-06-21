import numpy as np
import matplotlib.pyplot as plt
import cv2
from LoadData import LoadData

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


class TrafficSeek:
    def __init__(self):
        self.ld = LoadData()
        self.data = np.zeros((73, 4))
        self.ld.ReadData()

    def Seek(self):
        # data = self.ld.GetData()
        # data = np.sum(data, axis=0)
        # data = np.abs(data.reshape((4, 73)).T)
        # max_d = np.max(data)
        # min_d = np.min(data)
        # data = ((data - min_d) / max_d * 255).astype(np.uint8)
        # # plt.imshow(data, cmap='gray', aspect='auto')
        # # plt.colorbar()
        # # plt.show()
        # cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        # # img = cv2.imread('linepicture.png', cv2.IMREAD_GRAYSCALE)
        # cv2.imshow('image', data)
        # cv2.waitKey(0)
        # pass
        for i in range(0, 60000, 50):
            data = self.ld.GetData()
            data = np.sum(data, axis=0)
            data = np.abs(data.reshape((4, 73)).T)
            # max_d = np.max(data)
            # min_d = np.min(data)
            # data = ((data - min_d) / max_d * 255).astype(np.uint8)
            data = data.astype(np.uint8)
            thresh, data = cv2.threshold(data, 50, 255, cv2.THRESH_BINARY)
            cv2.namedWindow('image', cv2.WINDOW_NORMAL)
            # img = cv2.imread('linepicture.png', cv2.IMREAD_GRAYSCALE)
            cv2.imshow('image', data)
            cv2.waitKey(50)
            # plt.get_current_fig_manager().window.state('zoomed')
            # plt.subplots_adjust(left=0.04, bottom=None, right=0.96, top=None, wspace=None, hspace=0.5)
            # file_name = 'S1_C' + str(self.ld.index) + '_P' + str(4) + '_'
            # self.data.tofile(file_name + '.bin')
