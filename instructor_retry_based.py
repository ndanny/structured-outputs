import instructor
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel
from typing import Literal, Optional

load_dotenv()


class User(BaseModel):
    name: str
    age: int
    role: Literal["admin", "premium", "free"]
    email: Optional[str] = None


client = instructor.from_groq(Groq())

user: User = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Create a random user profile."},
    ],
    response_model=User,
    max_retries=3,
)

print(repr(user))

# User(name='Emma Johnson', age=27, role='premium', email=None)

"""
ON RETRIES:

[assistant]: {"name": "Jordan", "age": 24, "role": "superuser", "email": "bad"}
[user]: ValidationError: 
         - role: 'superuser' is not a valid literal. Must be 'admin', 'premium', or 'free'
         - email: invalid email format
         Please fix your response.
[assistant]: {"name": "Jordan", "age": 24, "role": "free", "email": "jordan@email.com"}


* Retries cost extra tokens + latency
"""
