from pydantic import BaseModel, Field

class PredictRequest(BaseModel):
    """
    Request body schema for /predict endpoint.
    """
    text: str = Field(..., min_length=5, description="News article text to classify")

class PredictResponse(BaseModel):
    """
    Response schema for /predict endpoint.
    """
    label: str = Field(..., description="Predicted label: 'FAKE' or 'REAL'")
    confidence: float = Field(..., ge=0, le=1, description="Confidence score (0-1)")
