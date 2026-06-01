from dotenv import load_dotenv

load_dotenv()

import anthropic
import instructor
from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    name: str
    age: int
    location: str
    email: Optional[str] = None


client = instructor.from_anthropic(anthropic.Anthropic())

user: User = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    temperature=1.0,
    messages=[
        {
            "role": "user",
            "content": "Create a random user profile.",
        }
    ],
    response_model=User,
)

print(repr(user))

# User(name='Marcus Chen', age=34, location='Portland, Oregon', email='marcus.chen@email.com')
