from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel
from typing import Literal, Optional

load_dotenv()


class User(BaseModel):
    name: str
    age: int
    role: Literal["admin", "premium", "free"]
    email: Optional[str] = None


client = OpenAI()

completion = client.beta.chat.completions.parse(
    model="gpt-5-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Create a random user profile."},
    ],
    response_format=User,
)

user: User | None = completion.choices[0].message.parsed

print(repr(user))

"""
User(name='Jordan Rivera', age=24, role='free', email='jordan.rivera@email.com')
"""

print(user.model_dump_json(indent=2))

"""
{
  "name": "Jordan Rivera",
  "age": 24,
  "role": "free",
  "email": "jordan.rivera@email.com"
}
"""
