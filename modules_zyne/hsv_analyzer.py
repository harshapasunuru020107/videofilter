import cv2
import numpy as np
import os

def get_average_hsv(frames_folder):
    total_brightness = 0
    total_saturation = 0
    total_hue = 0
    frame_count = 0

    for filename in sorted(os.listdir(frames_folder)):
        path = os.path.join(frames_folder, filename)
        frame = cv2.imread(path)
        if frame is None:
            continue  # Skip unreadable or non-image files

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        h_channel = hsv[:, :, 0]
        s_channel = hsv[:, :, 1]
        v_channel = hsv[:, :, 2]

        total_hue += h_channel.mean()
        total_saturation += s_channel.mean()
        total_brightness += v_channel.mean()
        frame_count += 1

    if frame_count == 0:
        return 0, 0, 0

    avg_hue = total_hue / frame_count
    avg_saturation = total_saturation / frame_count
    avg_brightness = total_brightness / frame_count

    return avg_hue, avg_saturation, avg_brightness
