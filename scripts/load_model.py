"""
🔽 Script to pre-download HuggingFace model into local cache (./models/distilbert).
Run this once so production doesn’t need to download on startup.
"""

import os
from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_NAME = os.getenv("MODEL_NAME", "distilbert-base-uncased")
MODEL_PATH = os.getenv("MODEL_PATH", "./models/distilbert")
HF_TOKEN = os.getenv("HF_TOKEN", None)

os.makedirs(MODEL_PATH, exist_ok=True)

print(f"⬇️ Downloading {MODEL_NAME} into {MODEL_PATH} ...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, cache_dir=MODEL_PATH, token=HF_TOKEN)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, cache_dir=MODEL_PATH, token=HF_TOKEN)

print("✅ Model downloaded and cached successfully!")
