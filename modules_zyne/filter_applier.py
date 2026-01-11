import cv2
import os
import modules_zyne.filters as filters


def apply_filter_to_video(frames_folder, selected_filter, output_path="output1.mp4", fps=30):
    frame_files = sorted(os.listdir(frames_folder))

    first_frame = cv2.imread(os.path.join(frames_folder, frame_files[0]))
    height, width, _ = first_frame.shape

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    filter_func = getattr(filters, selected_filter)

    for filename in frame_files:
        frame = cv2.imread(os.path.join(frames_folder, filename))
        if frame is None:
            continue

        filtered = filter_func(frame)

        # Handle grayscale filters
        if len(filtered.shape) == 2:
            filtered = cv2.cvtColor(filtered, cv2.COLOR_GRAY2BGR)

        out.write(filtered)

    out.release()
