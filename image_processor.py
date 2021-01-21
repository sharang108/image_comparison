import os
import cv2
import numpy as np
# import scipy.spatial as scipy


class ImageProcessor:


	FILE_PATH = "./files/"
	RESIZE_DIM = (400, 400)

	def __init__(self, pivot_img, compare_img):
		self.pivot_img = pivot_img
		self.compare_img = compare_img

	def write_tmp_files(self, file_name, file_data):
		file_path = os.path.join(
					ImageProcessor.FILE_PATH, str(file_name)
				)
		with open(file_path, 'wb') as tmp_file:
			for chunk in file_data.chunks():
				tmp_file.write(chunk)
		return cv2.imread(file_path)

	def preprocess(self, file_name, data):
		img_data = self.write_tmp_files(file_name, data)
		img_data = cv2.resize(img_data, ImageProcessor.RESIZE_DIM, interpolation=cv2.INTER_CUBIC)
		img_data = np.float32(img_data/255)
		histr = cv2.calcHist([img_data], [0, 1, 2], None, [256, 256, 256], [0, 1, 0, 1, 0, 1])
		histr = cv2.normalize(histr, histr)
		return histr

	def check_similarity_score(self):
		file_pivot = str(self.pivot_img) + ".jpg"
		file_compare = str(self.compare_img) + ".jpg"
		pivot_hist = self.preprocess(file_pivot, self.pivot_img)
		compare_hist = self.preprocess(file_compare, self.compare_img)
		score = cv2.compareHist(compare_hist, pivot_hist, cv2.HISTCMP_CORREL) * 100
		# print(scipy.distance.chebyshev(compare_hist, pivot_hist), "chebyshev distance")
		return score
