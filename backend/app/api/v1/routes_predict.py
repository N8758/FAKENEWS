from fastapi import APIRouter, Depends, HTTPException
from app.schemas.predict import PredictRequest, PredictResponse
from app.services.inference import get_prediction

router = APIRouter()

@router.post("/predict", response_model=PredictResponse, tags=["prediction"])
async def predict(request: PredictRequest):
    """
    Takes news text input and returns prediction (fake or real).
    """
    try:
        result = get_prediction(request.text)
        return PredictResponse(label=result["label"], confidence=result["confidence"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
