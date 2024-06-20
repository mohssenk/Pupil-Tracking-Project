import os
from main import main

if __name__ == "__main__":
    base_path = os.getcwd()
    parent_path = os.path.dirname(base_path)

    # This runs on a new file added to /data
    new_file = input("Enter a string name of an mp4 file [DONT NOT INLCUDE .mp4]:\n")
    video_input_path = os.path.join(parent_path, 'data', f'{new_file}.mp4')
    if not os.path.exists(video_input_path):
        print("File does not exist.")
        exit()  # Exit the program if the file does not exist
    else: print("File exists.")

    video_output_path = os.path.join(parent_path, 'results', f'{new_file}.avi') 
    main(video_input_path, video_output_path, '')
