from flask import json, jsonify, render_template, request, redirect, url_for, session, flash
from application import app
import cv2
import numpy as np
from PIL import Image #    pip install pillow
import numpy as np
import base64
import io
import cv2

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
batchcount = 0

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/inputimg', methods=['GET', 'POST'])
def inputimg():
    if request.method == 'POST':
        file = request.files['imgfile']
        print(file)
        if 'imgfile' not in request.files:
            flash('No file uploaded')
            print("No file uploaded")
            return render_template("index.html")
        file = request.files['imgfile']
        im = Image.open(file)
        img_data = display(im)
        return render_template("index.html", img_data=img_data)
    return render_template("index.html")

@app.route('/translation', methods=['GET', 'POST'])
def translation():
    if request.method == 'POST':
        # Get the JSON data from the request
        img_data = request.json['img_data'] 
        
        img = convertinit(img_data)

        # Define the translation matrix
        translation_matrix = np.float32([[1, 0, 50], [0, 1, 50]])

        # Apply the translation
        translated_image = cv2.warpAffine(img, translation_matrix, (img.shape[1], img.shape[0]))

        # Encode the modified image back to base64
        pil_image = Image.fromarray(translated_image)
        img_data = display(pil_image)
    return jsonify({"img_data":img_data})

@app.route('/rotation', methods=['GET', 'POST'])
def rotation():
    if request.method == 'POST':
        # Get the JSON data from the request
        img_data = request.json['img_data'] 
        
        img = convertinit(img_data)

        # Define the rotation angle
        angle = 30  # Degrees

        # Calculate the image's center point
        center = (img.shape[1] // 2, img.shape[0] // 2)

        # Rotate the image
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1)
        rotated_image = cv2.warpAffine(img, rotation_matrix, (img.shape[1], img.shape[0]))

        # Encode the modified image back to base64
        pil_image = Image.fromarray(rotated_image)
        img_data = display(pil_image)
    return jsonify({"img_data":img_data})

@app.route('/scaling', methods=['GET', 'POST'])
def scaling():
    if request.method == 'POST':
        # Get the JSON data from the request
        img_data = request.json['img_data'] 
        
        img = convertinit(img_data)

        # Define the scaling factors
        scaling_factor_x = 2
        scaling_factor_y = 0.5

        # Compute the scaling matrix
        scaling_matrix = np.float32([[scaling_factor_x, 0, 0], [0, scaling_factor_y, 0]])

        # Apply the scaling
        scaled_image = cv2.warpAffine(img, scaling_matrix, (img.shape[1], img.shape[0]))

        # Encode the modified image back to base64
        pil_image = Image.fromarray(scaled_image)
        img_data = display(pil_image)
    return jsonify({"img_data":img_data})

@app.route('/shearing', methods=['GET', 'POST'])
def shearing():
    if request.method == 'POST':
        # Get the JSON data from the request
        img_data = request.json['img_data'] 
        
        img = convertinit(img_data)

         # Define the shearing matrix
        shearing_matrix = np.float32([[1, 0.5, 0], [0.5, 1, 0]])

        # Apply the shearing
        sheared_image = cv2.warpAffine(img, shearing_matrix, (img.shape[1], img.shape[0]))

        # Encode the modified image back to base64
        pil_image = Image.fromarray(sheared_image)
        img_data = display(pil_image)
    return jsonify({"img_data":img_data})

def display(im):
    data = io.BytesIO()
    im.save(data, "JPEG")
    #Then encode the saved image file.
    encoded_img_data = base64.b64encode(data.getvalue())
    img_data = encoded_img_data.decode('utf-8')
    return img_data

def convertinit(img_data):
    img_base64 = img_data.split(",")[1]

    # Decode the base64 data
    image_bytes = base64.b64decode(img_base64)

    # Create a BytesIO object
    image_data = io.BytesIO(image_bytes)

    # Open the image with PIL
    pil_image = Image.open(image_data)
    img = np.array(pil_image)
    return img
