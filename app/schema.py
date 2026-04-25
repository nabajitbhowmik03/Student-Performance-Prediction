from pydantic import BaseModel, Field

class StudentInput(BaseModel):
    study_hours: float = Field(..., gt=0, description="Hours studied per day")
    attendance_percentage: int = Field(..., ge=0, le=100)
    previous_score: float = Field(..., ge=0, le=100)
    assignments_completed: int = Field(..., ge=0)

    class Config:
        schema_extra = {
            "example": {
                "study_hours": 5,
                "attendance_percentage": 85,
                "previous_score": 72,
                "assignments_completed": 8
            }
        }
