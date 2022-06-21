import numpy as np


class LoadData:
    def __init__(self):
        self.index = 0
        self.data = None

    def ReadData(self):
        bin_file = np.fromfile("D1_C1_P257_20220113115900.bin", dtype=np.float32)
        col = 257
        size = len(bin_file)
        row = int(size / col)
        data1 = bin_file.reshape((row, col))[0: 60000:, 162:235]
        bin_file = np.fromfile("D1_C2_P236_20220113115900.bin", dtype=np.float32)
        col = 236
        size = len(bin_file)
        row = int(size / col)
        data2 = bin_file.reshape((row, col))[0: 60000:, 153:226]
        bin_file = np.fromfile("D1_C3_P237_20220113115900.bin", dtype=np.float32)
        col = 237
        size = len(bin_file)
        row = int(size / col)
        data3 = bin_file.reshape((row, col))[0: 60000:, 151:224]
        bin_file = np.fromfile("D1_C4_P234_20220113115900.bin", dtype=np.float32)
        col = 234
        size = len(bin_file)
        row = int(size / col)
        data4 = bin_file.reshape((row, col))[0: 60000:, 151:224]
        self.data = np.hstack((data1, data2, data3, data4))

    def GetData(self):
        self.index = self.index + 50
        return self.data[self.index - 50: self.index, :]
