import cv2
import numpy as np

# 🔥 1. STRONG BRIGHTEN
def brighten(frame):
    return cv2.convertScaleAbs(frame, alpha=1.4, beta=60)


# 🔥 2. STRONG DARKEN (cinematic)
def darken(frame):
    return cv2.convertScaleAbs(frame, alpha=0.6, beta=-40)


# 🔥 3. HIGH CONTRAST POP
def enhance(frame):
    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)

    merged = cv2.merge((cl, a, b))
    return cv2.cvtColor(merged, cv2.COLOR_LAB2BGR)


# 🔥 4. VERY STRONG SEPIA
def sepia(frame):
    kernel = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])
    sepia_frame = cv2.transform(frame, kernel)
    return np.clip(sepia_frame, 0, 255).astype(np.uint8)


# 🔥 5. STRONG COOL (BLUE CINEMA)
def cool(frame):
    b, g, r = cv2.split(frame)
    b = cv2.add(b, 60)
    r = cv2.subtract(r, 40)
    return cv2.merge((b, g, r))


# 🔥 6. STRONG WARM (ORANGE CINEMA)
def warm(frame):
    b, g, r = cv2.split(frame)
    r = cv2.add(r, 60)
    b = cv2.subtract(b, 40)
    return cv2.merge((b, g, r))


# 🔥 7. TRUE BLACK & WHITE (HIGH CONTRAST)
def black_and_white(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return cv2.equalizeHist(gray)


# 🔥 8. CINEMATIC SKETCH
def sketch(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    inv = 255 - gray
    blur = cv2.GaussianBlur(inv, (25, 25), 0)
    sketch = cv2.divide(gray, 255 - blur, scale=256)
    return cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)


# 🔥 9. VINTAGE FILM LOOK
def vintage(frame):
    sep = sepia(frame)
    noise = np.random.randint(0, 30, frame.shape, dtype=np.uint8)
    return cv2.addWeighted(sep, 0.9, noise, 0.1, 0)


# 🔥 10. DRAMATIC INVERT
def invert(frame):
    return cv2.bitwise_not(frame)
