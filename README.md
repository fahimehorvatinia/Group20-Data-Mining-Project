# ESC-50 Environmental Sound Classification Project

**ECEN 758 Data Mining and Analysis - Fall 2025**

**Team Members:**
- Banghyon Lee (Joseph)
- Fahimeh Orvati Nia
- Nandhini Valiveti
- Sushama Perati

## Project Overview

This project implements comprehensive environmental sound classification using the ESC-50 dataset. We explore traditional machine learning methods, deep learning approaches, and transfer learning techniques to classify 50 different environmental sound categories.

## [View Results Website](results.html)

## Dataset

**ESC-50 Dataset:**
- 2000 audio recordings (5 seconds each)
- 50 environmental sound classes
- 40 examples per class
- Pre-arranged into 5 folds for cross-validation

## Features

### Feature Extraction
- **Traditional Features (176 features):**
  - MFCC (Mel-frequency cepstral coefficients)
  - Chroma features
  - Mel spectrogram
  - Spectral contrast
  - Tonnetz features

- **Transfer Learning Features:**
  - YAMNet embeddings (2048 features per audio file)

### Preprocessing
- Raw features
- Normalized features (StandardScaler)
- Selected features (Top 100 via Mutual Information)

## Models Implemented

### Team Member Contributions

#### Fahimeh Orvati Nia
- Naive Bayes Classifier
- 1D Convolutional Neural Network (CNN)

#### Banghyon Lee (Joseph)
- Random Forest
- Gradient Boosting
- XGBoost
- Transfer Learning with YAMNet + Random Forest
- MLP on YAMNet embeddings
- Self-Supervised Learning (Pseudo-Labeling)

#### Nandhini Valiveti
- Support Vector Machine (SVM) - Linear kernel
- Support Vector Machine (SVM) - RBF kernel
- Multi-Layer Perceptron (MLP)

#### Sushama Perati
- Logistic Regression
- K-Nearest Neighbors (KNN)

## Evaluation Metrics

All models are evaluated using:
- Accuracy
- Precision (macro-averaged)
- Recall (macro-averaged)
- F1-Score (macro-averaged)
- Confusion Matrices
- Learning Curves
- Feature Importance (where applicable)

## Project Structure

```
.
├── ESC_50_Complete_Project_All_Methods.ipynb  # Main project notebook
├── Project_Report.tex                          # IEEE format report
├── results.html                                # Results visualization website
├── data_out/                                   # Feature files (CSV)
│   ├── esc50_features_raw.csv
│   ├── esc50_features_normalized_corrected.csv
│   └── esc50_features_selected.csv
├── ESC-50_data/                               # Dataset (audio files excluded from repo)
│   └── meta/                                   # Metadata only
└── README.md                                  # This file
```

## Getting Started

### Prerequisites

```bash
pip install numpy pandas scikit-learn matplotlib seaborn tensorflow tensorflow-hub librosa xgboost jupyter
```

### Running the Project

1. Clone this repository:
```bash
git clone https://github.com/fahimehorvatinia/Group20-Data-Mining-Project.git
cd Group20-Data-Mining-Project
```

2. Download the ESC-50 dataset from [here](https://github.com/karolpiczak/ESC-50) and extract to `ESC-50_data/`

3. Open and run `ESC_50_Complete_Project_All_Methods.ipynb` in Jupyter Notebook

4. View results in `results.html` (generated after running the notebook)

## Key Features

- Unified data splitting ensuring all classes in train/val/test
- No data leakage between splits
- Comprehensive model comparison
- Transfer learning with YAMNet
- Self-supervised learning exploration
- GPU/CPU compatibility

## Results Summary

See the [Results Website](results.html) for detailed performance comparisons across all models and feature sets.

## Report

The project report is available in `Project_Report.tex` (IEEE conference format).

## License

This project is for educational purposes as part of ECEN 758 Data Mining and Analysis course.

## Acknowledgments

- ESC-50 dataset creators
- TensorFlow Hub for YAMNet model
- scikit-learn, TensorFlow, and other open-source libraries

