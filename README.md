# Pupil Tracker

## Overview
This project aims to monitor a pupil's movements within a video. It follows the pupil's location over time and visualizes these findings effectively.

Examples of the tracker operating below:

The following is Eye Example 1 in /data
[![Watch the Video](path/to/video_thumbnail.jpg)](https://www.youtube.com/watch?v=Myv5pqWOFkM)

The following is Eye Example 2 in /data
[![Watch the Video](path/to/video_thumbnail.jpg)](https://www.youtube.com/watch?v=oSwysY2Rwqk)

## Summary

This eye tracker follows the pupil as it moves around. The tracker is designed for videos that stable and that focus on one eye (zoomed in closely) Fundamentally, the model operates by performing a contour analysis and then looking for a well-sized, round contour. It draws a red circle around the pupil to track it.

It also tracks the size of the pupil over time. This can be used to evaluate the model's performance, as large jumps in size can be indicative of inaccurate tracking.

Examples 3-6 demonstrate the advantages and limitations. Examples 4 and 5 showcase the strength of the model’s ability to track a moving pupil (though imperfect). Example 3 shows that glares can impact the model's ability to detect the pupil. Example 6 highlights some limitations when the pupil is not well contrasted with the surroundings.

## Features
- Pupil segmentation to identify the pupil in each frame.
- Visualizes change in pupil size over time.  

## Prerequisites
Ensure you have Python installed on your system. Also ensure the installation of open-cv, numpy, and matplotlib (listed in requirements.txt)

## Usage
Execute the `main.py` script in /src to run.

To run on a new file, upload video file into /data and run new_data.py, then type in the name of the file you wish to run the model on.

## Data
Video contains 6 example videos in /data, which are all processed with the project execution.

## Results
Processed videos and data visualizations are saved in the `results` directory.

## Credit
Credit to the videos belong to the following sources:

https://www.youtube.com/watch?v=-01-XBHXFq8&ab_channel=AJMAKESTHINGS

https://www.youtube.com/watch?v=P7nCvM9qMzE&ab_channel=StockFootage93

https://www.youtube.com/watch?v=Fmg9ZOHESgQ&t=96s&ab_channel=TheSlowMoGuys

https://www.youtube.com/watch?v=ePQSYhE_FHY&ab_channel=Newen
