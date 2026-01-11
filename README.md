VideoFilters is a modular computer vision–based video processing pipeline that automatically analyzes a video and applies a suitable strong, cinematic filter frame-by-frame to generate an enhanced output video.

This project demonstrates how videos can be treated as image sequences and processed intelligently using OpenCV.

 Features:
         1 .Extracts frames from a video
         2.Analyzes average HSV (Hue, Saturation, Brightness)
         3.Automatically selects an appropriate filter
         4.Applies strong, clearly visible filters
         5.Clean, modular architecture
         6.Built using OpenCV & NumPy
 
 Project Structure:
 videofilters/
│
├── main.py
├── input1.mp4                 # Input video (user provided)
│
├── modules_zyne/
│   ├── __init__.py
│   ├── frame_extractor.py     # Video → frames
│   ├── hsv_analyzer.py        # HSV analysis
│   ├── filter_selector.py     # Filter decision logic
│   ├── filter_applier.py      # Applies filter & rebuilds video
│   └── filters.py             # Strong cinematic filters
│
├── frames/                    # Auto-generated
├── output1.mp4                # Auto-generated

HOW IT WORKS:

Input Video
   ↓
Frame Extraction
   ↓
HSV Color Analysis
   ↓
Filter Selection
   ↓
Filter Application
   ↓
Output Video




