from flask import Flask,request,jsonify
from pizzapred import FoodClassification
import os

app = Flask(__name__)

@app.route("/guess-this",methods=["POST"])

def classify_image():
    if "image" not in request.files:
        return "No Image given"
    
    img_dir = "./input_images"
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)

    image_file = request.files["image"]
    img_path = img_dir + image_file.filename
    image_file.save(img_path)

    food = FoodClassification()
    pred = food.main(img_path)

    return jsonify(
        {"food":pred}
    )

if __name__=="__main__":
    app.run(host="0.0.0.0",post=5000)