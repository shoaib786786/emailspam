# MODELS
import os
MODEL_VERSION = "0.0.1"
PATH_TO_PREPROCESSOR = f"/Users/mohammedzaidsyed/Desktop/Spam/spamclassification/web_service/saved_pkl/dv__v{MODEL_VERSION}.pkl"
PATH_TO_MODEL = f"/Users/mohammedzaidsyed/Desktop/Spam/spamclassification/web_service/saved_pkl/model__v{MODEL_VERSION}.pkl"

CATEGORICAL_COLS = ["label", "text", "label_num"]

# MISC
APP_TITLE = "Email Spam Classification"
APP_DESCRIPTION = (
    "Spam Classification "
    "classifying whether spam or ham "
)
APP_VERSION = "0.0.1"