
from huggingface_hub import InferenceClient


# Queries the model to get the capital of a country
def get_capital(client: InferenceClient, country: str) -> str:
    output = client.chat.completions.create(
        messages=[
            {"role": "user", "content": f"The capital of {country} is"},
        ],
        stream=False,
        max_tokens=20,
    )
    return output.choices[0].message.content