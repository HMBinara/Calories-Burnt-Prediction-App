# 🔥 BurnFit Dashboard - Calories Burnt Prediction App

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-ff4b4b)
![Machine Learning](https://img.shields.io/badge/ML-XGBoost-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📋 Overview

**BurnFit Dashboard** is a modern, interactive web application designed to predict the number of calories burned during physical activity. Powered by a Machine Learning model (XGBoost) and built with **Streamlit**, this application provides real-time estimates based on physiological data and exercise metrics.

Whether you are a fitness enthusiast or a data science learner, this dashboard offers a clean interface to explore how different factors like heart rate, duration, and body temperature affect calorie expenditure.

## ✨ Key Features

- **Real-time Prediction**: Instantly calculates calories burnt as you adjust input parameters.
- **Interactive Visualizations**: Dynamic charts powered by **Plotly** to visualize trends over time.
- **User-Friendly Interface**: Clean, responsive design with a sidebar for easy data input.
- **Comprehensive Metrics**: Takes into account Gender, Age, Height, Weight, Duration, Heart Rate, and Body Temperature.

## 🛠️ Technologies Used

- **Python**: Core programming language.
- **Streamlit**: For building the interactive web interface.
- **Pandas & NumPy**: For data manipulation and numerical operations.
- **Plotly**: For interactive graphing and data visualization.
- **Scikit-learn / XGBoost**: For the underlying machine learning model.

## 📂 Project Structure

```
Calories-Burnt-Prediction-App/
├── .vscode/               # VS Code settings
├── venv/                  # Virtual Environment
├── app.py                 # Main Streamlit application file
├── Cb_prediction.pkl      # Pre-trained Machine Learning model
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── LICENSE                # License file
```

## 🚀 Installation & Setup

Follow these steps to run the application locally on your machine.

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Calories-Burnt-Prediction-App.git
cd Calories-Burnt-Prediction-App
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
streamlit run app.py
```

The app will automatically open in your default web browser at `http://localhost:8501`.

## 💡 Usage

1.  Open the application in your browser.
2.  Use the **Sidebar** on the left to input your details:
    *   **Gender**: Male / Female
    *   **Age**: Years
    *   **Height & Weight**: Physical metrics
    *   **Duration**: Exercise time in minutes
    *   **Heart Rate**: Average beats per minute
    *   **Body Temperature**: In Celsius
3.  View the **Total Calories Burnt** prediction on the right card.
4.  Analyze the **Calorie Burn Trend** graph to see how calories increase with duration based on your current metrics.

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to fork the repository and submit a pull request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
*Developed with ❤️ by [HMbinara]*
