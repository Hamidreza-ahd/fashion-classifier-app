# 👕 Fashion Image Classifier (Flask + CNN)

## 📌 Overview
This project is a deep learning-based web application that classifies fashion images using a Convolutional Neural Network (CNN) trained on the Fashion-MNIST dataset.  
The trained model is deployed using Flask and provides a simple web interface for real-time image prediction.

Users can upload an image of a clothing item and receive:
- Predicted class label
- Confidence score
- Image preview

---

## 🚀 Features
- 🧠 CNN model trained on Fashion-MNIST dataset  
- 🌐 Web interface using Flask  
- 📸 Image upload and preview  
- 📊 Real-time prediction with confidence score  
- 🎯 Simple and lightweight UI  

---

## 🛠️ Tech Stack
- Python  
- TensorFlow / Keras  
- Flask  
- NumPy  
- Pillow (PIL)  
- HTML/CSS (inline in Flask)

---

## 📂 Project Structure
```
project/
│
├── app.py              # Flask web app
├── model.keras         # Trained CNN model
├── requirements.txt    # Dependencies
```

---

## ⚙️ How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Hamidreza-ahd/fashion-classifier-app/
cd your-repo-name
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
```bash
python app.py
```

### 4. Open in browser
```
http://127.0.0.1:5000
```

---

## 📊 Model Details
- Dataset: Fashion-MNIST  
- Architecture: Convolutional Neural Network (CNN)  
- Input shape: 28x28 grayscale images  
- Output classes: 10 clothing categories  

### Classes:
- T-shirt/top  
- Trouser  
- Pullover  
- Dress  
- Coat  
- Sandal  
- Shirt  
- Sneaker  
- Bag  
- Ankle boot  

---

## 📸 Example Output
- Upload an image of a clothing item  
- Model predicts the category  
- Displays confidence score (e.g., 0.91)

---

## 🎯 Purpose
This project was built as a learning step to:
- Practice deep learning model development  
- Understand model deployment using Flask  
- Build end-to-end ML applications  

---

## 📈 Future Improvements
- Improve UI/UX  
- Deploy on cloud (Render / Railway)  
- Add top-3 predictions  
- Convert to REST API  
- Mobile-friendly interface  

---

## 👤 Author
**Hamidreza Ahmadi**  
Computer Engineering Student  
Passionate about AI, Machine Learning, and Computer Vision  

---

## ⭐ If you like this project
Give it a star ⭐ and feel free to contribute or suggest improvements!
