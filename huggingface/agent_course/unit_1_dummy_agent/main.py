from dotenv import dotenv_values
from huggingface_hub import InferenceClient

from country import get_capital
from weather import get_weather

def main():

    config = dotenv_values("../../../.env")

    client = InferenceClient(
        model="meta-llama/Llama-4-Scout-17B-16E-Instruct", 
        token=config.get("HF_TOKEN"), # If not passed, will use HF_TOKEN env variable
    )

    print("Ask the model to get the capital of France")
    capital = get_capital(client, "France")
    print(capital)
    print("------------------------------")

    print("Ask the model to get the capital of Germany")
    capital = get_capital(client, "Germany")
    print(capital)
    print("------------------------------")

    print("Ask the model to get the weather in London")
    weather = get_weather(client, "London")
    print(weather)
    print("------------------------------")



if __name__ == "__main__":
    main()
