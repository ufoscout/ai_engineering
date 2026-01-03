from dotenv import dotenv_values
from smolagents import CodeAgent, DuckDuckGoSearchTool, InferenceClientModel, tool

@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggests a menu based on the occasion.
    Args:
        occasion (str): The type of occasion for the party. Allowed values are:
                        - "casual": Menu for casual party.
                        - "formal": Menu for formal party.
                        - "superhero": Menu for superhero party.
                        - "custom": Custom menu.
    """
    if occasion == "casual":
        return "Pizza, snacks, and drinks."
    elif occasion == "formal":
        return "3-course dinner with wine and dessert."
    elif occasion == "superhero":
        return "Buffet with high-energy and healthy food."
    else:
        return "Custom menu for the butler."
    

def main():
    
    config = dotenv_values("../../../.env")

    # An agent that uses the DuckDuckGoSearchTool
    agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=InferenceClientModel(
        token=config.get("HF_TOKEN")
    ))
    agent.run("Search for the best music recommendations for a party at the Wayne's mansion.")


    # An agent that uses our custom suggest_menu tool
    agent = CodeAgent(tools=[suggest_menu], model=InferenceClientModel(
        token=config.get("HF_TOKEN")
    ))
    agent.run("Prepare a formal menu for the party.")

    
    # An agent that is allowed to use the datetime module in the generated code
    agent = CodeAgent(tools=[], model=InferenceClientModel(
        token=config.get("HF_TOKEN")
    ), additional_authorized_imports=['datetime'])

    agent.run(
        """
        Alfred needs to prepare for the party. Here are the tasks:
        1. Prepare the drinks - 30 minutes
        2. Decorate the mansion - 60 minutes
        3. Set up the menu - 45 minutes
        3. Prepare the music and playlist - 45 minutes

        If we start right now, at what time will the party be ready?
        """
    )

if __name__ == "__main__":
    main()
