import os
from pupil_detector import PupilDetector
from eye_plotter import EyePlotter
from media_manager import MediaManager

def main(video_input_path, video_output_path, video_index):
    '''Processes all video frames to track the pupil across given video'''

    # Initialize the necessary classes
    media_manager = MediaManager(video_input_path, video_output_path)
    pupil_detector = PupilDetector()
    eye_plotter = EyePlotter()

    # Process video frames until none are left
    while True:
        frame = media_manager.fetch_frame()
        if frame is None:
            break  
        pupil_coordinates = pupil_detector.detect_pupil(frame)
        eye_plotter.encircle_pupil(frame, pupil_coordinates) 
        media_manager.store_frame(frame) 

    pupil_sizes, frame_rate = pupil_detector.pupil_sizes, media_manager.frame_rate
    eye_plotter.plot_pupil_size(pupil_sizes, frame_rate, video_index, video_output_path[:-9])
    
    media_manager.cleanup()

if __name__ == "__main__":
    base_path = os.getcwd()
    parent_path = os.path.dirname(base_path)

    # Runs all the videos defaultly placed in /data
    for idx in [1, 2, 3, 4, 5, 6]:
        video_input_path = os.path.join(parent_path, 'data', f'eye{idx}.mp4')
        video_output_path = os.path.join(parent_path, 'results', f'eye{idx}.avi') 
        main(video_input_path, video_output_path, idx)
