from PIL import Image, ImageStat
import numpy as np

def is_blurry(image_path, threshold=100):
    img = Image.open(image_path).convert("L")
    arr = np.array(img, dtype=np.float32)
    # variance of Laplacian approx for sharpness
    lap = np.gradient(np.gradient(arr)[0])[0] ** 2
    score = lap.mean()
    return score < threshold

def is_too_dark(image_path, min_brightness=50):
    img = Image.open(image_path)
    stat = ImageStat.Stat(img)
    brightness = sum(stat.mean)/3
    return brightness < min_brightness
