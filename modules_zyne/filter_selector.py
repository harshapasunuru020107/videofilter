def select_filter(hue, saturation, value):
    if hue < 20 and saturation < 50:
        return 'black_and_white'
    elif hue > 100 and saturation > 100:
        return 'cool'
    elif hue < 30 and value > 150:
        return 'brighten'
    elif hue < 30 and value < 100:
        return 'darken'
    elif 30 <= hue <= 60:
        return 'warm'
    elif 60 < hue <= 90:
        return 'enhance'
    elif 90 < hue <= 120:
        return 'sepia'
    elif hue > 120:
        return 'sketch'
    else:
        return 'enhance'  # default fallback
