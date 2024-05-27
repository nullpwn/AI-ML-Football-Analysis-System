# Football Analysis Project

## Introduction

The objective of this project is to detect and track players, referees, and footballs in a video using YOLO, a leading AI object detection model. We will enhance the model's performance through training. Additionally, players will be assigned to teams based on their t-shirt colors using Kmeans for pixel segmentation and clustering. This will enable us to measure a team's ball possession percentage during a match.

Optical flow will be utilized to gauge camera movement between frames, allowing precise measurement of player movements. Furthermore, perspective transformation will be applied to depict the scene's depth and perspective, enabling us to measure player movement in meters rather than pixels. Ultimately, we will calculate the speed and distance covered by players.

![Football Analysis](https://github.com/nullpwn/AI-ML-Football-Analysis-System/blob/main/output_videos/screenshot.png)


## Modules Used

The following modules are used in this project:

- **YOLO**: AI object detection model
- **Kmeans**: Pixel segmentation and clustering to detect t-shirt color
- **Optical Flow**: Measure camera movement
- **Perspective Transformation**: Represent scene depth and perspective
- **Speed and distance calculation per player**

## Trained Models

- Trained Yolo v5

## Sample Video

- [Sample input video](https://drive.google.com/file/d/1xpB9azsAdY_xoGzSRgctp2Km7d7jE8ts/view?usp=sharing)

## Requirements

## Requirements

To run this project, you need to have the following requirements installed:

- Python 3.x
- ultralytics
- supervision
- OpenCV
- NumPy
- Matplotlib
- Pandas
