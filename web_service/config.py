# MODELS
import os
MODEL_VERSION = "0.0.1"
PATH_TO_PREPROCESSOR = f"/Users/mohammedzaidsyed/Desktop/Spam/emailspam/web_service/dv_v/dv.pkl"
PATH_TO_MODEL = f"/Users/mohammedzaidsyed/Desktop/Spam/emailspam/web_service/model_v/model.pkl"
PATH_TO_TRAIN = "/Users/mohammedzaidsyed/Desktop/Spam/emailspam/data/train-set.csv"
PATH_TO_TEST = "/Users/mohammedzaidsyed/Desktop/Spam/emailspam/data/test-set.csv"

CATEGORICAL_COLS = ["text"]

# MISC
APP_TITLE = "Email Spam Classification"
APP_DESCRIPTION = (
    "Spam Classification "
    "classifying whether spam or ham "
)
APP_VERSION = "0.0.1"