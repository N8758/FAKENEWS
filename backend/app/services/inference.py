import torch
import torch.nn.functional as F
from app.models.classifier import get_model

# Load model + tokenizer (singleton)
model, tokenizer = get_model()

def preprocess(text: str):
    """
    Preprocess input text using tokenizer.
    Returns tensors ready for model inference.
    """
    return tokenizer(
        text,
        padding=True,
        truncation=True,
        max_length=512,
        return_tensors="pt"
    )

def get_prediction(text: str):
    """
    Run inference on input text and return label + confidence.
    """
    inputs = preprocess(text)

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probs = F.softmax(logits, dim=-1).squeeze()

    # Argmax = predicted class
    predicted_class = torch.argmax(probs).item()
    confidence = probs[predicted_class].item()

    # Map index → label
    # Assumption: 0 = REAL, 1 = FAKE (adjust if dataset differs)
    label_map = {0: "REAL", 1: "FAKE"}
    label = label_map.get(predicted_class, "UNKNOWN")

    return {"label": label, "confidence": round(confidence, 4)}
