# Top Rated Movies - EDA, Feature Engineering & Modeling 

**Overview**

This repository analyzes a dataset of top-rated movies to perform exploratory data analysis (EDA), feature engineering, and train models to predict a movie's popularity. The work is organized into notebooks for EDA/FE and model training.

## Project structure 🔧

- `data/`
  - `Top_Rated_Movies.csv` — raw dataset used for EDA
  - `Top_Rated_Movies_Cleaned.csv` — cleaned dataset produced by the EDA notebook
- `notebooks/`
  - `Trm_EDA_FE.ipynb` — EDA and feature engineering (creates cleaned CSV)
  - `model_training.ipynb` — model training and evaluation (saves `rfr_model.pkl`)
- `model/` — where the model is stored
- `application.py` — small Flask API to serve predictions and list top movies
- `requirements.txt` — minimal dependencies for running the app

## Running the Flask app 🔧

1. Install dependencies:

```powershell
pip install -r requirements.txt
```

2. Run the app:

```powershell
python application.py
```





