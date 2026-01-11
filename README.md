\documentclass[12pt]{article}

\usepackage[a4paper, margin=1in]{geometry}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{listings}
\usepackage{xcolor}

\hypersetup{
    colorlinks=true,
    linkcolor=black,
    urlcolor=blue
}

\title{\textbf{VideoFilters \\ Automatic Video Filter Pipeline}}
\author{Harshapasunuru}


\begin{document}

\maketitle

\section{Introduction}
VideoFilters is a computer vision based video processing pipeline that automatically analyzes a video and applies a strong cinematic filter frame-by-frame to generate an enhanced output video.

This project demonstrates how videos can be treated as sequences of images and processed intelligently using OpenCV.

\section{Features}
\begin{itemize}
    \item Extracts frames from a video
    \item Analyzes average HSV (Hue, Saturation, Brightness)
    \item Automatically selects an appropriate filter
    \item Applies strong and clearly visible filters
    \item Modular and scalable architecture
    \item Built using OpenCV and NumPy
\end{itemize}

\section{Project Structure}
\begin{verbatim}
videofilters/
|
|-- main.py
|-- input1.mp4
|
|-- modules_zyne/
|   |-- __init__.py
|   |-- frame_extractor.py
|   |-- hsv_analyzer.py
|   |-- filter_selector.py
|   |-- filter_applier.py
|   |-- filters.py
|
|-- frames/
|-- output1.mp4
\end{verbatim}

\section{System Workflow}
\begin{center}
Input Video $\rightarrow$ Frame Extraction $\rightarrow$ HSV Analysis $\rightarrow$ Filter Selection $\rightarrow$ Filter Application $\rightarrow$ Output Video
\end{center}

\section{Available Filters}
The following strong filters are implemented:
\begin{itemize}
    \item Brighten
    \item Darken (Cinematic)
    \item Enhance (High Contrast)
    \item Warm
    \item Cool
    \item Sepia
    \item Vintage
    \item Black and White (High Contrast)
    \item Sketch
    \item Invert
\end{itemize}

\section{Requirements}
\begin{itemize}
    \item Python 3.10 or 3.11 (recommended)
    \item OpenCV
    \item NumPy
\end{itemize}

\subsection{Installing Dependencies}
\begin{lstlisting}[language=bash]
pip install opencv-python numpy
\end{lstlisting}

\section{How to Run}
\subsection{Step 1: Add Input Video}
Place a video in the project root directory and rename it as:
\begin{verbatim}
input1.mp4
\end{verbatim}

\subsection{Step 2: Run the Program}
\begin{lstlisting}[language=bash]
python main.py
\end{lstlisting}

\section{Output}
After execution:
\begin{itemize}
    \item frames folder is generated automatically
    \item output1.mp4 is created automatically
\end{itemize}

The output video should not be created manually.



If the output video is grayscale, the pipeline is working correctly.

\section{Future Enhancements}
\begin{itemize}
    \item Audio merging
    \item Faster in-memory processing
    \item AI-based filter scoring
    \item REST API integration
    \item Video quality analysis
\end{itemize}

\section{Author}
Harsha \\
Computer Vision and Backend Developer

\section{Conclusion}
VideoFilters demonstrates a clean and modular approach to video processing using computer vision principles. The project forms a strong foundation for future AI-based video enhancement systems.

\end{document}
