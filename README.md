# 🛡️ Network Security: ML-Powered Phishing Detection System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-green?style=for-the-badge&logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-Latest-green?style=for-the-badge&logo=mongodb)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-blue?style=for-the-badge&logo=mlflow)

**An Enterprise-Grade End-to-End ML Pipeline for Real-Time Phishing Detection**

</div>

---

## 📋 Overview

**Network Security** is a production-ready machine learning system that detects and prevents phishing attacks through intelligent network data analysis. Built with a focus on scalability, reliability, and performance, this project implements a complete MLOps pipeline using industry-standard tools and best practices.

The system processes raw network data through automated ingestion, validation, transformation, and model training stages, then serves real-time predictions via a high-performance FastAPI service integrated with MLflow for experiment tracking and DagsHub for model versioning.

---

## ✨ Key Features

- 🔄 **Automated Data Ingestion Pipeline** - Seamlessly loads phishing network data from CSV into MongoDB
- ✅ **Robust Data Validation** - Schema validation with comprehensive error handling
- 🔧 **Intelligent Data Transformation** - Feature engineering and preprocessing optimized for ML models
- 🤖 **Advanced Model Training** - Multiple ensemble algorithms (Random Forest, Gradient Boosting, AdaBoost, Logistic Regression)
- ⚡ **Real-Time Prediction API** - FastAPI service for instant phishing detection on new data
- 📊 **MLOps Integration** - MLflow tracking + DagsHub versioning for reproducible experiments
- 🐳 **Docker Ready** - Containerized deployment for seamless cloud integration
- 📈 **Performance Monitoring** - Classification metrics and model evaluation
- 🔐 **Production-Grade** - Exception handling, logging, and error management throughout

---

## 🏗️ Architecture

```
Network Security ML Pipeline
├── 📥 Data Ingestion (CSV → MongoDB)
├── ✔️ Data Validation (Schema Check)
├── 🔄 Data Transformation (Feature Engineering)
├── 🎯 Model Training (Ensemble Methods)
└── 🚀 Prediction Service (FastAPI REST API)
```

**Tech Stack:**
- **Data Processing:** Pandas, NumPy, Scikit-learn
- **ML Frameworks:** Scikit-learn, MLflow, DagsHub
- **Backend:** FastAPI, Uvicorn
- **Database:** MongoDB
- **MLOps:** MLflow, DagsHub
- **Environment:** Python 3.9+

---

## 🚀 Installation

### Prerequisites

Ensure you have the following installed:

