from PIL import Image
import numpy as np

def preprocess_image(image_path, target_size=(224,224)):
    img = Image.open(image_path).convert("RGB")
    img = img.resize(target_size)
    img_array = np.array(img) / 255.0  # normalize
    img_array = img_array.reshape((1, *target_size, 3))  # batch dimension
    return img_array
