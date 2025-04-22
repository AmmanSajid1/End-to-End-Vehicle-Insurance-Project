# 🚗 Vehicle Insurance Prediction using MLOps

**An end-to-end Machine Learning project to predict vehicle insurance interest, deployed using modern MLOps and FastAPI for a blazing-fast web interface.**

This project predicts whether a customer is likely to be interested in vehicle insurance using features like demographics, vehicle info, and policy data. It incorporates full-scale **MLOps best practices**, cloud infrastructure, CI/CD automation, containerization, and a production-ready **FastAPI backend**.

---

## 🌟 Key Highlights

- ✅ **End-to-End ML Pipeline**: From data ingestion to deployment.
- ⚡ **FastAPI Backend**: Super-fast, async-ready web API for real-time inference.
- ☁️ **Cloud-Native**: MongoDB Atlas for data storage, AWS S3 for model registry, EC2 for hosting.
- 🐳 **Dockerized Deployment**: Easily portable, cloud-ready builds.
- 🔁 **CI/CD Automation**: GitHub Actions with EC2 self-hosted runner.
- 📦 **Modular Codebase**: Built for maintainability and scalability.
- 🔐 **Secure Secrets**: AWS keys & DB strings managed via environment variables.

---

## 🧠 Problem Statement

Build a predictive model that classifies whether a customer is likely to be interested in purchasing **vehicle insurance**, using the following features:

- **Demographics**: Gender, Age, Region Code
- **Vehicle**: Vehicle Age, Vehicle Damage
- **Policy**: Premium, Sales Channel

---

## 🛠️ Tech Stack

| Category | Tool |
|---------|------|
| Language | Python 3.10 |
| API Framework | FastAPI |
| ML Framework | scikit-learn |
| Cloud Storage | MongoDB Atlas, AWS S3 |
| Cloud Hosting | AWS EC2 |
| CI/CD | GitHub Actions + EC2 Runner |
| Containerization | Docker, AWS ECR |
| Monitoring | Custom logging module |
| Infra Config | AWS IAM, S3, Secrets via GitHub Actions |

---

## 🧪 ML Pipeline Components

1. **Data Ingestion**  
   Pulls data from **MongoDB Atlas**, converts it into Pandas DataFrame.

2. **Data Validation**  
   Uses YAML schema to validate dataset structure and types.

3. **Data Transformation**  
   Applies encoding, scaling, and feature engineering.

4. **Model Training**  
   Trains using scikit-learn; saves model artifacts.

5. **Model Evaluation**  
   Deploys only if new model surpasses a 0.02 threshold improvement.

6. **Model Registry + Deployment**  
   Push/pull models from AWS S3; integrates with FastAPI backend.

7. **Prediction API with FastAPI**  
   Real-time scoring endpoint and `/train` route for retraining pipeline.

---

## 📦 Project Structure

```
├── .github/
│   └── workflows/                 # GitHub Actions for CI/CD
│
├── artifact/                     # Generated artifacts from each pipeline run
│   ├── 2025_04_22_*              # Timestamped artifact directories
│   │   ├── data_ingestion/
│   │   │   ├── feature_store/
│   │   │   └── ingested/
│   │   ├── data_validation/
│   │   ├── data_transformation/
│   │   │   ├── transformed/
│   │   │   └── transformed_object/
│   │   └── model_trainer/
│   │       └── trained_model/
│
├── config/                       # Configuration files
├── logs/                         # Logging outputs
├── notebooks/                    # EDA and MongoDB notebook
│
├── src/                          # Core source code
│   ├── cloud_storage/            # AWS S3 model push/pull logic
│   ├── components/               # ML pipeline components
│   ├── configuration/            # AWS, MongoDB connection setup
│   ├── constants/                # Constant and global variables
│   ├── data_access/              # MongoDB data retrieval logic
│   ├── entity/                   # Config classes, Estimators, Artifacts
│   ├── exception/                # Custom exception handling
│   ├── logger/                   # Custom logging module
│   ├── pipeline/                 # Training and prediction pipelines
│   ├── utils/                    # Utility functions
│
├── src.egg-info/                 # Package metadata for local imports
├── static/                       # Static assets (CSS, JS if needed)
│   └── css/
├── templates/                    # HTML templates for FastAPI (Jinja2)
│
├── app.py                        # FastAPI entrypoint
├── requirements.txt              # Python dependencies
├── setup.py                      # Setup script for packaging
├── pyproject.toml                # Modern Python packaging config
├── Dockerfile                    # Docker build file
├── .dockerignore                 # Docker ignore rules
└── README.md                     # Project documentation

```

---

## ⚡ FastAPI Endpoints

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET/POST | Home page to submit customer features, get prediction |
| `/train` | GET | Trigger model training pipeline |

---

## 🚀 Running the Project

```bash
# Step 1: Set up virtual environment
conda create -n vehicle python=3.10 -y
conda activate vehicle

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Start FastAPI server
python app.py
```

Access the API docs at:  
👉 `http://localhost:5000/docs` (FastAPI Swagger UI)

---

## 🔁 CI/CD and Deployment

- CI/CD with **GitHub Actions** and **self-hosted runner** on EC2
- Dockerized deployment pushed to **AWS ECR**
- EC2 instance hosts the container via exposed **port 5080**
- Secure keys & secrets managed via GitHub secrets

---

## 🎯 Future Enhancements

- Add Grafana + Prometheus for model & app monitoring
- Auto-scheduling retraining jobs with Apache Airflow
- Move to Kubernetes for scalable orchestration
- Frontend dashboard using React or Streamlit

---

## 📬 Let's Connect!

Want to talk MLOps, data, or tech in general?  
Feel free to [reach out on LinkedIn](https://www.linkedin.com/in/amman-sajid-47bb481ba/) or message me for collaboration opportunities.

---