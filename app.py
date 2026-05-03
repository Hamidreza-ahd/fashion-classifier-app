from flask import Flask, request
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import base64

app = Flask(__name__)
model = load_model("model.keras")

classes = [
    "T-shirt/top","Trouser","Pullover","Dress","Coat",
    "Sandal","Shirt","Sneaker","Bag","Ankle boot"
]

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    confidence = None
    image_data = None
    message = None

    if request.method == "POST":
        file = request.files.get("image")

        if not file or file.filename == "":
            message = "Please upload an image"
        else:
            try:
                # برای نمایش عکس
                file_bytes = file.read()
                image_data = base64.b64encode(file_bytes).decode("utf-8")

                # پردازش تصویر
                img = Image.open(file.stream).convert("L")
                img = img.resize((28,28))

                img = np.array(img)/255.0
                img = 1 - img
                img = img.reshape(1,28,28,1)

                pred = model.predict(img)
                result = classes[np.argmax(pred)]
                confidence = float(np.max(pred))

            except:
                message = "Invalid image file"

    return f"""
    <html>
    <head>
    <style>
    body {{
        font-family: Arial;
        background: linear-gradient(to right, #ece9e6, #ffffff);
        text-align: center;
        padding-top: 40px;
    }}

    .container {{
        background: white;
        padding: 30px;
        margin: auto;
        width: 400px;
        border-radius: 12px;
        box-shadow: 0px 5px 20px rgba(0,0,0,0.1);
    }}

    button {{
        background: #4CAF50;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 6px;
        cursor: pointer;
    }}

    button:hover {{
        background: #45a049;
    }}

    img {{
        margin-top: 15px;
        border-radius: 10px;
        max-width: 200px;
    }}

    .result {{
        margin-top: 20px;
        font-size: 18px;
        color: #333;
    }}

    .error {{
        color: red;
        margin-top: 15px;
    }}
    </style>
    </head>

    <body>

    <div class="container">
        <h1>👕 Fashion Classifier</h1>

        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="image"><br><br>
            <button type="submit">Predict</button>
        </form>

        {f'<img src="data:image/png;base64,{image_data}">' if image_data else ""}

        {f'''
        <div class="result">
            <p><b>Prediction:</b> {result}</p>
            <p><b>Confidence:</b> {confidence:.2f}</p>
        </div>
        ''' if result else ""}

        {f'<div class="error">{message}</div>' if message else ""}

    </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)