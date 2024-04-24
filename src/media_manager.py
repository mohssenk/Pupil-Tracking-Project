import cv2

class MediaManager:
    ''' Handles video reading and writing operations '''

    def __init__(self, video_input_path, video_output_path, codec='XVID'):
        self.capture = cv2.VideoCapture(video_input_path)

        if not self.capture.isOpened():
            raise Exception(f"Failed to open video file: {video_input_path}")
        
        self.frame_width = int(self.capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.frame_rate = self.capture.get(cv2.CAP_PROP_FPS) 

        codec_fourcc = cv2.VideoWriter_fourcc(*codec)
        self.writer = cv2.VideoWriter(video_output_path, codec_fourcc, self.frame_rate, (self.frame_width, self.frame_height))

    def fetch_frame(self):
        successful, frame = self.capture.read()
        return frame if successful else None

    def store_frame(self, frame):
        self.writer.write(frame)

    def cleanup(self):
        self.capture.release()
        self.writer.release()
