from pydantic import BaseModel, Field, field_validator # Gold standard in Python for data validation. BaseModel is the core class you inherit from to create a data schema.
from typing import List

class ReceiptData(BaseModel):
    # Define the fields.
    merchant: str = Field(description="Name of the store or business")
    total: float = Field(description="The final total amount paid")
    items: List[str] = Field(default_factory=list, description="List of items purchased")
    tax_amount: float = Field(description="The tax amount paid")

    # Additional check on the Total field, to catch any negative numbers. 
    @field_validator('total')
    @classmethod
    def total_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Total must be a positive number")
        return v