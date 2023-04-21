import cv2
import tkinter

class App:
	def __init__(self, window, window_title):
		self.window = window
		self.window.title(window_title)
		self.window.mainloop()

App(tkinter.Tk(), window_title="Window")

class MyVideoCapture:
	def __init__(self, video_source=0):
		self.vid = cv2.VideoCapture(video_source)
		if not self.vid.isOpened():
			raise ValueError("Unable to open source", video_source)
		self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
		self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)


	def __del__(self):
		if self.vid.isOpened():
			self.vid.release()
		self.window.mainloop()

	def 