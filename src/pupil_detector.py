import cv2
import numpy as np

class PupilDetector:
    ''' Implements pupil detection using image contours '''

    def __init__(self, threshold_min=20, threshold_max=255, area_min=5000, circ_min=0.5, circ_max=1.9): 
        self.threshold_min = threshold_min
        self.threshold_max = threshold_max
        self.area_min = area_min
        self.circ_min = circ_min
        self.circ_max = circ_max
        self.pupil_sizes = []

    def detect_pupil(self, frame): 
        grayscale = frame[:, :, 0]
        _, binary_image = cv2.threshold(grayscale, self.threshold_min, self.threshold_max, cv2.THRESH_BINARY_INV) 
        contours, _ = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            area = cv2.contourArea(contour)
            (center_x, center_y), radius = cv2.minEnclosingCircle(contour)
            area_circle = np.pi * (radius**2)
            circularity = area_circle / area if area > 0 else 0

            if area > self.area_min and self.circ_min < circularity < self.circ_max: 
                self.pupil_sizes.append(area_circle)
                return (int(center_x), int(center_y), int(radius)) 

        return (0, 0, 0)
