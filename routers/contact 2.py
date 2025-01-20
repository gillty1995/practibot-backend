from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from services.email_service import send_email

router = APIRouter()

# Define the Pydantic model for request validation
class ContactRequest(BaseModel):
    name: str
    email: EmailStr
    message: str

@router.post("/contact")
async def contact_form(contact_request: ContactRequest):
    """
    Handles contact form submissions.

    Args:
        contact_request (ContactRequest): The validated contact form data.
    """
    try:
        # Send the email using the email service
        send_email(
            name=contact_request.name,
            email=contact_request.email,
            message=contact_request.message
        )
        return {"message": "Your message has been sent successfully!"}

    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to send email.")