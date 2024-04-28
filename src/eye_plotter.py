import cv2
import matplotlib.pyplot as plt
import os

class EyePlotter:
    ''' Facilitates the visualization of pupil detection results '''

    def __init__(self, circle_color=(0, 0, 255)): 
        self.circle_color = circle_color
    
    def encircle_pupil(self, frame, pupil_data):
        if pupil_data is not None:
            x, y, radius = map(int, map(round, pupil_data[:3]))
            if x != 0 and y != 0: 
                cv2.circle(frame, (x, y), radius, self.circle_color, 2) 
        return frame

    def plot_pupil_size(self, sizes, fps, output_dir, index=''):
        times = [i / fps for i in range(len(sizes))]
        plt.figure(figsize=(10, 5))
        plt.plot(times, sizes, label='Pupil Size', color='blue')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Pupil Size in Number of Pixels')
        plt.title('Pupil Size Over Time')
        plt.legend()
        plt.grid(True)
        plt.ylim(bottom=0)
        if index == '':
            file_path = os.path.join(output_dir, 'pupil_size_over_time_new_example.png')
        else: file_path = os.path.join(output_dir, f'pupil_size_over_time_{index}.png')
        plt.savefig(file_path)
