import anthropic
import instructor
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Literal, Optional

load_dotenv()


class User(BaseModel):
    name: str
    age: int
    role: Literal["admin", "premium", "free"]
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


"""
User(name='Alex Thompson', age=28, role='premium', email='alex.thompson@email.com')
"""

print(user.model_dump_json(indent=2))

"""
{
  "name": "Alex Thompson",
  "age": 28,
  "role": "premium",
  "email": "alex.thompson@email.com"
}
"""
