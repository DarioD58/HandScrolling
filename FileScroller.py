from pynput.mouse import  Controller

class FileScroller():
    def __init__(self) -> None:
        self.mouse = Controller()
        self.landmark_right = 0.0
        self.landmark_left = 0.0

    def update(self, landmarks, orientation):
        if orientation[0].classification[0].label == 'Left':
            if landmarks.landmark[8].y < self.landmark_left - 0.05:
                self.mouse.scroll(0, -1)
                self.landmark_left = landmarks.landmark[8].y
            else:
                self.landmark_left = landmarks.landmark[8].y
        elif orientation[0].classification[0].label == 'Right':
            if landmarks.landmark[8].y > self.landmark_right + 0.05:
                self.mouse.scroll(0, 1)
                self.landmark_right = landmarks.landmark[8].y
            else:
                self.landmark_right = landmarks.landmark[8].y
