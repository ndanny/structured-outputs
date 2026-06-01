from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=256,
    system="Only output the raw JSON string, no markdown, no explanation.",
    messages=[
        {
            "role": "user",
            "content": "Generate a user JSON with name, age, role, and email.",
        },
    ],
)

print(message.content[0].text)

"""
```json
{
  "name": "John Doe",
  "age": 28,
  "role": "Software Engineer",
  "email": "john.doe@example.com"
}
```
"""
