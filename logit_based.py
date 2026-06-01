"""
Logit-based structured generation with Outlines:

+-----+     +--------+     +------------+     +---------------+
| llm | --> | logits | --> | new logits | --> | probabilities |
+-----+     +--------+     +------------+     +---------------+

Invalid tokens are set to -infinity before softmax,
so the model literally cannot generate them.
No retries needed.

Example — generating the "role" field in User:

    Model sees: '{"name": "John", "age": 25, "role": "'

    Raw logits:
        "admin":    6.2   ← valid, kept
        "premium":  5.8   ← valid, kept
        "free":     4.1   ← valid, kept
        "manager":  3.9   → set to -inf (not in Literal)
        "user":     3.4   → set to -inf (not in Literal)
        "owner":    2.1   → set to -inf (not in Literal)

    After softmax:
        "admin":   52%
        "premium": 35%
        "free":    13%
"""

import outlines
from transformers import AutoTokenizer, AutoModelForCausalLM
from pydantic import BaseModel
from typing import Literal, Optional


class User(BaseModel):
    name: str
    age: int
    role: Literal["admin", "premium", "free"]
    email: Optional[str] = None


MODEL_NAME = "HuggingFaceTB/SmolLM2-135M-Instruct"


model = outlines.from_transformers(
    AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto"),
    AutoTokenizer.from_pretrained(MODEL_NAME),
)

result = model("Create a random user profile.", User, max_new_tokens=200)

user = User.model_validate_json(result)

print(repr(user))

# User(name='John Doe', age=25, role='admin', email='johndoe@gmail.com')

"""
WITHOUT Outlines (prompt hacking a tiny model):

    {"name": John Smith, "age": 28, "role": "free",}

    json.loads() → JSONDecodeError
"""
