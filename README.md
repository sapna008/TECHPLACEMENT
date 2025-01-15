# Internship Tasks Repository

This repository contains two distinctive projects completed during internship:
1. Random Password Generator
2. Fruit Object Detection Application

## 📁 Repository Structure

```
root/
├── Task1/
│   └── Password Generator/
└── Task2/
    └── Fruit Detection App/
```

## 🔐 Task 1: Random Password Generator

A Python-based application that generates secure random passwords based on specified criteria.

### Features
- Customizable password length
- Mix of uppercase and lowercase letters
- Special characters and numbers
- Secure random generation

### Usage
```python
# Example usage of password generator
python password_generator.py
```

## 🍎 Task 2: Fruit Detection Application

A Streamlit-based web application that identifies fruits from uploaded images using a TensorFlow/Keras deep learning model.

### Technologies Used
- Python
- Streamlit
- TensorFlow/Keras
- NumPy
- Deep Learning for Image Classification

### Key Dependencies
```python
numpy
tensorflow
keras
streamlit
```

### Installation

1. Clone the repository
```bash
git clone [your-repository-link]
cd [project-directory]
```

2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages
```bash
pip install -r requirements.txt
```

### Running the Applications

#### Password Generator
```bash
cd Task1
python password_generator.py
```

#### Fruit Detection App
```bash
cd Task2
streamlit run app.py
```

### 🎯 How the Fruit Detection Works

1. **Image Input**
   - User uploads an image through the Streamlit interface
   - Image is preprocessed using NumPy

2. **Model Processing**
   ```python
   import numpy as np
   import tensorflow as tf
   from tensorflow import keras
   from tensorflow.keras.models import load_model
   import streamlit as st
   ```
   - Image is converted to appropriate format
   - Pre-trained model processes the image
   - Prediction results are displayed

3. **Output**
   - Displays the detected fruit name
   - Shows confidence score (if implemented)

## 🛠️ Technical Requirements

- Python 3.7+
- TensorFlow 2.x
- Streamlit
- NumPy
- Appropriate GPU drivers (optional, for faster processing)

## 📋 Setup Instructions

1. **Environment Setup**
   ```bash
   pip install numpy tensorflow tensorflow-keras streamlit
   ```

2. **Running the Applications**
   - Navigate to respective task directories
   - Follow individual task instructions

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## 🐛 Known Issues & Future Improvements

- List any known issues
- Potential improvements for password generator
- Possible enhancements for fruit detection model
- UI/UX improvements

## 📞 Contact

[Sapna Sarkar] - [sapnapks1@gmail.com]

Project Link: [https://github.com/sapna008/TECHPLACEMENT.git]((https://github.com/sapna008/TECHPLACEMENT.git))

## 🙏 Acknowledgments

- TensorFlow team for the deep learning framework
- Streamlit team for the web app framework
- Dataset sources (if applicable)
