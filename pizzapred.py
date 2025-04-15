import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image as i

class FoodClassification():
    def __init__(self):
        self.model = tf.keras.models.load_model("pizza_steak.keras")
        self.image = None

    def main(self,image):
        self.parse(image)
        pred = self.model.predict(self.image)
        if pred >=0.5:
            return "steak"
        else:
            return "pizza"
        
    def parse_image(self,image):
        img = i.load_img(image,target_size = (224,224))
        self.image = i.img_to_array(img)
        self.image = np.expand_dims(self.image,axis)
        self.image/=255.0

if __name__ == "__main__":
    img = ""
    food=FoodClassification()
    food.main(img)