- **Python 3.9+** - [Download Python](https://www.python.org/)
- **MongoDB** - [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) (Cloud) or [Local Installation](https://www.mongodb.com/docs/manual/installation/)
- **Git** - Version control system
- **pip** - Python package manager

### Step-by-Step Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Miskat362/network-security-ml.git
   cd network-security-ml
   ```

2. **Create Virtual Environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Create a `.env` file in the root directory:
   ```env
   MONGODB_URL_KEY=mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority
   ```

5. **Verify Installation**
   ```bash
   python -c "import network_security; print('Installation successful!')"
   ```

---

## 💡 Quick Start

### 1. Train the Model

**Using the Training Pipeline:**
```bash
python main.py
```

**Using the FastAPI Endpoint:**
```bash
# Start the server
uvicorn app:app --reload

# In another terminal, trigger training
curl http://localhost:8000/train
```

### 2. Make Predictions

**Using the REST API:**
```bash
# Start the FastAPI server
uvicorn app:app --reload

# Make a prediction request
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d @sample_data.json
```

### 3. Monitor Experiments

Open MLflow UI to track model experiments:
```bash
mlflow ui
```
Visit `http://localhost:5000` in your browser.

### 4. View API Documentation

Start the server and navigate to:
- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

---

## 📁 Project Structure

```
network-security-ml/
├── 📄 app.py                          # FastAPI application entry point
├── 📄 main.py                         # Training pipeline execution script
├── 📄 setup.py                        # Package setup configuration
├── 📄 requirements.txt                # Python dependencies
├── 📄 Dockerfile                      # Docker container configuration
├── 📄 README.md                       # This file
│
├── 🔐 network_security/               # Main package directory
│   ├── __init__.py
│   ├── 📁 components/                 # ML pipeline components
│   │   ├── data_ingestion.py         # MongoDB data loading
│   │   ├── data_validation.py        # Schema & data quality validation
│   │   ├── data_transformation.py    # Feature engineering & preprocessing
│   │   └── model_trainer.py          # Model training & evaluation
│   │
│   ├── 📁 pipeline/                   # Orchestration
│   │   ├── training_pipeline.py      # End-to-end training workflow
│   │   └── batch_prediction.py       # Batch prediction module
│   │
│   ├── 📁 entity/                     # Data structure definitions
│   │   ├── config_entity.py          # Configuration classes
│   │   └── artifact_entity.py        # Artifact classes
│   │
│   ├── 📁 exception/                  # Error handling
│   │   └── exception.py              # Custom exceptions
│   │
│   ├── 📁 logging/                    # Logging configuration
│   │   └── logger.py                 # Custom logger setup
│   │
│   ├── 📁 constant/                   # Constants & configurations
│   │   └── training_pipeline/        # Pipeline-specific constants
│   │
│   ├── 📁 utils/                      # Utility functions
│   │   ├── main_utils/
│   │   │   └── utils.py              # General utilities
│   │   └── ml_utils/
│   │       ├── model/
│   │       │   └── estimator.py      # Model wrapper
│   │       └── metric/
│   │           └── classification_metric.py  # Evaluation metrics
│   │
│   └── 📁 cloud/                      # Cloud integration (future)
│
├── 📊 data_schema/
│   └── schema.yaml                    # Data schema definition
│
├── 📂 network_data/
│   └── phishingData.csv              # Source phishing dataset
│
├── 📂 Artifacts/                      # Generated models & artifacts
│   └── {timestamp}/
│       ├── data_ingestion/
│       ├── data_validation/
│       ├── data_transformation/
│       └── model_trainer/
│
├── 📂 final_model/                    # Final trained model storage
│
└── 📂 logs/                           # Application logs
```

---

## 🔄 Pipeline Workflow

The system follows a well-defined ML pipeline with the following stages:

```
┌─────────────┐
│  Raw Data   │ (CSV files in network_data/)
└──────┬──────┘
       │
       ▼
┌─────────────────────┐
│ Data Ingestion      │ Loads data from CSV → MongoDB
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Data Validation     │ Validates schema & data quality
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Data Transformation │ Feature engineering & preprocessing
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Model Training      │ Trains ensemble models, logs with MLflow
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Prediction Service  │ REST API for real-time inference
└─────────────────────┘
```

---

## 🛠️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# MongoDB Connection
MONGODB_URL_KEY=mongodb+srv://user:password@cluster.mongodb.net/

# MLflow & DagsHub (Optional)
MLFLOW_TRACKING_URI=http://localhost:5000
MLFLOW_EXPERIMENT_NAME=network-security-phishing-detection
```

### Data Schema

Define your data validation schema in `data_schema/schema.yaml`:

```yaml
name: phishing_data
version: 1.0
columns:
  - feature_name: string
  - feature_value: float
required: true
```

---

## 📊 Supported Models

The project supports multiple ensemble and classical algorithms:

- **Random Forest Classifier** - Robust ensemble method
- **Gradient Boosting Classifier** - Advanced boosting technique
- **AdaBoost Classifier** - Adaptive boosting
- **Logistic Regression** - Linear baseline model

Model selection and hyperparameter tuning are handled automatically during training.

---

## 🐳 Docker Deployment

Build and run the application in a Docker container

---

## 📈 Model Performance

The trained models are evaluated using comprehensive classification metrics:

- **Accuracy** - Overall correctness
- **Precision** - True positive rate among predictions
- **Recall** - True positive rate among actual positives
- **F1-Score** - Harmonic mean of precision and recall
- **ROC-AUC** - Area under the receiver operating characteristic curve

All metrics are logged in MLflow for experiment tracking.

---
### Development Setup

```bash
# Install development dependencies
pip install -r requirements.txt

```
---

## 👨‍💻 Author

**Miskat Ahmmed**
- 📧 Email: memiskat362@gmail.com
- 🔗 GitHub: [@Miskat362](https://github.com/Miskat362)
- 🐍 LinkedIn: [Connect](https://linkedin.com/in/miskat-ahmmed)

---

## ✔ Acknowledgments

- **Scikit-learn** - Machine learning library
- **FastAPI** - Modern web framework
- **MLflow** - Experiment tracking
- **DagsHub** - ML versioning and collaboration
- **MongoDB** - NoSQL database

---
#### 🤝 Contributions are welcome!

---
<div align="center">

**⭐ If you found this project helpful, please star it! ⭐**

</div>