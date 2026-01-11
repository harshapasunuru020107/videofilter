from modules_zyne.frame_extractor import extract_frames
from modules_zyne.hsv_analyzer import get_average_hsv
from modules_zyne.filter_selector import select_filter
from modules_zyne.filter_applier import apply_filter_to_video


def main():
    video_path = "input1.mp4"

    frames_folder = extract_frames(video_path)

    hue, saturation, brightness = get_average_hsv(frames_folder)
    print(f"Hue={hue:.2f}, Sat={saturation:.2f}, Val={brightness:.2f}")

    selected_filter = select_filter(hue, saturation, brightness)
    print(f"Applying filter: {selected_filter}")

    apply_filter_to_video(frames_folder, selected_filter)

    print("✅ Output video saved as output1.mp4")


if __name__ == "__main__":
    main()
