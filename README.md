# Pupil Tracker

## Overview
This project aims to monitor the pupil's movements within video data. It processes video inputs to identify and follow the pupil's location over time, and visualizes these findings effectively.

Examples of the tracker operating below:

The following is Eye Example 1 in /data
[![Watch the Video](path/to/video_thumbnail.jpg)](https://www.youtube.com/watch?v=Myv5pqWOFkM)

The following is Eye Example 2 in /data
[![Watch the Video](path/to/video_thumbnail.jpg)](https://www.youtube.com/watch?v=oSwysY2Rwqk)

## Summary

This eye tracker follows the pupil as it moves around in a zoomed-in eye. Fundamentally, the model operates by performing a contour analysis and then looking for a well-sized, round contour. It draws a red circle around the pupil to track it.

It also tracks the size of the pupil over time. This can be used to evaluate the model's performance, as large jumps in size can be indicative of inaccurate tracking.

Examples 3-6 demonstrate the advantages and limitations. Examples 4 and 5 showcase the strength of the model’s ability to track a moving eye (though imperfect). Example 3 shows that glares can impact the model's ability to detect the pupil. Example 6 highlights some limitations when the pupil is not well contrasted with the surroundings.

## Features
- Pupil segmentation to identify the pupil in each frame.
- Visualizes change in pupil size over time.  

## Prerequisites
Ensure you have Python installed on your system. Also ensure the instillation of open-cv, numpy, and matplotlib (listed in requirements.txt)

## Usage
Execute the `main.py` script in /src to run.

To run on a new file, upload video file into /data and comment in the final block in main.py, which allows one to input a new file name to process. The block that processes the default files may also be commented out if needed.

## Data
Video contains 6 example videos in /data, which are all processed with the project execution

## Results
Processed videos and data visualizations are saved in the `results` directory.
